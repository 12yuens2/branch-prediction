from enum import Enum
from abc import ABC, abstractmethod

class Branch(Enum):
    NOT_TAKEN = 0
    TAKEN = 1

class Step:
    def __init__(self, address, branch):
        self.address = address
        self.branch = branch

class Predictor(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def predict_correct(self, step):
        pass
    
    def translate_address(self, address, table_bits):
        mask = 2 ** table_bits - 1
        return int(address) & mask
    
    def simulate(self, execution):
        correct_prediction_count = 0

        for step in execution:
            if self.predict_correct(step):
                correct_prediction_count += 1

        return correct_prediction_count / len(execution) * 100




## Predictor implementations ##

class AlwaysTakenPredictor(Predictor):
    def __init__(self):
        self.prediction = Branch.TAKEN
        
    def predict_correct(self, step):
        return self.prediction == step.branch

class AlwaysNotTakenPredictor(Predictor):
    def __init__(self):
        self.prediction = Branch.NOT_TAKEN
        
    def predict_correct(self, step):
        return self.prediction == step.branch

class TwoBitCounter():
    def __init__(self):
        self.prediction = Branch.NOT_TAKEN
        self.history_bits = (0, 0)
        
    def update(self, prediction_correct):
        self.update_bits(prediction_correct)
        
        if self.history_bits[0]:
            self.prediction = Branch.TAKEN
        else:
            self.prediction = Branch.NOT_TAKEN
            
    def update_bits(self, prediction_correct):
        prediction_value = self.prediction.value
        
        if (prediction_correct):
            self.history_bits = (prediction_value, prediction_value)
        else:
            last_bit = self.history_bits[1]
            self.history_bits = (last_bit, int(not prediction_value))

class TwoBitPredictor(Predictor):
    def __init__(self, table_bits):
        # Create a TwoBitCounter for each entry in the table
        counters = enumerate([TwoBitCounter() for i in range(2 ** table_bits)])
        self.table = {address: counter for (address, counter) in counters}
        self.table_bits = table_bits
        
    def predict_correct(self, step):
        address = self.translate_address(step.address, self.table_bits)
        counter = self.table[address]
        prediction = counter.prediction
        
        prediction_correct = prediction == step.branch
        counter.update(prediction_correct)
        
        return prediction_correct

class CorrelatingCounter():
    def __init__(self, register_bits):
        self.two_bit_counters = [TwoBitCounter() for i in range(2 ** register_bits)]

    def prediction(self, shift_register):
        counter = self.two_bit_counters[shift_register]
        return counter.prediction
    
    def update(self, prediction_correct, shift_register):
        counter = self.two_bit_counters[shift_register]
        counter.update(prediction_correct)

class CorrelatingPredictor(Predictor):
    def __init__(self, table_bits, register_bits):
        
        # Create a CorrelatingCounter for each entry in the table
        inner_predictors = enumerate([CorrelatingCounter(register_bits) for i in range(2 ** table_bits)])
        self.table = {address: ip for (address, ip) in inner_predictors}
        self.table_bits = table_bits
        
        # Initialise shift register
        self.shift_register = 0b0
        self.register_bits = register_bits
    
    def predict_correct(self, step):
        address = self.translate_address(step.address, self.table_bits)
        inner_predictor = self.table[address]
        prediction = inner_predictor.prediction(self.shift_register)
        
        prediction_correct = prediction == step.branch
        inner_predictor.update(prediction_correct, self.shift_register)
        
        self.update_register(step.branch == Branch.TAKEN)
        
        return prediction_correct
        
    def update_register(self, branch_taken):
        self.shift_register = self.shift_register >> 1
        
        if (branch_taken):
            self.shift_register |= 1 << (self.register_bits - 1)

class GsharePredictor(Predictor):
    def __init__(self, table_bits, register_bits):
        
        # Create a TwoBitCounter for each entry in the table
        counters = enumerate([TwoBitCounter() for i in range(2 ** table_bits)])
        self.table = {address: counter for (address, counter) in counters}
        print(len(self.table))
        self.table_bits = table_bits
        
        # Initialise shift register
        self.shift_register = 0b0
        self.register_bits = register_bits
        
    def predict_correct(self, step):
        address = self.translate_address(step.address, self.table_bits)
        counter = self.get_inner_predictor(address)
        prediction = counter.prediction
        
        prediction_correct = prediction == step.branch
        counter.update(prediction_correct)
        
        self.update_register(step.branch == Branch.TAKEN)
        
        return prediction_correct
    
    def get_inner_predictor(self, address):
        index = address ^ self.shift_register
        return self.table[index]
        
    def update_register(self, branch_taken):
        self.shift_register = self.shift_register >> 1

        if (branch_taken):
            self.shift_register |= 1 << (self.register_bits - 1)
