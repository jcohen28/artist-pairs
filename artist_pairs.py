# The follow code completes in under a second on my laptop
# As a result, I decided that it wasn't necessary to optimize further nor were tradeoffs in precision required
# Please let me know if there are system constraints that I should consider when optimizing
import time

artist_rows = {}
# 1. Create dictionary of artists to the set of all rows in which they appear
# Performance: O(m)
with open('Artist_lists_small.txt', 'r') as fp:
    for line_num, line in enumerate(fp):
        artists = line.split(',')
        for artist in artists:            
            row_set = artist_rows.get(artist, set())
            row_set.add(line_num)
            artist_rows[artist] = row_set

# print('{} distinct artists'.format(len(artist_rows.keys())))
# The given file as 11,846 distinct artists


# 2. Filter all artists that show up fewer than 50 times
# Performance: O(m)
artist_rows = {artist:rows for artist, rows in artist_rows.items() if len(rows) >= 50}

# print('{} distinct artists that recur 50+ times'.format(len(artist_rows.keys())))
# The given file has 120 distinct artists that recur at least 50 times


# 3. For each artist compare row overlap with all other artists.
# Ignore artists that have already been the "current artist" to avoid duplicates
# Performance: O(m^2)
with open('output_artist_pairs_{}.txt'.format(time.time()), 'w') as f:
    visited_artists = set()    
    for current_artist, current_rows in artist_rows.items():
        visited_artists.add(current_artist)
        for compare_artist, compare_rows in artist_rows.items():
            if compare_artist not in visited_artists:
                overlap_count = len([row for row in compare_rows if row in current_rows])                
                if overlap_count >= 50:                    
                    f.write('{},{}\n'.format(current_artist, compare_artist))

# The given file has 93 pairs that overlap 50+ times

