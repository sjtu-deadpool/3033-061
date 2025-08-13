#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Gemini API IMDB ID Lookup Tool for MovieLens
Uses natural language queries and detailed movie information from u.item
"""

import pandas as pd
import re
import json
import time
import requests
import random
from typing import Optional, Dict, List, Tuple
import os
from datetime import datetime

# Gemini API Configuration
GEMINI_API_KEY = ""  # Please fill in your Gemini API key here
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# Movie Genre Mapping (based on u.genre)
GENRE_MAPPING = {
    0: "unknown", 1: "action", 2: "adventure", 3: "animation", 4: "children's", 5: "comedy",
    6: "crime", 7: "documentary", 8: "drama", 9: "fantasy", 10: "film-noir",
    11: "horror", 12: "musical", 13: "mystery", 14: "romance", 15: "sci-fi",
    16: "thriller", 17: "war", 18: "western"
}

class MovieInfo:
    """Movie information class with natural language query generation"""
    def __init__(self, movie_id: int, title: str, year: str, genres: List[str], release_date: str = ""):
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.genres = genres
        self.release_date = release_date
        
        # Extract clean title (remove year)
        self.clean_title = re.sub(r'\s*\(\d{4}\)$', '', title)
    
    def get_genre_description(self) -> str:
        """Get genre description for natural language"""
        if not self.genres or self.genres == ["unknown"]:
            return "movie"
        elif len(self.genres) == 1:
            return f"{self.genres[0]} movie"
        else:
            return f"{self.genres[0]} and other genres movie"
    
    def get_natural_query(self) -> str:
        """Generate natural language query"""
        genre_desc = self.get_genre_description()
        
        # Construct more natural query sentences
        queries = [
            f"What is the IMDB ID for the {self.year} {genre_desc} '{self.clean_title}'?",
            f"Please tell me the IMDB number for '{self.clean_title}' ({self.year}), a {genre_desc}",
            f"IMDB ID for {self.clean_title} ({self.year}) - {genre_desc}",
            f"Find IMDB identifier for the {self.year} film '{self.clean_title}' which is a {genre_desc}"
        ]
        
        return random.choice(queries)

class GeminiIMDbLookup:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': api_key
        }
        self.request_count = 0
        self.success_count = 0
        self.error_count = 0
        
    def query_gemini(self, prompt: str) -> Optional[str]:
        """Query Gemini API"""
        if not self.api_key:
            print("Error: Please set Gemini API key")
            return None
            
        url = GEMINI_API_URL
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        
        try:
            self.request_count += 1
            response = requests.post(url, headers=self.headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                if 'candidates' in data and len(data['candidates']) > 0:
                    content = data['candidates'][0]['content']['parts'][0]['text']
                    self.success_count += 1
                    return content
                else:
                    print(f"No content in API response: {data}")
                    self.error_count += 1
                    return None
            elif response.status_code == 429:
                # Handle rate limiting
                print("⏳ API rate limit reached, waiting 30 seconds...")
                time.sleep(30)
                return self.query_gemini(prompt)  # Retry
            else:
                print(f"API request failed: {response.status_code} - {response.text}")
                self.error_count += 1
                return None
                
        except requests.exceptions.Timeout:
            print("API request timeout")
            self.error_count += 1
            return None
        except Exception as e:
            print(f"API request exception: {e}")
            self.error_count += 1
            return None
    
    def extract_imdb_id(self, text: str) -> Optional[str]:
        """Extract IMDB ID from text"""
        if not text:
            return None
            
        # Match pattern: tt + 7 digits
        pattern = r'tt(\d{7})'
        matches = re.findall(pattern, text, re.IGNORECASE)
        
        if matches:
            # Return first match (without tt prefix)
            return matches[0]
        
        # If standard format not found, try other possible formats
        # Match pure numeric ID (might not have tt prefix)
        pattern2 = r'\b(\d{7})\b'
        matches2 = re.findall(pattern2, text)
        
        if matches2:
            return matches2[0]
            
        return None
    
    def lookup_movies_batch(self, movies_batch: List) -> Dict[int, str]:
        """Batch lookup multiple movies' IMDB IDs using natural language"""
        if not movies_batch:
            return {}
        
        # Construct natural language batch queries
        queries = []
        for i, movie in enumerate(movies_batch, 1):
            if hasattr(movie, 'get_natural_query'):
                query = movie.get_natural_query()
            else:
                # Backward compatibility with dict format
                query = f"{movie['title']} ({movie['year']})"
            queries.append(f"{i}. {query}")
        
        query_text = "\n".join(queries)
        
        prompt = f"""I need to find IMDB IDs for the following movies. Please help me find their accurate IMDB numbers (format: tt + 7 digits):

{query_text}

Please respond in the following format, one movie per line:
1. tt0114709 - Toy Story (1995)
2. tt0113189 - GoldenEye (1995)  
3. tt0113228 - Four Rooms (1995)
4. unknown - if you're not sure about a movie's IMDB ID
5. tt0114885 - Babe (1995)

Please ensure:
- Each line starts with a number (1-{len(movies_batch)})
- IMDB ID format is tt + 7 digits
- Write "unknown" or "not found" if uncertain
- Keep the movie order unchanged"""
        
        print(f"🔍 Querying {len(movies_batch)} movies...")
        print("Query content:")
        for query in queries:
            print(f"  {query}")
        
        # Call API
        response = self.query_gemini(prompt)
        
        if response:
            print(f"📝 Gemini response:\n{response}")
            return self.parse_batch_response(response, movies_batch)
        
        return {}
    
    def parse_batch_response(self, response: str, movies_batch: List) -> Dict[int, str]:
        """Parse batch query results"""
        results = {}
        lines = response.strip().split('\n')
        
        print(f"🔍 Parsing response, {len(lines)} lines total")
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
                
            print(f"  Parsing line {line_num}: {line}")
            
            # Try to match format: number. tt1234567 - movie name
            pattern = r'^(\d+)\.\s*(tt\d{7}|unknown|not found)'
            match = re.match(pattern, line, re.IGNORECASE)
            
            if match:
                seq_num = int(match.group(1))
                imdb_info = match.group(2).lower()
                
                # Check if sequence number is within valid range
                if 1 <= seq_num <= len(movies_batch):
                    movie = movies_batch[seq_num - 1]
                    movie_id = movie.movie_id if hasattr(movie, 'movie_id') else movie['movie_id']
                    
                    if imdb_info.startswith('tt') and len(imdb_info) == 9:
                        # Extract 7-digit ID
                        imdb_id = imdb_info[2:]  # Remove tt prefix
                        results[movie_id] = imdb_id
                        title = movie.clean_title if hasattr(movie, 'clean_title') else movie['title']
                        print(f"    ✅ {seq_num}. {title} -> {imdb_id}")
                    else:
                        title = movie.clean_title if hasattr(movie, 'clean_title') else movie['title']
                        print(f"    ❓ {seq_num}. {title} -> not found")
                else:
                    print(f"    ⚠️ Sequence number out of range: {seq_num}")
            else:
                # Try to extract IMDB ID directly from line
                imdb_pattern = r'tt(\d{7})'
                imdb_matches = re.findall(imdb_pattern, line, re.IGNORECASE)
                if imdb_matches:
                    print(f"    📝 Extracted IMDB IDs from line: {imdb_matches}")
                    
                    # Try to match to corresponding movie
                    for movie in movies_batch:
                        title = movie.clean_title if hasattr(movie, 'clean_title') else movie['title']
                        if title.lower() in line.lower():
                            if imdb_matches:
                                movie_id = movie.movie_id if hasattr(movie, 'movie_id') else movie['movie_id']
                                results[movie_id] = imdb_matches[0]
                                print(f"    🎯 Matched: {title} -> {imdb_matches[0]}")
                                break
        
        return results
    
    def get_stats(self) -> Dict:
        """Get query statistics"""
        return {
            'total_requests': self.request_count,
            'successful': self.success_count,
            'errors': self.error_count,
            'success_rate': self.success_count / max(self.request_count, 1) * 100
        }

