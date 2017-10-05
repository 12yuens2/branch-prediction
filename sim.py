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

    def update(self, prediction_correct):
        self.prediction = Branch.TAKEN
    
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



s = AlwaysTaken()
p = Predictor(s)

e = [Step(i, Branch.NOT_TAKEN) for i in range(10)]

simulate(p, e)
