import sys
import os
from pathlib import Path
sys.path.append(os.path.realpath(os.path.dirname(__file__))+'/../')

import matplotlib.pyplot as plt

def plot_training_errors(data, save=True):
    for key, values in data.items():
        epochs = []
        errors = []
        for i, error in enumerate(values):
            epochs.append(i)
            errors.append(error)

        plt.plot(epochs, errors, label=key)
        plt.title(f'Training errors for {key}')
        plt.xlabel('Epochs')
        plt.ylabel('Loss (MAE)')
        plt.legend()
        plt.show()
        if save:
            plt.savefig(f'graphs/{key}_training_error.png')
