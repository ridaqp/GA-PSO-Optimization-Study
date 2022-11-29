from . import particle
import numpy as np
from optproblems import cec2005


class PSO():
    def __init__(self, size=50, dims=10, lbound = -100, ubound=100, eps= 0.9, iters=150, w=0.7, alpha=0.5, beta=1.5, gamma = 1.5, obj = cec2005.F1):
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
        self.bestiter = 0

    """Function to get the fitness value of a particle"""     
    def get_fit(self, particle):
       return self.obj(particle.position)
    
    """Function to update the personal best position of particles in the population"""
    def update_pBests(self):
        for particle in self.population:
            current = self.get_fit(particle)
            if(particle.pBest > current):
                particle.pBestPos = particle.position

    """Function to update the global best position of particles in the population"""           
    def update_gBest(self,i):
        for particle in self.population:
            current = self.get_fit(particle)
            if(self.gBest > current):
                self.gBest = current
                self.gBestPos = particle.position
                self.bestiter = i

    
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
            self.update_gBest(i)

            self.evaluate()
           


#PSO(lbound = -100, ubound = 100, size = 50, iters =100).optimize()

#Tests: 
#PSO(100).optimize()
#PSO(10, 10, iters= 1000).optimize()
#PSO(50, 2, -100, 100, 1, 50, 0.5, 0.8, 0.9,0).optimize()
#PSO(50, 10, -100, 100, 1, 100, 0.5, 1.5, 0.9,0).optimize()






















