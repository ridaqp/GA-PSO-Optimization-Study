
import random
import numpy as np
from optproblems import cec2005

class Particle():
    def __init__(self, dims, eps, iters):
        #informants
        self.position = np.random.uniform(-100, 100, [dims])
        self.pBest_position = self.position
        self.pBest_value = float('inf') #this
        self.step = eps
        self.dims = dims
        self.velocity = np.random.uniform(-0.2*(100 - (-100)), 0.2*(100 - (-100)), [dims])

    def update(self, ubound, lbound):
        self.position = self.position + self.velocity
        for i in range(2):
            if self.position[i] > ubound:
                print("here", self.position[i])
                self.position[i] = ubound
                print("then", self.position[i])
            if self.position[i]< lbound:
                print("here", self.position[i])
                self.position[i] = lbound
                print("then", self.position[i])

# class particle(): 
    

#     def __init__(self, dims, size, lbound,ubound, eps, objfunc, iters ):

#         self.position = np.random.uniform(lbound, ubound, [dims])   # particle's position
#         self.velocity = np.random.uniform(-0.2*(ubound - lbound), 0.2*(ubound - lbound), [dims])   # particle's velocity


#         self.informants = [] # particle's neighbours

#         # initialise best positions
#         #self.infbest =  np.copy(self.position) # the best position among neighbours/informants
#         self.pbest =  self.position   # the particle's best

#         self.objfunc = objfunc
#         # get particle's current fitness
#         #self.fitness = self.get_fitness(self.position)
        

#         #step size
#         self.step = eps

#         # ?? necessary for velocity update
#         self.dims = dims


#     def get_fitness(self, position):
#         return self.objfunc(position)

#     def updatePos(self, lbound, ubound, best_pos, best):
        
       
#         #update position
#         self.position += self.step * self.velocity 
        

#         #check and fix bound violations
#         for i in range (self.dims):
#             if self.position[i] > ubound:
#                 print("here", self.position[i])
#                 self.position[i] = ubound
#                 print("then", self.position[i])
#             if self.position[i]< lbound:
#                 print("here", self.position[i])
#                 self.position[i] = lbound
#                 print("then", self.position[i])
        

#         # get new personal cost
#         current = self.get_fitness(self.position)
#         # if new cost is lower than personal best
#         #print("cost: current, personal, global", current, self.get_fitness(self.pbest), best)
#         #print("pos: current, personal, global", self.position, self.pbest, best_pos)

#         if current < self.get_fitness(self.pbest):
#             #set personal best as current position
#             self.pbest = np.copy(self.position)

#             #check informants best 

#             # if new personal cost is less than the global best
#             if current < best:
#                 #update global best
#                 best_pos = self.position
#                 best = current
#         return best_pos, best
        
    
#     """Update Velocity"""
#     def updateVel(self, inertia, alpha, beta, gamma, lbound, ubound, gbest):
#         # add decaying weight here
#         velocity = inertia * self.velocity + alpha*np.random.rand(self.dims)*(self.pbest - self.position) + beta*np.random.rand(self.dims)*(gbest - self.position) + 0 #+ gamma*np.random.rand(self.dims)*(self.infbest - self.position)
#         # check if velocity out of bounds: 
#         for i in range (self.dims):
#             if velocity[i] > ubound:
#                 velocity[i] = ubound
#             if velocity[i]< lbound:
#                 velocity[i] = lbound
#         self.velocity = velocity
      
        
# # default fitness function. 
# def sphere(inputs):
#     return np.sum(inputs ** 2)
