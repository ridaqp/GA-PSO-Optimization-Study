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
        #print("population:", self.population)



    """ TOURNAMENT SELECTION """
    def tournament_selection(self, population, k = 3):

        # calculating function values of each member of population
        # it contains the values returned by the objective function
        values = [self.function(i) for i in population]

        # saving best individual incase deleted by mistake
        best_index = np.argmin(values)
        best_individual = population[best_index]

        newPopulation = []
        #print("values:", values)

        for i in range(self.npop):
            # extracting random indexes
            random_index = np.random.choice(self.npop, k)
            
            best = random_index[0]
            # finding best index from k number of random indexes (tournament)
            for j in random_index:
                if values[best] > values[j]:
                    best = j

            # inserting best individual from k random instances of population
            newPopulation.append(population[best])
        
        # we want to make sure we do not lose the lowest value incase 
        if best_individual not in newPopulation:
            print("true")
            newPopulation[-1] = best_individual
        #print("new fit pop:", newPopulation)
        return newPopulation



    """ MUTATION """
    def mutation(self, population, mr):

        # if len(population[0]) <= 1:
        #     raise ValueError("No mutation can occur for individuals with 1 or less variables")
        # iterating through the whole population
        for i in population:
            # iterating through each individual
            for j in range(len(i)):
                # if random number is below the mutation rate, it falls under the probability
                if mr > random.random():
                    # shuffle in place, acts as mutation
                    random.shuffle(i)

        #print("mutation pop:", population)
        return population



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

        #print("new cross pop:", newPopulation)
        return newPopulation
    

test = cec2005.F1(1)
ga = GA(test, -100, 100, 1, 10, 10)
ga.tournament_selection(ga.population, 3)
ga.crossover(ga.population, 0.9)
ga.mutation(ga.population, 0.5)