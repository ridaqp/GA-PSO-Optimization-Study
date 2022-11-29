import particle
import numpy as np
from optproblems import cec2005
#objectivefunctions.Sphere

class PSO():
    def __init__(self, size, dims=10, lbound = -100, ubound=100, eps= 0.5, iters=50, w=0.5, alpha=0.8, beta=0.9, gamma = 0.3, obj = cec2005.F20):
        # number of particles in the population
        self.size = size
        #initialise swarm
        self.population = [particle.Particle(dims, eps, lbound, ubound) for _ in range(size)]
        
        self.gBest = float('inf') # the best global positions value
        self.gBestPos = np.zeros(dims) # the best global position vector
        self.alpha = alpha # acceleration coefficient for personal best
        self.beta = beta # acc. coefficient for global best
        self.gamma = gamma #acc. coeff. for social best (among the informants)
        self.inertia = w #inertia weight
        self.ubound = ubound #upper bound for objective func
        self.lbound = lbound #lower bound for objective func
        self.obj = obj(dims) # the objective/fitness function
        self.dims = dims # dimensions in the search space 
        self.iters = iters #number of iterations to run PSO

    """Function to get the fitness value of a particle"""     
    def get_fit(self, particle):
       print(particle.position)
       return self.obj(particle.position)
    
    """Function to update the personal best position of particles in the population"""
    def update_pBests(self):
        for particle in self.population:
            current = self.get_fit(particle)
            if(particle.pBest > current):
                particle.pBestPos = particle.position

    """Function to update the global best position of particles in the population"""           
    def update_gBest(self):
        for particle in self.population:
            current = self.get_fit(particle)
            if(self.gBest > current):
                self.gBest = current
                self.gBestPos = particle.position

    
    """Function to evaluate the swarm - finds the best social position + updates the velocity and position of each particle"""           
    def evaluate(self):
        for particle in self.population:
            
            # get a set of random particles as informants - https://www.scottcondron.com/jupyter/optimisation/visualisation/2020/08/02/interactive-particle-swarm-optimisation-from-scratch-in-python.html
            informants = np.random.choice(self.population,6)
            if particle not in informants:
                # add self to informant set
                np.append(informants, particle)


            current = float('inf') # set infinity as a place holder for best position cost among informant
            for i in range (len(informants)):
                next = informants[i]
                #compare fitness of current particle against the current best informant's fitness
                if(self.get_fit(next) < current):
                    infposition = next.position
                    current = self.get_fit(next)   

            
            #update velocity components
            cognitive = np.random.rand(self.dims) * (particle.pBestPos - particle.position) # a portion of the distance from best personal
            population = np.random.rand(self.dims) * (self.gBestPos - particle.position) # a portion of the distance from best global 
            social = np.random.rand(self.dims) * (infposition - particle.position) # a portion of the distance from the best of the informants
            # calculate new velocity
            velocity = self.inertia * particle.velocity + self.alpha*cognitive + self.beta * population + self.gamma * social
            
            #update velocity
            particle.updateVel(velocity)

            #update position
            particle.updatePos()

    """Function to optimise the PSO i.e., evaluate the swarm by finding best global, and best personal and social positions for each particle n times.
    where 'n' is the number of iterations"""  
    def optimize(self):
        
        for i in range(self.iters):
            # find the personal best of all the particles in the swarm
            self.update_pBests()
            #find the global best position in the swarm
            self.update_gBest()

            # results
            self.show_particles(i)
            self.evaluate()
           
        print("The best global position is: ", self.gBestPos, " with value ", self.gBest)



    # def show_particles(self, iteration):        
    #     print(iteration, 'iterations')
    #     print('BestPosition in this time:', self.gBestPos)
    #     print('BestValue in this time:', self.gBest)


#Tests: 
#PSO(100).optimize()
#PSO(10, 10, iters= 1000).optimize()
#PSO(50, 2, -100, 100, 1, 50, 0.5, 0.8, 0.9,0).optimize()
#PSO(50, 2, -32, 32, 1, 100, 0.5, 0.8, 0.9,0).optimize()
PSO(50, 2, -5, 5, 1, 1000, 0.5, 0.8, 0.9,0).optimize() #410. 0 




















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







