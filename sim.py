from enum import Enum
from abc import ABC, abstractmethod

class Branch(Enum):
    NOT_TAKEN = 0
    TAKEN = 1



class Step:

    def __init__(self, address, branch):
        self.address = address
        self.branch = branch

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


class TwoBitPredictor(Strategy):
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

class Predictor:

    def __init__(self, strategy):
        self.strategy = strategy

    def predict(self, step):
        prediction = self.strategy.prediction

        prediction_correct = step.branch == prediction
        self.strategy.update(prediction_correct)

        return prediction_correct

    
def simulate(predictor, execution):
    
    correct_prediction_count = 0
    for step in execution:
        if predictor.predict(step):
            correct_prediction_count += 1

    print(len(execution))
    print(correct_prediction_count)



sa = AlwaysTaken()
pa = Predictor(sa)

sn = AlwaysNotTaken()
pn = Predictor(sn)

s2b = TwoBitPredictor()
p2b = Predictor(s2b)

e = [Step(i, Branch.TAKEN) for i in range(10)]
e.extend([Step(i, Branch.NOT_TAKEN) for i in range(10)])

e = [Step(0, Branch.TAKEN), Step(0, Branch.NOT_TAKEN), Step(0, Branch.TAKEN), Step(0, Branch.TAKEN), Step(0, Branch.NOT_TAKEN)]


simulate(pa, e)
print("====================")
simulate(pn, e)
print("====================")
simulate(p2b, e)
