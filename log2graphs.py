from parse_logs import parse_log_files
from make_graphs import plot_training_errors

def log2graphs(log_file, tr_label, te_label, max_epoch=None, show=True, save=True):
    data = parse_log_files(log_file)
    plot_training_errors(data, tr_label, te_label, max_epoch=max_epoch, show=show, save=save)

if __name__ == "__main__":
    log2graphs("/Users/bd20841/code/IMP2_make_graphs/logs/1000_dt5ab_iter_log_2.txt", tr_label="DT5AB_1000", te_label="DT3", max_epoch=250)
