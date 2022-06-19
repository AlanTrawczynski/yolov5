from utils.plots import plot_results
from pathlib import Path

path = input('Path hacia results.csv: ')
path = Path(path)

if path.suffix != '.csv':
    path = path / 'results.csv'

plot_results(path)