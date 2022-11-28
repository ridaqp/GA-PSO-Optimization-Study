import particle
import numpy as np
from optproblems import cec2005


class PSO(): 
    #global bestpos; 

    def __init__(self, objective, lbound, ubound, step, dims = 10, size= 10, iters = 300,  w = 0.6, alpha = 2, beta = 2, gamma = 2 ):

        self.swarm = [particle.particle(dims, size, lbound, ubound, step, objective, iters) for i in range(size)] 

        # set upper limits on hyperparams:
        self.inertia = w # weight for previous velocity
        self.alpha = alpha  # acceleration coefficient for personal best
        self.beta = beta  # acc. coeff. for informants best
        self.gamma = gamma  # acc. coeff. for global best

        # set bounds on dimensions for input
        self.lbound, self.ubound = lbound, ubound
        # set bounds on dimensions for velocity
        self.vlbound, self.vubound = -0.2 * (ubound - lbound), 0.2*(ubound - lbound)

        self.gbest = float('inf')
        self.gbest_pos = np.zeros(dims)
        self.iters = iters
        # self.dimensions = dims  # dimensions of the search space
        # self.swarmsize = size #no. of particles in the swarm/population

        # self.swarm = self.setParticles()

        # # set upper limits on different hyperparameters
        # alp = 0 # for personal best
        # c2limit = 0 # for social best
        # c3limit = 0 # for global best

        # maxIters = iters

        # gbest = []  # to keep track of the global best solutions in every iteration
        # fitnessfunc = benchmark
        
        # step = 0.7  # step size for position update

    def evaluate_swarm(self):
        for i in range (self.iters):
            # evaluate each particle
            for particle in self.swarm:
                particle.updateVel(self.inertia, self.alpha, self.beta, self.gamma, self.vlbound, self.vubound, self.gbest_pos )

                self.gbest_pos, self.gbest = particle.updatePos(self.lbound, self.ubound, self.gbest_pos, self.gbest)
        return self.gbest_pos, self.gbest


    # """Evaluate and update particles until convergence"""
    # def optimise(self, benchmark):
        
    #     for i in range (self.maxIters):
    #         self.evaluate_swarm()
    #         self.update_swarm()
            
    #         #if converged:
    #             #break out of loop

#Test: 
benchmark = cec2005.F1(10)
# create pso 
swarm = PSO(benchmark, -100, 100, 1, 10, 10, 10)
best, value = swarm.evaluate_swarm()
print(" the best search position is", best, "whose values is", value)







