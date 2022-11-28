import particle
import numpy as np



self, dims, size, lbound,ubound, eps, objfunc = sphere
class PSO(): 
    global bestpos ; 
    bestpos = np.zeros(dims)

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
        self.vlbound, self.vuboundvMin = -0.2 * (ubound - lbound), 0.2*(ubound - lbound)


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

    def setParticles(self):
        swarm = []
        for i in range (self.swarmsize):
            particle.particle(self.dims, self.swarmsize, self.xMin, self.xMax, self.step)
            swarm.append(particle.particle(self.dimensions))

    def evaluate_swarm(self):
        for i in range (self.iters):
            # evaluate each particle
            for particle in self.swarm:
                particle.updateVel(self.inertia, self.alpha, self.beta, self.gamma, self.vlbound, self.vubound)

                particle.updatePos(self.lbound, self.ubound)
        return bestpos, self.swarm[0].get_fitness(bestpos)


    """Evaluate and update particles until convergence"""
    def optimise(self, benchmark):
        
        for i in range (self.maxIters):
            self.evaluate_swarm()
            self.update_swarm()
            
            #if converged:
                #break out of loop







