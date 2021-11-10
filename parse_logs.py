import os
from collections import defaultdict
import matplotlib.pyplot as plt

def parse_log_files(log_file):

    with open(log_file, 'r') as f:
        nmr_params = []

        header_line = f.readline()
        h_block = header_line.split('|')
        header = h_block[1:]
        for i in range(len(header)-1):
                    nmr_params.append(header[i].split()[1])

        values = defaultdict(list)

        for idx, line in enumerate(f):
            for i in range(len(nmr_params)):
                main_block = line.split('|')
                val_block = main_block[1:]
                values[nmr_params[i]].append(float(val_block[i].split()[1]))
    return values
