import os
import datetime
import utils
def main():
    today = datetime.date.today()
    logs_directory = 'logs'
    output_directory = 'output'
    # If no repertory then we create one
    os.makedirs(output_directory, exist_ok=True)
    # Read logs
    logs = []
    log_filename = os.path.join(logs_directory, 'listen-2021-12-01.log')
    # Debugging file path
    #log_filename = os.path.abspath(os.path.join(logs_directory, 'listen-2021-12-01.log'))
    print(f"Constructed file path: {log_filename}")
    if os.path.exists(log_filename):
        print("File exists")
        logs.extend(utils.read_log_file(log_filename))
        print(f"Logs read: {len(logs)} lines")
    else:
        print("File does not exist")
    # Process logs to estimate streams
    utils.making_dataframe(logs)
if __name__ == "__main__":
    main()
