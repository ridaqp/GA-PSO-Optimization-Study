import numpy as np
import matplotlib.pyplot as plt
import random

class GA:

    def __init__(self, function, min_bound, max_bound, dims, pop, gen):
        # objective function
        self.function = function
        self.min_bound = min_bound # min int value for function
        self.max_bound = max_bound # max int value for function
        self.dims = dims # dimension of each input to objective function

        # population number
        self.npop = pop
        # number of generations
        self.gen = gen

        self.population = []
        
        # population is a nested list, each element with dims number of elements
        for i in range(self.npop):
            # finding each individual of the population by selecting random number between min and max bound
            # of the objective function for dims number of times
            individual = [round(random.uniform(self.min_bound, self.max_bound),4) for _ in range(self.dims)]
            self.population.append(individual)


    """ TOURNAMENT SELECTION """
    def tournament_selection(self, population, k = 3):

        # calculating fitness of each member of population
        # it contains the values returned by the objective function
        fitness = [self.function(i) for i in population]
        newpopulation = []

        for i in range(self.npop):
            # extracting random indexes
            random_index = np.random.choice(self.npop, k)
            
            best = random_index[0]
            # finding best index from k number of random indexes (tournament)
            for j in random_index:
                if fitness[j] > fitness[best]:
                    best = j

            # inserting best individual from k random instances of population
            newpopulation.append[population[best]]
        
        return newpopulation