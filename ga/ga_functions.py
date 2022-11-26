import numpy as np
import matplotlib.pyplot as plt
import random

# for testing
from optproblems import cec2005

class GA:

    def __init__(self, function, min_bound, max_bound, dims, pop, gen):
        # objective function
        self.function = function
        self.min_bound = min_bound # min int value for function
        self.max_bound = max_bound # max int value for function
        self.dims = dims # number of variables of each input to objective function

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
        print("population:", self.population)




    """ ONE-POINT CROSSOVER """
    def crossover(self, population, cr):
        # by default, crossover is copy of previous gen parents
        newPopulation = population.copy()

        # forming parent pairs in population
        for i in range(0, self.npop, 2):
            # checking probability of crossover
            # if random number is below the crossover rate, it falls under the probability
            if cr > random.random():
                # finding crossover point within length of parent (dims)
                cp = random.randint(0, self.dims - 1)
                # performing crossover, creating 2 new children by merging variables from parents
                # to or from crossover point
                newPopulation[i] = population[i][:cp] + population[i+1][cp:]
                newPopulation[i+1] = population[i+1][:cp] + population[i][cp:]

        print("new cross pop:", newPopulation)
        return newPopulation



    """ TOURNAMENT SELECTION """
    def tournament_selection(self, population, k = 3):

        # calculating fitness of each member of population
        # it contains the values returned by the objective function
        fitness = [self.function(i) for i in population]
        newPopulation = []
        print("fitness:", fitness)

        for i in range(self.npop):
            # extracting random indexes
            random_index = np.random.choice(self.npop, k)
            
            best = random_index[0]
            # finding best index from k number of random indexes (tournament)
            for j in random_index:
                if fitness[best] > fitness[j]:
                    best = j

            # inserting best individual from k random instances of population
            newPopulation.append(population[best])
        
        print("new fit pop:", newPopulation)
        return newPopulation
    

test = cec2005.F1(1)
ga = GA(test, -100, 100, 1, 10, 10)
ga.tournament_selection(ga.population, 3)
ga.crossover(ga.population, 0.9)