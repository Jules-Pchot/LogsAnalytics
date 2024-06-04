from collections import defaultdict, Counter

def read_log_file(filepath):
    logs = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 3:
                sng_id, user_id, country = parts
                logs.append((sng_id, user_id, country))
    return logs

def process_logs(logs):
    song_counts = defaultdict(Counter)
    for sng_id, user_id, country in logs:
        song_counts[country][sng_id] += 1
    return song_counts

def get_top_50_songs_by_country(song_counts):
    top_50_songs_by_country = {}
    for country, counts in song_counts.items():
        top_50_songs = counts.most_common(50)
        top_50_songs_by_country[country] = top_50_songs
    return top_50_songs_by_country

def write_top_50_file(filepath, top_50_songs_by_country):
    with open(filepath, 'w') as file:
        for country, top_50_songs in top_50_songs_by_country.items():
            line = f"{country}|"
            line += ",".join([f"{sng_id}:{count}" for sng_id, count in top_50_songs])
            file.write(line + "\n")
