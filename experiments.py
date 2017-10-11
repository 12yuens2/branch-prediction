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

