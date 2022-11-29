import numpy as np
import random

# for testing
from optproblems import cec2005

class GA:

    def __init__(self, function, min_bound, max_bound, dims, pop = 100, gen = 100):
        # objective function
        self.function = function
        self.min_bound = min_bound # min int value for function
        self.max_bound = max_bound # max int value for function
        self.dims = dims # number of variables of each input to objective function

        # population number
        self.npop = pop
        # number of generations
        self.generations = gen

        self.population = []
        
        # population is a nested list, each element with dims number of elements
        for i in range(self.npop):
            # finding each individual of the population by selecting random number between min and max bound
            # of the objective function for dims number of times

            """ the calulcation of an individual has been taken from the sample code cec2005_test.py provided by Prof. Hadj"""
            individual = [round(random.uniform(self.min_bound, self.max_bound),4) for _ in range(self.dims)]
            self.population.append(individual)
        #print("population:", self.population)



    """ MUTATION """
    def mutation(self, mr = 0.5):

        # iterating through the whole population
        for i in range(self.npop):
            # if random number is below the mutation rate, it falls under the probability
            if mr > random.random():
                # adding random value of gaussian distribution to each element of individual
                #print("before", self.population[i])
                for x in range(self.dims):
                    # mutating new gene
                    new_gene = self.population[i][x] + np.random.normal()
                    # only add new gene to population if it is within bounds
                    if self.min_bound <= new_gene <= self.max_bound: 
                        self.population[i][x] = new_gene
                #print("after", self.population[i])


    """ ONE-POINT CROSSOVER """
    def crossover(self, cr = 0.7):
        # by default, crossover is copy of previous gen parents
        newPopulation = self.population.copy()

        # forming parent pairs in population
        for i in range(0, self.npop - 1, 2):
            # checking probability of crossover
            # if random number is below the crossover rate, it falls under the probability
            if cr > random.random():
                # finding crossover point within length of parent (dims)
                cp = random.randint(0, self.dims - 1)
                # performing crossover, creating 2 new children by merging variables from parents
                # to or from crossover point
                newPopulation[i] = self.population[i][:cp] + self.population[i+1][cp:]
                newPopulation[i+1] = self.population[i+1][:cp] + self.population[i][cp:]

        self.population = newPopulation
    

    """ TOURNAMENT SELECTION """
    def tournament_selection(self, values, k):
        newPopulation = []

        for i in range(self.npop):
            # extracting random indexes
            random_index = np.random.choice(self.npop, k)
            
            best = random_index[0]
            # finding best index from k number of random indexes (tournament)
            for j in random_index:
                if values[best] > values[j]:
                    best = j

            # inserting best individual from k random instances of population
            newPopulation.append(self.population[best])

        self.population = newPopulation



    """ GENETIC ALGORITHM """
    def run_ga(self, k = 5, cr = 0.8, mr = 0.6):
        
        # calculating function values of each member of population
        # it contains the values returned by the objective function
        self.best_individual, self.best_value, self.best_gen = self.population[0], self.function(self.population[0]), 0
        
        for generation in range(self.generations):


            # finding values from objective function
            values = [self.function(i) for i in self.population]

            # saving best individual
            index = np.argmin(values)
            value = min(values)
            individual = self.population[index]
            
            if self.best_value > value:
                self.best_value = value
                self.best_individual = individual
                self.best_gen = generation

            # running tournament selection
            self.tournament_selection(values, k)
            #print("population after selection:", self.population)
            # running crossover
            self.crossover(cr)
            #print("population after crossover:", self.population)
            # running mutation
            self.mutation(mr)
            #print("population after mutation:", self.population)
        
        return self.best_individual, self.best_value, self.best_gen