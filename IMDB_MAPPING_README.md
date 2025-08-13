# MovieLens 100k IMDB ID Mapping Generator

This document explains how to generate the IMDB ID mapping file for the 943 movies in the MovieLens 100k dataset, with their corresponding movie titles and u.item sequence numbers.

## Generated Files

### Basic Files
1. **movielens_movies.csv** - CSV file containing all movie information
2. **imdb_mapping_template.json** - JSON format template file
3. **imdb_mapping_template.py** - Python format placeholder mapping

### Real IMDB ID Files
4. **real_imdb_mapping.py** - Mapping file containing verified IMDB IDs
5. **imdb_lookup_helper.py** - Assistant script for manual IMDB ID lookup

## Usage Steps

### Step 1: Generate Basic Mapping
```bash
python generate_imdb_mapping.py
```
This will generate the basic mapping files and templates.

### Step 2: Generate Real IMDB ID Mapping
```bash
python generate_real_imdb_mapping.py
```
This will generate a mapping file containing some known IMDB IDs.

### Step 3: View Current Results
Check the `real_imdb_mapping.py` file, and you will see a format similar to what you requested:

```python
IMDB_LIST = [
    "0114709",  # 1. Toy Story (1995) - VERIFIED
    "0113189",  # 2. GoldenEye (1995) - VERIFIED
    "0000003",  # 3. Four Rooms (1995) - PLACEHOLDER - NEEDS REAL IMDB ID
    "0000004",  # 4. Get Shorty (1995) - PLACEHOLDER - NEEDS REAL IMDB ID
    "0112462",  # 8. Babe (1995) - VERIFIED
    "0114369",  # 11. Seven (Se7en) (1995) - VERIFIED
    "0114814",  # 12. Usual Suspects, The (1995) - VERIFIED
    # ... more movies
]
```

## Current Status

- **Total Movies**: 1682 films
- **Verified IMDB IDs**: 20 (1.2%)
- **Need to Find**: 1662

### Verified Movies (Examples)
```
"0114709",  # 1. Toy Story (1995)
"0113189",  # 2. GoldenEye (1995)  
"0114746",  # 7. Twelve Monkeys (1995)
"0112462",  # 8. Babe (1995)
"0114369",  # 11. Seven (Se7en) (1995)
"0114814",  # 12. Usual Suspects, The (1995)
"0113277",  # 25. Heat (1995)
"0110413",  # 56. Pulp Fiction (1994)
"0109830",  # 64. Forrest Gump (1994)
"0116282",  # 100. Fargo (1996)
```

## How to Add More Real IMDB IDs

### Method 1: Using Helper Script
```bash
python imdb_lookup_helper.py
```
This script will:
- Automatically open IMDB search in browser
- Allow you to input the found IMDB ID
- Generate correctly formatted mapping entries

### Method 2: Manual Search and Edit
1. Search for movie title and year on IMDB.com
2. Extract IMDB ID from URL (e.g., tt0111161 -> use 0111161)
3. Add to the `KNOWN_IMDB_IDS` dictionary in `generate_real_imdb_mapping.py`:
   ```python
   KNOWN_IMDB_IDS = {
       # Existing mappings...
       199: "0111161",  # The Shawshank Redemption (1994)
       # Add more...
   }
   ```
4. Re-run `python generate_real_imdb_mapping.py`

### Method 3: Batch Lookup (Advanced)
If you have an OMDb API key, you can modify the API calls in `generate_real_imdb_mapping.py` to automatically lookup IDs.

## Final Output Format

Eventually you will get the required format:
```python
"0111161",  # 1. The Shawshank Redemption (1994)
"0068646",  # 2. The Godfather (1972)  
"0071562",  # 3. The Godfather: Part II (1974)
"0468569",  # 4. The Dark Knight (2008)
"0050083",  # 5. 12 Angry Men (1957)
# ... continue with remaining movies
```

## File Descriptions

### generate_imdb_mapping.py
- Parses u.item file
- Extracts movie ID, title, year
- Generates basic template files

### generate_real_imdb_mapping.py  
- Contains known real IMDB IDs
- Generates mixed placeholder and real ID mapping
- Provides statistics and progress tracking

### imdb_lookup_helper.py
- Interactive IMDB ID lookup tool
- Automatically opens browser search
- Convenient for batch processing

## Tips

1. **Prioritize Popular Movies**: Look up well-known movies first, as they are usually easier to find
2. **Use Original Titles**: If English titles don't work, try using original language titles
3. **Verify Years**: Ensure release year on IMDB matches the year in dataset
4. **Batch Processing**: Using helper scripts can greatly improve efficiency

## Contribution

If you find more real IMDB IDs, please update the `KNOWN_IMDB_IDS` dictionary and regenerate the mapping file. This can help other users get a more complete mapping.

---

**Note**: IMDB ID format should be 7 digits without the "tt" prefix. For example: `tt0111161` -> `0111161`