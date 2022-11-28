import particle

class PSO(): 

    def __init__(self, benchmark, dims, size, iters = 100):

        dimensions = dims  # dimensions of the search space
        swarmsize = size
        swarm = self.setParticles()

        # set upper limits on different hyperparameters
        c1limit = 0 # for personal best
        c2limit = 0 # for social best
        c3limit = 0 # for global best

        maxIters = iters

        gbest = []  # to keep track of the global best solutions in every iteration
        fitnessfunc = benchmark
        
        step = 0.1  # step size for position update

    def setParticles(self):
        swarm = []
        for i in range (self.swarmsize):
            swarm.append(particle.particle(self.dimensions))

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