def load_movielines_data_with_genres() -> pd.DataFrame:
    """Load detailed movie data with genre information from u.item"""
    print("📚 Loading detailed movie information from u.item...")
    
    try:
        # Define column names
        columns = ['movie_id', 'title', 'release_date', 'video_date', 'imdb_url'] + \
                  [f'genre_{i}' for i in range(19)]  # 19 genre flag bits
        
        # Read u.item file
        df = pd.read_csv('ml-100k/u.item', sep='|', names=columns, encoding='latin1')
        
        print(f"📊 Successfully loaded {len(df)} movies")
        
        # Process genre information
        def extract_genres(row):
            genres = []
            for i in range(19):
                if row[f'genre_{i}'] == 1:
                    genre_name = GENRE_MAPPING.get(i, f"genre{i}")
                    genres.append(genre_name)
            return genres if genres else ["unknown"]
        
        # Extract year
        def extract_year(title):
            match = re.search(r'\((\d{4})\)', title)
            return match.group(1) if match else ""
        
        # Apply processing
        df['genres'] = df.apply(extract_genres, axis=1)
        df['year'] = df['title'].apply(extract_year)
        
        print("✅ Movie genre information processed")
        return df
        
    except FileNotFoundError:
        print("❌ ml-100k/u.item file not found")
        return None
    except Exception as e:
        print(f"❌ Failed to read movie data: {e}")
        return None

