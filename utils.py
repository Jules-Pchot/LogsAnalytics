from collections import defaultdict, Counter
import pandas as pd
import numpy as np

# Fonction pour lire le fichier de logs
def read_log_file(filepath):
    logs = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = [part.strip() for part in line.strip().split('|')]
            if len(parts) == 3:
                sng_id, user_id, country = parts
                logs.append((sng_id, user_id, country))
    return logs

def data_wrangling(df):
    clean_df = df[df['country'].str.len() == 2]
    return clean_df
def making_dataframe(logs):
    # Create DataFrame directly from the list of tuples
    df = pd.DataFrame(logs, columns=['sng_id','user_id', 'country'])
    noUser_df = df.drop(['user_id'],axis=1)
    clean_df = data_wrangling(noUser_df)
    # Group by country and aggregate songs into lists
    songs_by_country = clean_df.groupby("country")["sng_id"].apply(list).reset_index()
    '''use to Debug dataframe'
    print("Original DataFrame:")
    print(df)
    print("clean_df:")
    print(clean_df)
    print("\nSongs by Country DataFrame:")
    print(songs_by_country)
    '''
    return songs_by_country

# Fonction pour obtenir les 50 morceaux les plus populaires par pays
def get_top_50_songs_by_country(song_counts_by_country):


# Fonction pour écrire les résultats dans un fichier
def write_top_50_file(filepath, top_50_songs_by_country):
    with open(filepath, 'w') as file:
        for country, top_50_songs in top_50_songs_by_country.items():
            line = f"{country}|"
            line += ",".join([f"{sng_id}:{count}" for sng_id, count in top_50_songs])
            file.write(line + "\n")
