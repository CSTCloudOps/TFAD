import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from pandas.io.formats import style


def A1Benchmark_plot():
    csv_paths = [i for i in os.listdir("./A1Benchmark") if i.endswith(".csv")]

    for csv_path in csv_paths:
        df = pd.read_csv(os.path.join("./A1Benchmark", csv_path), index_col='timestamp')
        os.makedirs("plot/A1Benchmark/", exist_ok=True)
        save_path = os.path.join("plot/A1Benchmark/", csv_path.replace(".csv", ".png"))
        
        anomaly_pos = df['is_anomaly'] == 1

        df['is_anomaly'] = None
        df.loc[anomaly_pos, 'is_anomaly'] = df[anomaly_pos]['value']

        fig = df.plot(figsize=(20, 10), style=['b', 'ro']).get_figure()
        fig.savefig(save_path)
        plt.close(fig)


def A2Benchmark_plot():
    csv_paths = [i for i in os.listdir("./A2Benchmark") if i.endswith(".csv")]

    for csv_path in csv_paths:
        df = pd.read_csv(os.path.join("./A2Benchmark", csv_path), index_col='timestamp')
        os.makedirs("plot/A2Benchmark/", exist_ok=True)
        save_path = os.path.join("plot/A2Benchmark/", csv_path.replace(".csv", ".png"))
        
        anomaly_pos = df['is_anomaly'] == 1

        df['is_anomaly'] = None
        df.loc[anomaly_pos, 'is_anomaly'] = df[anomaly_pos]['value']

        fig = df.plot(figsize=(20, 10), style=['b', 'ro']).get_figure()
        fig.savefig(save_path)
        plt.close(fig)

if __name__ == '__main__':
    A1Benchmark_plot()
    A2Benchmark_plot()
