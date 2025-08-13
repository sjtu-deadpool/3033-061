#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate real IMDB ID mapping for MovieLens 100k dataset
This script provides some known IMDB IDs and tools to help find others
"""

import pandas as pd
import json
import requests
import time

# Known IMDB IDs for some popular MovieLens movies
# Format: MovieLens movie_id -> real IMDB ID (without tt prefix)
KNOWN_IMDB_IDS = {
    # Popular movies with known IMDB IDs
    1: "0114709",    # Toy Story (1995) -> tt0114709
    2: "0113189",    # GoldenEye (1995) -> tt0113189

    # Add more as you find them...
}

def load_movielens_data():
    """Load MovieLens movie data from CSV"""
    try:
        movies_df = pd.read_csv('movielens_movies.csv')
        print(f"Loaded {len(movies_df)} movies from movielens_movies.csv")
        return movies_df
    except FileNotFoundError:
        print("Error: movielens_movies.csv not found. Please run generate_imdb_mapping.py first.")
        return None

def search_omdb_api(title, year, api_key=None):
    """
    Search OMDb API for IMDB ID
    You need to get a free API key from http://www.omdbapi.com/
    """
    if not api_key:
        print("Warning: No OMDb API key provided. Cannot search automatically.")
        return None
    
    url = "http://www.omdbapi.com/"
    params = {
        'apikey': api_key,
        't': title,
        'y': year,
        'type': 'movie'
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get('Response') == 'True':
            imdb_id = data.get('imdbID', '').replace('tt', '')
            return imdb_id
        else:
            print(f"Movie not found: {title} ({year})")
            return None
    except Exception as e:
        print(f"Error searching for {title}: {e}")
        return None

def generate_imdb_mapping_with_known_ids(movies_df, output_file='real_imdb_mapping.py'):
    """Generate Python file with real IMDB IDs where known"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""\n')
        f.write('Real IMDB ID Mapping for MovieLens 100k Dataset\n')
        f.write('Format: "imdb_id",  # movie_id. Movie Title (Year)\n')
        f.write('"""\n\n')
        
        f.write('# MovieLens 100k Real IMDB ID Mapping\n')
        f.write('# Known IMDB IDs are included, others need to be looked up\n\n')
        
        f.write('IMDB_LIST = [\n')
        
        for _, movie in movies_df.iterrows():
            movie_id = movie['movie_id']
            title = movie['title']
            year = movie['year']
            
            # Use known IMDB ID if available, otherwise use placeholder
            if movie_id in KNOWN_IMDB_IDS:
                imdb_id = KNOWN_IMDB_IDS[movie_id]
                comment = f"# {movie_id}. {title} ({year}) - VERIFIED"
            else:
                # Generate placeholder ID
                imdb_id = f"{'0' * (7 - len(str(movie_id)))}{movie_id}"
                comment = f"# {movie_id}. {title} ({year}) - PLACEHOLDER - NEEDS REAL IMDB ID"
            
            f.write(f'    "{imdb_id}",  {comment}\n')
        
        f.write(']\n\n')
        
        # Add helper functions
        f.write('def get_verified_count():\n')
        f.write('    """Count how many real IMDB IDs we have"""\n')
        f.write(f'    return {len(KNOWN_IMDB_IDS)}\n\n')
        
        f.write('def get_total_count():\n')
        f.write('    """Get total number of movies"""\n')
        f.write(f'    return {len(movies_df)}\n\n')
        
        f.write('def print_stats():\n')
        f.write('    """Print mapping statistics"""\n')
        f.write('    verified = get_verified_count()\n')
        f.write('    total = get_total_count()\n')
        f.write('    print(f"IMDB Mapping Status:")\n')
        f.write('    print(f"  Verified: {verified}/{total} ({verified/total*100:.1f}%)")\n')
        f.write('    print(f"  Remaining: {total-verified}")\n\n')
        
        f.write('if __name__ == "__main__":\n')
        f.write('    print_stats()\n')
        f.write('    print("\\nFirst 10 entries:")\n')
        f.write('    for i, imdb_id in enumerate(IMDB_LIST[:10]):\n')
        f.write('        print(f"    {imdb_id}")\n')

