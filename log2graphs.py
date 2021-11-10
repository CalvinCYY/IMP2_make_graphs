from parse_logs import parse_log_files
from make_graphs import plot_training_errors

def log2graphs(log_file):
    data = parse_log_files(log_file)
    plot_training_errors(data)

if __name__ == "__main__":
    log2graphs("path/to/log.txt")
