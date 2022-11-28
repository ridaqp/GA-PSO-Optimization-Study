
import random
import numpy as np
from optproblems import ce2005


class particle(): 
    def __init__(self, dims, size, lbound,ubound, eps, objfunc, iters ):

        self.position = np.random.uniform(lbound, ubound, [size,dims])   # particle's position
        self.velocity = np.random.uniform(-0.2(ubound - lbound), 0.2(ubound - lbound), [size,dims])   # particle's velocity
        self.informants = [] # particle's neighbours

        # initialise best positions
        self.infbest = self.position # the best position among neighbours/informants
        self.pbest = self.position   # the particle's best
        self.gbest = self.position   # the swarm's best

        # hyperparameters
        self.inertia = 0 # weight for previous velocity
        self.alpha = 0  # acceleration coefficient for personal best
        self.beta = 0   # acc. coeff. for informants best
        self.gamma = 0  # acc. coeff. for global best

        # get particle's current fitness
        self.fitness = self.get_fitness()
        self.objfunc = objfunc

        #step size
        self.step = eps

    def get_fitness(self):
        pass    


    def updatePos(self):
        #self.updateVal()
        self.position += self.step * self.velocity 

        pass

    def updateVel(self):
        pass
        
# default fitness function. 
def sphere(inputs):
    return np.sum(inputs ** 2)
