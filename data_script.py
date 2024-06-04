import os
import datetime
from utils import read_log_file, process_logs, get_top_50_songs_by_country, write_top_50_file

def main():
    today = datetime.date.today()
    logs_directory = 'logs'
    output_directory = 'output'

    # Créer le répertoire de sortie s'il n'existe pas
    os.makedirs(output_directory, exist_ok=True)

    # Lire les fichiers de logs des 7 derniers jours
    logs = []
    for i in range(7):
        date = today - datetime.timedelta(days=i)
        log_filename = os.path.join(logs_directory, f'listen-{date.strftime("%Y%m%d")}.log')
        if os.path.exists(log_filename):
            logs.extend(read_log_file(log_filename))

    # Traiter les logs pour obtenir les comptes de streams
    song_counts = process_logs(logs)

    # Obtenir les top 50 chansons par pays
    top_50_songs_by_country = get_top_50_songs_by_country(song_counts)

    # Écrire les résultats dans le fichier de sortie
    output_filename = os.path.join(output_directory, f'country_top50_{today.strftime("%Y%m%d")}.txt')
    write_top_50_file(output_filename, top_50_songs_by_country)

if __name__ == "__main__":
    main()
