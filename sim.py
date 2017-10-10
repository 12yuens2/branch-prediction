from strategies import *


strategy_module = __import__("strategies")

class Step:
    def __init__(self, address, branch):
        self.address = address
        self.branch = branch

class Predictor:
    def __init__(self, strategy, execution, tablesize):
        self.strategy = getattr(strategy_module, strategy)
        self.execution = execution

        predictors = enumerate([self.strategy() for i in range(tablesize)])
        self.table = {address: predictor for (address, predictor) in predictors}
        
    def predict(self, step):
        predictor = self.table[step.address]
        prediction = predictor.prediction
        
        prediction_correct = step.branch == prediction
        predictor.update(prediction_correct)
        
        return prediction_correct
    
    def simulate(self):
        correct_prediction_count = 0
        
        for step in self.execution:
            if self.predict(step):
                correct_prediction_count += 1
            
        return correct_prediction_count / len(self.execution) * 100


class Correlating(Predictor):
    def __init__(self, strategy, execution, tablesize):
        super().__init__()

        predictors = enumerate(predictor() for i in range(m))
        self.table = {i: predictor for (i, predictor) in predictors}

        self.shift_register = 0

    def predict(self, step):
        predictor = self.table[step.address]
        prediction = predictor.prediction(self.shift_register)

        prediction_correct = step.branch == prediction
        predictor.update(prediction_correct):w

        return prediction_correct

    def simulate(self):
        return super().simulate()

e = [Step(i, Branch.TAKEN) for i in range(10)]
e.extend([Step(i, Branch.NOT_TAKEN) for i in range(10)])

e = [Step(0, Branch.TAKEN), Step(0, Branch.NOT_TAKEN), Step(0, Branch.TAKEN), Step(0, Branch.TAKEN), Step(0, Branch.NOT_TAKEN)]

class1 = getattr(strategy_module, "AlwaysTaken")
instance = class1()

for step in e:
    print(step.branch)

p = Predictor("AlwaysNotTaken", e, 8)
print(p.simulate())

p = Predictor("AlwaysTaken", e, 8)
print(p.simulate())

p = Predictor("TwoBit", e, 8)
print(p.simulate())
