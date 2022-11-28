
import numpy as np
import matplotlib.pyplot as plt

def Sphere(x):
    z = np.sum(np.square(x))
    return z

#parameters
d = 10
xMin, xMax = -100, 100
vMin, vMax = -0.2 * (xMax - xMin), 0.2*(xMax - xMin)
MaxIt = 300
ps = 10
c1 = 2
c2 = 2
w = 0.9 -((0.9-0.4)/MaxIt) * np.linspace(0, MaxIt, MaxIt)

#helper functions
def limitV(V):
    for i in range (len(V)):
        if V[i] > vMax:
            V[i] = vMax
        if V[i]< vMin:
            V[i] = vMin
    return V

def limitX(X): 
    for i in range (len(X)):
        if X[i] > xMax:
            X[i] = xMax
        if X[i]< xMin:
            X[i] = xMin
    return X


#algo

def optimization():
    class Particle():
        def __init__(self) -> None:
            self.position = np.random.uniform(xMin, 50, [ps,d])
            #print("the init position vector", self.position)
            self.velocity = np.random.uniform(vMin, vMax, [ps,d])
            # finding values from objective function
            #print(len(self.position))
            #print("the position", self.position[1])
            #self.cost = np.asarray([test(i) for i in self.position])
           

            self.cost = np.zeros(ps)
            self.cost[:] = Sphere(self.position[:])
            self.pbest = np.copy(self.position)
            self.pbest_cost = np.copy(self.cost)
            self.index = np.argmin(self.pbest_cost)
            self.gbest = self.pbest[self.index]
            self.gbest_cost = self.pbest_cost[self.index]
            # array of the best cost at every iteration
            self.BestCost = np.zeros(MaxIt)
        
        def Evaluate(self):
            for it in range(MaxIt):
                # for every particle
                for i in range(ps):
                    #update its velocity
                    self.velocity[i] = (w[it]*self.velocity[i] 
                                        + c1*np.random.rand(d)*(self.pbest[i] - self.position[i]) 
                                        + c2*np.random.rand(d)*(self.gbest - self.position[i]))
                    #limit its velocity
                    self.velocity[i] = limitV(self.velocity[i])
                    print(len(self.velocity))

                    #update its position
                    self.position[i] = self.position[i] + self.velocity[i] #epsilon?
                    print(self.position[i])

                    #limit its position
                    self.position[i] = limitX(self.position[i])

                    #check fitness
                    self.cost[i] = Sphere(self.position[i])
                    
                    #broke personal record
                    if self.cost[i] < self.pbest_cost[i]:
                        self.pbest[i] = self.position[i]
                        self.pbest_cost[i] = self.cost[i]

                        if self.pbest_cost[i]<self.gbest_cost:
                            self.gbest = self.pbest[i]
                            self.gbest_cost = self.pbest_cost[i]
                self.BestCost[it] = self.gbest_cost


        def Plot(self):
            plt.semilogy(self.BestCost)
            print("Best Fitness Value = ", self.gbest_cost)

    a = Particle()
    a.Evaluate()
    a.Plot()

optimization()

