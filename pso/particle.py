
import random
import numpy as np
from optproblems import ce2005
from PSO import bestpos

class particle(): 
    
    def __init__(self, dims, size, lbound,ubound, eps, objfunc, iters ):

        self.position = np.random.uniform(lbound, ubound, [size,dims])   # particle's position
        self.velocity = np.random.uniform(-0.2(ubound - lbound), 0.2(ubound - lbound), [size,dims])   # particle's velocity
        self.informants = [] # particle's neighbours

        # initialise best positions
        self.infbest = self.position # the best position among neighbours/informants
        self.pbest = self.position   # the particle's best
        self.gbest = self.position   # the swarm's best

        
        # get particle's current fitness
        self.fitness = self.get_fitness()
        self.objfunc = objfunc

        #step size
        self.step = eps

        # ?? necessary for velocity update
        self.dims = dims

        

    def get_fitness(self, position):
          return self.objfunc(position)


    def updatePos(self, lbound, ubound):

        #update position
        pos += self.step * self.velocity 
        #check and fix bound violations
        for i in range (self.dims):
            if pos[i] > ubound:
                pos[i] = ubound
            if pos[i]< lbound:
                pos[i] = lbound
        self.position = pos

        # update best costs
        current = self.get_fitness(self.position)
        if current < self.get_fitness(self.pbest):
            self.pbest = self.position

            #add informants best 

            # check global best
            if current < self.get_fitness(bestpos):
                #update global best
                bestpos = self.position

        
    
    """Update Velocity"""
    def updateVel(self, inertia, alpha, beta, gamma, lbound, ubound):
        # add decaying weight here
        velocity = inertia * self.velocity + alpha*np.random.rand(self.dims)*(self.pbest - self.position) + beta*np.random.rand(self.dims)*(self.gbest - self.position)+ gamma*np.random.rand(self.dims)*(self.infbest - self.position)
        # check if velocity out of bounds: 
        for i in range (self.dims):
            if velocity[i] > ubound:
                velocity[i] = ubound
            if velocity[i]< lbound:
                velocity[i] = lbound
        self.velocity = velocity
      
        
# default fitness function. 
def sphere(inputs):
    return np.sum(inputs ** 2)