def create_lookup_helper(movies_df, output_file='imdb_lookup_helper.py'):
    """Create a helper script for manual IMDB ID lookup"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""\n')
        f.write('IMDB ID Lookup Helper\n')
        f.write('Use this script to help find IMDB IDs for MovieLens movies\n')
        f.write('"""\n\n')
        
        f.write('import webbrowser\n')
        f.write('import pandas as pd\n\n')
        
        f.write('def open_imdb_search(title, year):\n')
        f.write('    """Open IMDB search in browser for given movie"""\n')
        f.write('    search_query = f"{title} {year}"\n')
        f.write('    url = f"https://www.imdb.com/find?q={search_query.replace(\' \', \'+\')}&ref_=nv_sr_sm"\n')
        f.write('    print(f"Opening IMDB search for: {title} ({year})")\n')
        f.write('    webbrowser.open(url)\n\n')
        
        f.write('def lookup_batch(start_id=1, count=10):\n')
        f.write('    """Lookup a batch of movies starting from start_id"""\n')
        f.write('    movies_df = pd.read_csv("movielens_movies.csv")\n')
        f.write('    \n')
        f.write('    for i in range(count):\n')
        f.write('        idx = start_id + i - 1\n')
        f.write('        if idx >= len(movies_df):\n')
        f.write('            break\n')
        f.write('            \n')
        f.write('        movie = movies_df.iloc[idx]\n')
        f.write('        print(f"\\n{movie[\'movie_id\']}. {movie[\'title\']} ({movie[\'year\']})")\n')
        f.write('        \n')
        f.write('        choice = input("Press Enter to search, \'s\' to skip, \'q\' to quit: ").strip().lower()\n')
        f.write('        if choice == \'q\':\n')
        f.write('            break\n')
        f.write('        elif choice == \'s\':\n')
        f.write('            continue\n')
        f.write('        else:\n')
        f.write('            open_imdb_search(movie[\'title\'], movie[\'year\'])\n')
        f.write('            imdb_id = input("Enter IMDB ID (without tt prefix, or press Enter to skip): ").strip()\n')
        f.write('            if imdb_id:\n')
        f.write('                print(f"    {movie[\'movie_id\']}: \\"{imdb_id}\\",    # {movie[\'title\']} ({movie[\'year\']})")\n\n')
        
        f.write('if __name__ == "__main__":\n')
        f.write('    print("IMDB ID Lookup Helper")\n')
        f.write('    print("This will help you find IMDB IDs for MovieLens movies")\n')
        f.write('    print("\\nUsage:")\n')
        f.write('    print("  lookup_batch(1, 10)  # Look up movies 1-10")\n')
        f.write('    print("  lookup_batch(50, 5)  # Look up movies 50-54")\n')
        f.write('    print("\\nExample:")\n')
        f.write('    lookup_batch(1, 5)\n')

def update_mapping_with_new_ids(new_ids_dict):
    """Update the known IMDB IDs dictionary"""
    global KNOWN_IMDB_IDS
    KNOWN_IMDB_IDS.update(new_ids_dict)
    print(f"Updated mapping with {len(new_ids_dict)} new IMDB IDs")

def main():
    """Main function"""
    print("Real IMDB ID Mapping Generator")
    print("="*40)
    
    # Load movie data
    movies_df = load_movielens_data()
    if movies_df is None:
        return
    
    # Generate files
    generate_imdb_mapping_with_known_ids(movies_df, 'real_imdb_mapping.py')
    create_lookup_helper(movies_df, 'imdb_lookup_helper.py')
    
    print(f"\n✅ Generated files:")
    print(f"   📄 real_imdb_mapping.py - Mapping with {len(KNOWN_IMDB_IDS)} verified IMDB IDs")
    print(f"   🔍 imdb_lookup_helper.py - Helper script for manual lookup")
    
    print(f"\n📊 Current status:")
    print(f"   Total movies: {len(movies_df)}")
    print(f"   Verified IMDB IDs: {len(KNOWN_IMDB_IDS)}")
    print(f"   Remaining: {len(movies_df) - len(KNOWN_IMDB_IDS)}")
    print(f"   Progress: {len(KNOWN_IMDB_IDS)/len(movies_df)*100:.1f}%")
    
    print(f"\n💡 Next steps:")
    print(f"   1. Run: python imdb_lookup_helper.py")
    print(f"   2. Manually look up IMDB IDs for movies")
    print(f"   3. Add found IDs to KNOWN_IMDB_IDS dictionary")
    print(f"   4. Re-run this script to update the mapping")
    
    print(f"\n🎯 Sample verified entries:")
    for movie_id in list(KNOWN_IMDB_IDS.keys())[:5]:
        movie_info = movies_df[movies_df['movie_id'] == movie_id].iloc[0]
        imdb_id = KNOWN_IMDB_IDS[movie_id]
        print(f'    "{imdb_id}",  # {movie_id}. {movie_info["title"]} ({movie_info["year"]})')

if __name__ == "__main__":
    main()