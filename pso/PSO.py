import particle
import numpy as np
from optproblems import cec2005
import objectivefunctions


class PSO():
    def __init__(self, size, dims=2, lbound = -100, ubound=100, eps= 0.5, iters=50, w=0.5, alpha=0.8, beta=0.9, gamma = 0.3, obj = objectivefunctions.Sphere):
        self.size = size
        self.population = [particle.Particle(dims, eps, lbound, ubound) for _ in range(size)]
        self.gBest_value = float('inf')
        self.gBestPos = np.zeros(dims)
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.inertia = w
        self.ubound = ubound
        self.lbound = lbound
        self.obj = obj
        self.dims = dims
        self.iters = iters

            
    def fitness(self, particle):
       return self.obj(particle.position)
    
    def update_pBests(self):
        for particle in self.population:
            current = self.fitness(particle)
            if(particle.pBest > current):
                particle.pBest = current
                particle.pBestPos = particle.position
                
    def update_gBest(self):
        for particle in self.population:
            current = self.fitness(particle)
            if(self.gBest_value > current):
                self.gBest_value = current
                self.gBestPos = particle.position

    
                
    def evaluate(self):
        for particle in self.population:
            
            # get a set of informants
            informants = np.random.choice(self.population,6)
            if particle not in informants:
                np.append(informants, particle)

            current = float('inf')
            for i in range (len(informants)):
                next = informants[i]
                #compare fitness of current article against all informants
                if(self.fitness(next) < current):
                    infposition = next.position
                    current = self.fitness(next)   

            
            #update velocity components
            
            cognitive = np.random.rand(self.dims) * (particle.pBestPos - particle.position)
            population = np.random.rand(self.dims) * (self.gBestPos - particle.position)
            social = np.random.rand(self.dims) * (infposition - particle.position)
            velocity = self.inertia * particle.velocity + self.alpha*cognitive + self.beta * population + self.gamma * social
            
            #update velocity
            particle.updateVel(velocity)

            #update position
            particle.updatePos()
            
    def optimize(self):
        itr = 0
        while(itr < self.iters):
            self.update_pBests()
            self.update_gBest()

            # results
            self.show_particles(itr)
            self.evaluate()
            itr += 1

        print("The best solution is: ", self.gBestPos, " in ", itr, " iterations")


    def show_particles(self, iteration):        
        print(iteration, 'iterations')
        print('BestPosition in this time:', self.gBestPos)
        print('BestValue in this time:', self.gBest_value)


#Tests: 
PSO(100).optimize()



        



















# class PSO(): 
#     #global bestpos; 

#     def __init__(self, objective, lbound, ubound, step, dims = 10, size= 10, iters = 300,  w = 0.6, alpha = 0.8, beta = 0.9, gamma = 2 ):

#         self.swarm = [particle.particle(dims, size, lbound, ubound, step, objective, iters) for i in range(size)] 

#         # set upper limits on hyperparams:
#         self.inertia = w # weight for previous velocity
#         self.alpha = alpha  # acceleration coefficient for personal best
#         self.beta = beta  # acc. coeff. for informants best
#         self.gamma = gamma  # acc. coeff. for global best

#         # set bounds on dimensions for input
#         self.lbound, self.ubound = lbound, ubound
#         # set bounds on dimensions for velocity
#         self.vlbound, self.vubound = -0.2 * (ubound - lbound), 0.2*(ubound - lbound)

#         self.gbest = float('inf')
#         self.gbest_pos = np.zeros(dims)
#         self.iters = iters

#     def evaluate_swarm(self):
#         for i in range (self.iters):
#             # evaluate each particle
#             for particle in self.swarm:
#                 particle.updateVel(self.inertia, self.alpha, self.beta, self.gamma, self.vlbound, self.vubound, self.gbest_pos )

#                 self.gbest_pos, self.gbest = particle.updatePos(self.lbound, self.ubound, self.gbest_pos, self.gbest)
#         return self.gbest_pos, self.gbest

# #Test: 
# benchmark = cec2005.F1(10)
# # create pso 
# swarm = PSO(benchmark, -100, 100, 0.5, 10, 30, 50)
# best, value = swarm.evaluate_swarm()
# print(" the best search position is", best, "whose values is", value)







