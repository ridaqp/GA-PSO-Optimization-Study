import particle

class PSO(): 

    def __init__(self, benchmark):

        dimensions = 0  # dimensions of the search space
      
        # set upper limits on different hyperparameters
        c1limit = 0 # for personal best
        c2limit = 0 # for social best
        c3limit = 0 # for global best

        maxIters = 0
        
        gbest = []  # to keep track of the global best solutions in every iteration
        fitnessfunc = benchmark
        swarm = []
        step = 0.1  # step size for position update

    def evaluate_swarm(self):
        pass

    def update_swarm(self): 
        pass 

    """Evaluate and update particles until convergence"""
    def optimise(self, benchmark):
        
        for i in range (self.maxIters):
            self.evaluate_swarm()
            self.update_swarm()
            
            #if converged:
                #break out of loop







