from enum import Enum
from abc import ABC, abstractmethod

class Branch(Enum):
    NOT_TAKEN = 0
    TAKEN = 1


class Strategy(ABC):

    def __init__(self):
        self.prediction = Branch.NOT_TAKEN
    
    @abstractmethod
    def update(self, prediction_correct):
        pass

class AlwaysTaken(Strategy):
    def __init__(self):
        self.prediction = Branch.TAKEN

    def update(self, _):
        pass

class AlwaysNotTaken(Strategy):
    def update(self, _):
        pass


class TwoBit(Strategy):
    def __init__(self):
        super().__init__()
        self.history_bits = (0, 0)

    def update(self, prediction_correct):
        self.update_bits(prediction_correct)

        if self.history_bits[0]:
            self.prediction = Branch.TAKEN
        else:
            self.prediction = Branch.NOT_TAKEN

    def update_bits(self, prediction_correct):
        prediction_value = self.prediction.value
        
        if prediction_correct:
            self.history_bits = (prediction_value, prediction_value)
        else:
            last_bit = self.history_bits[1]
            self.history_bits = (last_bit, int(not prediction_value))

        
class Correlating(Strategy):
    def __init__(self, tablesize, inner_strategy):
        super().__init__()

        predictors = enumerate(inner_strategy() for i in range(tablesize))
        self.table = {i: predictor for (i, predictor) in predictors}

    def prediction(self, shift_register):
        inner_predictor = self.table[shift_register]
        return inner_predictor.prediction

    def update(self, shift_register, prediction_correct):
        inner_predictor = self.table[shift_register]
        inner_predictor.update(prediction_correct)
