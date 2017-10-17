from predictors import *

def createStep(address, taken_bit):
    if (taken_bit == '1'):
        return Step(address, Branch.TAKEN)
    else:
        return Step(address, Branch.NOT_TAKEN)

def parseTrace(file):
    lines = file.read().splitlines()
    steps = [line.split(" ") for line in lines]
        
    execution = [createStep(step[0], step[1]) for step in steps]
    return execution

def get_unique_branches(trace):
    unique_branches = set([step.address for step in trace])
    return len(unique_branches)

def get_percentage_taken(trace):
    taken = 0
    
    for step in trace:
        if step.branch == Branch.TAKEN:
            taken += 1
            
    return taken / len(trace) * 100

def benchmark_properties(name, trace):
    unique_branches = get_unique_branches(trace)
    percentage_taken = get_percentage_taken(trace)
    total_length = len(trace)
    
    return str(name +  "\nTotal length: " + str(total_length) + "\nUnique branches: " + str(unique_branches) + 
                "\nPercentage taken: " + str(percentage_taken))


trace_echo = parseTrace(open("traces/Echo.out", "r"))
trace_fft = parseTrace(open("traces/FFT8192.out", "r"))
trace_sor = parseTrace(open("traces/SOR200.out", "r"))
trace_mc = parseTrace(open("traces/MonteCarlo20000.out", "r"))
trace_loop = parseTrace(open("traces/Loop5000.out", "r"))
trace_cond = parseTrace(open("traces/LoopCondition.out", "r"))
trace_sort = parseTrace(open("traces/BubbleSort500.out", "r"))
