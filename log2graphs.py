from parse_logs import parse_log_files
from make_graphs import plot_training_errors

def log2graphs(log_file, tr_label, te_label):
    data = parse_log_files(log_file)
    plot_training_errors(data, tr_label, te_label)

if __name__ == "__main__":
    log2graphs("/Users/bd20841/code/IMP2_make_graphs/logs/1000_dt5ab_iter_log.txt", tr_label="DT5AB_1000", te_label="DT3")