def create_movie_info_objects(df: pd.DataFrame) -> List[MovieInfo]:
    """Create MovieInfo object list"""
    movie_infos = []
    for _, row in df.iterrows():
        movie_info = MovieInfo(
            movie_id=row['movie_id'],
            title=row['title'],
            year=row['year'],
            genres=row['genres'],
            release_date=row['release_date']
        )
        movie_infos.append(movie_info)
    
    print(f"📋 Created {len(movie_infos)} movie info objects")
    return movie_infos

def load_movie_data() -> pd.DataFrame:
    """Legacy function for backward compatibility"""
    return load_movielines_data_with_genres()

def load_existing_mapping() -> Dict[int, str]:
    """Load existing IMDB ID mapping"""
    mapping_file = "imdb/progress_mapping.json"
    
    # First try to read progress from imdb folder
    if os.path.exists(mapping_file):
        try:
            with open(mapping_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Convert string keys to integer keys
                known_ids = {int(k): v for k, v in data.items()}
                print(f"📂 Loaded {len(known_ids)} known IMDB IDs from progress file")
                return known_ids
        except Exception as e:
            print(f"⚠️ Failed to read progress file: {e}")
    
    # Alternative: read from generate_real_imdb_mapping.py
    try:
        from generate_real_imdb_mapping import KNOWN_IMDB_IDS
        print(f"📚 Loaded {len(KNOWN_IMDB_IDS)} known IMDB IDs from original file")
        return KNOWN_IMDB_IDS
    except ImportError:
        print("🆕 No existing mapping found, starting with empty mapping")
        return {}

def save_progress_mapping(known_ids: Dict[int, str]):
    """Save progress to imdb folder"""
    # Ensure imdb folder exists
    os.makedirs("imdb", exist_ok=True)
    
    # Save progress JSON file
    progress_file = "imdb/progress_mapping.json"
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(known_ids, f, ensure_ascii=False, indent=2)
    
    print(f"💾 Progress saved to: {progress_file}")
    return progress_file

def save_final_mapping(known_ids: Dict[int, str], movie_infos: List[MovieInfo]):
    """Generate final mapping file"""
    # Ensure imdb folder exists
    os.makedirs("imdb", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'imdb/enhanced_imdb_mapping_{timestamp}.py'
    
    # Create movie_id to MovieInfo mapping
    movie_dict = {m.movie_id: m for m in movie_infos}
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""\n')
        f.write('MovieLens 100k IMDB ID Mapping (Enhanced Version)\n')
        f.write(f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write(f'Progress: {len(known_ids)}/{len(movie_infos)} ({len(known_ids)/len(movie_infos)*100:.1f}%)\n')
        f.write('Using enhanced Gemini API with natural language queries\n')
        f.write('"""\n\n')
        
        f.write('# MovieLens 100k IMDB ID Mapping\n')
        f.write(f'# Total verified IDs: {len(known_ids)}\n\n')
        
        f.write('KNOWN_IMDB_IDS = {\n')
        for movie_id in sorted(known_ids.keys()):
            if movie_id in movie_dict:
                movie = movie_dict[movie_id]
                imdb_id = known_ids[movie_id]
                genres_str = ', '.join(movie.genres[:2])  # Only show first two genres
                f.write(f'    {movie_id}: "{imdb_id}",    # {movie.clean_title} ({movie.year}) - {genres_str}\n')
        f.write('}\n\n')
        
        f.write('# Complete movie list format\n')
        f.write('IMDB_LIST = [\n')
        for movie in movie_infos:
            if movie.movie_id in known_ids:
                imdb_id = known_ids[movie.movie_id]
                f.write(f'    "{imdb_id}",  # {movie.movie_id}. {movie.clean_title} ({movie.year}) - VERIFIED\n')
            else:
                placeholder_id = f"{'0' * (7 - len(str(movie.movie_id)))}{movie.movie_id}"
                f.write(f'    "{placeholder_id}",  # {movie.movie_id}. {movie.clean_title} ({movie.year}) - PLACEHOLDER\n')
        f.write(']\n\n')
        
        f.write('if __name__ == "__main__":\n')
        f.write(f'    print(f"Total movies: {len(movie_infos)}")\n')
        f.write(f'    print(f"Verified IDs: {len(known_ids)}")\n')
        f.write(f'    print(f"Progress: {len(known_ids)/len(movie_infos)*100:.1f}%")\n')
    
    print(f"📄 Final mapping saved to: {output_file}")
    return output_file

def main():
    """Main function"""
    print("=== Enhanced Gemini API IMDB ID Lookup Tool ===")
    print("✨ Using natural language queries with detailed movie info")
    print("=" * 60)
    
    # Check API key
    api_key = GEMINI_API_KEY or os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ Error: Please set Gemini API key")
        print("Method 1: Set GEMINI_API_KEY variable in script")
        print("Method 2: Set GEMINI_API_KEY environment variable")
        print("Get API key: https://makersuite.google.com/app/apikey")
        return
    
    # Load detailed movie data
    movies_df = load_movielines_data_with_genres()
    if movies_df is None:
        return
    
    # Create movie info objects
    movie_infos = create_movie_info_objects(movies_df)
    
    # Load existing mapping
    known_ids = load_existing_mapping()
    
    # Initialize enhanced lookup
    lookup = GeminiIMDbLookup(api_key)
    
    # Calculate movies to lookup
    known_movie_ids = set(known_ids.keys())
    movies_to_lookup = [m for m in movie_infos if m.movie_id not in known_movie_ids]
    
    print(f"\n📊 Statistics:")
    print(f"   Total movies: {len(movie_infos)}")
    print(f"   Known IMDB IDs: {len(known_ids)}")
    print(f"   Movies to lookup: {len(movies_to_lookup)}")
    
    if len(movies_to_lookup) == 0:
        print("✅ All movies already have IMDB IDs!")
        return
    
    # Set batch parameters (changed to 5 per batch)
    movies_per_batch = 5  # Process 5 movies per batch
    total_batches = (len(movies_to_lookup) + movies_per_batch - 1) // movies_per_batch
    
    print(f"\n📋 Batch processing setup:")
    print(f"   Movies per batch: {movies_per_batch}")
    print(f"   Total batches: {total_batches}")
    print(f"   Remaining movies: {len(movies_to_lookup)}")
    
    # Show example queries for movies to be processed
    print(f"\n🎬 Movie query examples:")
    for i, movie in enumerate(movies_to_lookup[:3]):
        genres_str = ', '.join(movie.genres[:2])  
        print(f"   {i+1}. {movie.clean_title} ({movie.year}) - {genres_str}")
        print(f"      Query: {movie.get_natural_query()}")
    
    if len(movies_to_lookup) > 3:
        print(f"   ... and {len(movies_to_lookup) - 3} more movies")
    
    # User confirmation for batches to process
    max_batches = min(3, total_batches)  # Recommend max 3 batches (5 movies each)
    try:
        batches_to_process = int(input(f"\nEnter number of batches to process (recommend 1-{max_batches}, {movies_per_batch} movies each): ") or "1")
    except ValueError:
        batches_to_process = 1
    
    if batches_to_process > total_batches:
        batches_to_process = total_batches
        print(f"Adjusted to maximum available batches: {batches_to_process}")
    
    # Process movies
    processed = 0
    new_ids_found = 0
    
    print(f"\n🚀 Starting to process {batches_to_process} batches, total {min(batches_to_process * movies_per_batch, len(movies_to_lookup))} movies...")
    
    for batch_num in range(batches_to_process):
        start_idx = batch_num * movies_per_batch
        end_idx = min(start_idx + movies_per_batch, len(movies_to_lookup))
        
        # Prepare current batch movies
        current_batch = movies_to_lookup[start_idx:end_idx]
        
        print(f"\n📦 Batch {batch_num + 1}/{batches_to_process} (movies {start_idx + 1}-{end_idx}):")
        for i, movie in enumerate(current_batch):
            genres_str = ', '.join(movie.genres[:2])
            print(f"   {i + 1}. {movie.clean_title} ({movie.year}) - {genres_str}")
        
        # Batch lookup IMDB IDs
        batch_results = lookup.lookup_movies_batch(current_batch)
        
        # Update results
        for movie_id, imdb_id in batch_results.items():
            known_ids[movie_id] = imdb_id
            new_ids_found += 1
        
        processed += len(current_batch)
        
        print(f"🎯 Batch {batch_num + 1} completed: found {len(batch_results)}/{len(current_batch)} IMDB IDs")
        
        # Save progress (save after each batch)
        save_progress_mapping(known_ids)
        print(f"📊 Current progress: {len(known_ids)}/{len(movie_infos)} ({len(known_ids)/len(movie_infos)*100:.1f}%)")
        
        # Delay between batches
        if batch_num < batches_to_process - 1:
            print("⏳ Waiting 10 seconds before next batch...")
            time.sleep(10)
    
    # Show statistics
    stats = lookup.get_stats()
    print(f"\n📈 Processing completed statistics:")
    print(f"   Movies processed: {processed}")
    print(f"   New IDs found: {new_ids_found}")
    print(f"   API requests: {stats['total_requests']}")
    print(f"   Success rate: {stats['success_rate']:.1f}%")
    print(f"   Total IMDB IDs: {len(known_ids)} / {len(movie_infos)} ({len(known_ids)/len(movie_infos)*100:.1f}%)")
    
    # Save final results
    if new_ids_found > 0:
        final_file = save_final_mapping(known_ids, movie_infos)
        print(f"\n💾 Final results saved to: {final_file}")
        
        print(f"\n💡 Next steps:")
        print(f"   📂 Progress file: imdb/progress_mapping.json")
        print(f"   📄 Final file: {final_file}")
        print(f"   🔄 Continue running this script to find more IDs")
        print(f"   📊 Current completion: {len(known_ids)/len(movie_infos)*100:.1f}%")
    else:
        print("\n😔 No new IMDB IDs found this time")
    
    print(f"\n🎉 Enhanced version features:")
    print(f"   ✨ Natural language queries improve accuracy")
    print(f"   🎭 Movie genre information included")
    print(f"   📦 Small batch processing (5 movies/batch) improves success rate")
    print(f"   🔍 Enhanced response parsing algorithm")

def test_api():
    """Test API connection"""
    api_key = GEMINI_API_KEY or os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Please set API key first")
        return
    
    lookup = GeminiIMDbLookup(api_key)
    print("Testing API connection...")
    
    # Test with a well-known movie using new MovieInfo format
    test_movie = MovieInfo(1, "Toy Story (1995)", "1995", ["animation", "children's"])
    result = lookup.lookup_movies_batch([test_movie])
    if result:
        print(f"✅ API test successful! Toy Story (1995) -> {list(result.values())[0] if result else 'None'}")
    else:
        print("❌ API test failed")
    
    stats = lookup.get_stats()
    print(f"Statistics: {stats}")

if __name__ == "__main__":
    # If you need to test API, uncomment the line below
    # test_api()
    
    main()