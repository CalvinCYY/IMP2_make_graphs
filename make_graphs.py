import sys
import os
from pathlib import Path
sys.path.append(os.path.realpath(os.path.dirname(__file__))+'/../')

import matplotlib.pyplot as plt

def plot_training_errors(data, tr_label='training_set', te_label='test_set', max_epoch=None, show=True, save=True):
    for key, values in data.items():
        epochs = []
        errors = []
        for i, error in enumerate(values):
            epochs.append(i)
            errors.append(error)
            if i == max_epoch:
                break

        plt.plot(epochs, errors, label=key)
        plt.title(f'{tr_label} errors for {key} prediction against {te_label}')
        plt.xlabel('Epochs')
        plt.ylabel('Loss (MAE)')
        plt.legend()
        fig = plt.gcf()
        if show:
            plt.show()
        if save:
            if not os.path.exists(f'graphs/{tr_label}'):
                os.makedirs(f'graphs/{tr_label}')
            fig.savefig(f'graphs/{tr_label}/{tr_label}_{key}_training_error.png', format='png')
