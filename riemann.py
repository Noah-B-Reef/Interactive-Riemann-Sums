class Riemann:

   # Constructor
    def __init__(self, func, stepSize, interval, numOfSteps):
        self.func = func
        self.stepSize = stepSize
        self.interval = interval
        self.numOfSteps = numOfSteps

    def eval(self):

       self.validate()
       area = 0
       x = interval[0]

       for step in range(numOfSteps):
           x = x + stepSize
           area += func(x)

       return area

    def draw(self):
        pass

   def validate(self):
       if self.stepSize * self.numOfSteps > abs(self.interval[0]) + abs(self.interval[1]):
           print("Step size and/or number of steps exceeds interval")
           exit()
        # TODO
