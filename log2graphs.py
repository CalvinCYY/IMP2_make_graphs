from parse_logs import parse_log_files, parse_batch_log_files
from make_graphs import plot_training_errors, plot_comparison_errors

def log2graphs(log_file, tr_label, te_label, max_epoch=None, show=True, save=True):
    data = parse_log_files(log_file)
    plot_training_errors(data, tr_label, te_label, max_epoch=max_epoch, show=show, save=save)

def compare_log2graphs(log_files_path, graph_label, te_label, max_epoch=100, show=True, save=True, log_y=True, log_x=False):
    data_tag, data_list = parse_batch_log_files(log_files_path)
    plot_comparison_errors(data_tag, data_list, graph_label, te_label, max_epoch=max_epoch, show=show, save=save, log_y=log_y, log_x=log_x)


if __name__ == "__main__":
    #log2graphs("/Users/bd20841/code/IMP2_make_graphs/logs/new_logs/300_dt5ab_F_ga2_iter_log.txt", tr_label="DT5AB_F_ga2", te_label="DT4_F_containing")
    compare_log2graphs("/Users/bd20841/code/IMP2_make_graphs/logs/ga_logs", graph_label='DT5AB_gradient_accumulation', te_label='DT3', log_y=True, log_x=False)
