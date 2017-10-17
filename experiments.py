from matplotlib import pyplot as plt
from predictors import *
from benchmarks import *

class PlotData():
    def __init__(self, trace, label, marker):
        self.trace = trace
        self.data = []
        self.label = label
        self.marker = marker

def new_benchmark_experiment():
    return {
        "Echo": PlotData(trace_echo, "Echo", "x"),
        "FFT": PlotData(trace_fft, "FFT", "o"),
        "SOR": PlotData(trace_sor, "SOR", "s"),
        "MC": PlotData(trace_mc, "MonteCarlo", "^"),
        "Loop": PlotData(trace_loop, "Loop", "p"),
        "Conditional": PlotData(trace_cond, "LoopCondition", "."),
        "BubbleSort": PlotData(trace_sort, "Bubble Sort", "*")
    }



def plot_graph(title, data, ylabel="Prediction rate", xlabel="Predictor table size", xticks=[8, 512, 1024, 2048, 4096]):
    fig = plt.figure(figsize=(14,9))
    
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(xticks) 

    for d in data:
        plt.scatter(*zip(*d.data), marker=None)
        plt.plot(*zip(*d.data), label=d.label, marker=d.marker)
    plt.legend(loc="lower right")
    plt.ylim(top=100)
    plt.grid()
    return plt.axes()
