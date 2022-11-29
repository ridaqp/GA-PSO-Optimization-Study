import particle
import numpy as np
from optproblems import cec2005



class PSO():
    def __init__(self, size, dims=2, lbound = -100, ubound=100, eps= 0.5, iters=50, w=0.5, alpha=0.8, beta=0.9):
        self.size = size
        self.population = [particle.Particle(dims, eps, iters) for _ in range(size)]
        self.gBest_value = float('inf')
        self.gBest_position = np.zeros(dims)
        self.alpha = alpha
        self.beta = beta
        self.inertia = w
        self.ubound = ubound
        self.lbound = lbound
        self.dims = dims
            
    def fitness(self, particle):
       return np.sum(np.square(particle.position))
    
    def set_pBest(self):
        for particle in self.population:
            fitness_candidate = self.fitness(particle)
            if(particle.pBest_value > fitness_candidate):
                particle.pBest_value = fitness_candidate
                particle.pBest_position = particle.position
                
    def set_gBest(self):
        for particle in self.population:
            best_fitness_candidate = self.fitness(particle)
            if(self.gBest_value > best_fitness_candidate):
                self.gBest_value = best_fitness_candidate
                self.gBest_position = particle.position

    
                
    def evaluate(self):
        for particle in self.population:
            
            # get a set of informants
            informants = np.random.choice(self.population,6)
            #do opposite and remove it from here
            if particle not in informants:
                np.append(informants, particle)

            current = float('inf')
            for i in range (len(informants)):
                next = informants[i]
                #compare fitness of current article against all informants
                if(self.fitness(next) < current):
                    infposition = next.position
                    current = self.fitness(next)   
            
            self_confidence = self.alpha * np.random.rand(self.dims) * (particle.pBest_position - particle.position)
            swarm_confidence = self.beta * np.random.rand(self.dims) * (self.gBest_position - particle.position)
            social_confidence = 0.3 * np.random.rand(self.dims) * (infposition - particle.position)
            new_velocity = self.inertia * particle.velocity + self_confidence + swarm_confidence +social_confidence
            particle.velocity = new_velocity
            particle.update(self.ubound, self.lbound)
            
    def show_particles(self, iteration):        
        print(iteration, 'iterations')
        print('BestPosition in this time:', self.gBest_position)
        print('BestValue in this time:', self.gBest_value)


#Tests: 
search_space = PSO(100)

iteration = 0
while(iteration < 50):
    search_space.set_pBest()
    search_space.set_gBest()

    # results
    search_space.show_particles(iteration)
    search_space.evaluate()
    iteration += 1
    
print("The best solution is: ", search_space.gBest_position, " in ", iteration, " iterations")
        



















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







