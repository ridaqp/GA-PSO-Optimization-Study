
import numpy as np

class Particle():
    def __init__(self, dims, eps, lbound, ubound):

        self.position = np.random.uniform(lbound, ubound, [dims]) # initialise position of particle
        self.pBestPos = self.position # personal best position ofa particle
        self.pBest = float('inf') # initialise to positive infinity
        self.step = eps  # step size during postion update
        self.dims = dims # dimensions of the search space
        self.velocity = np.random.uniform(-0.2*(ubound - lbound), 0.2*(ubound - lbound), [dims]) # initialise velocity of the particle within bounds
        self.lbound = lbound 
        self.ubound = ubound

    def updatePos(self):
        self.position = self.position + self.step * self.velocity #update position of the particle

        # truncate values out of the input boundaries of the objective function
        for i in range(self.dims):
            if self.position[i] > self.ubound:
                self.position[i] = self.ubound
            if self.position[i]< self.lbound:
                self.position[i] = self.lbound

    def updateVel(self, velocity):
        self.velocity = velocity # update the velocity of the particle
        # set boundaries for the velocity - we choose it to be 20% of the difference between the input bounds 
        ubound = 0.2*(self.ubound - self.lbound)
        lbound = -0.2*(self.ubound - self.lbound)

        #truncate values out of the of bound
        for i in range(self.dims):
            if self.velocity[i] > ubound:
                self.velocity[i] = ubound
            if self.velocity[i]< lbound:
                self.velocity[i] = lbound

