import numpy as np
import random

# for testing
from optproblems import cec2005

class GA:

    def __init__(self, function, min_bound, max_bound, dims, pop = 100, gen = 20):
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
            individual = [round(random.uniform(self.min_bound, self.max_bound),4) for _ in range(self.dims)]
            self.population.append(individual)
        #print("population:", self.population)

        self.best_individual, self.best_value = self.population[0], self.function(self.population[0])



    """ MUTATION """
    def mutation(self, mr = 0.5):

        if len(self.population[0]) <= 1:
            print("No mutation can occur for individuals with 1 or less variables")

        # iterating through the whole population
        for i in self.population:
            # iterating through each individual
            for j in range(len(i)):
                # if random number is below the mutation rate, it falls under the probability
                if mr > random.random():
                    # shuffle in place, acts as mutation
                    random.shuffle(i)



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
    def tournament_selection(self, values, k = 3):
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
    def run_ga(self, k = 3, cr = 0.7, mr = 0.5):
        
        # calculating function values of each member of population
        # it contains the values returned by the objective function

        print("original population", self.population)

        for generation in range(self.generations):

            print("Generation", generation)

            print("THE FITNESS VALUE")
            print("the position", self.population[1])
            print(self.function(self.population[1]))
            # finding values from objective function
            values = [self.function(i) for i in self.population]

            # saving best individual
            index = np.argmin(values)
            value = min(values)
            individual = self.population[index]
            
            if self.best_value > value:
                self.best_value = value
                self.best_individual = individual

            print(f"New best individual is {self.best_individual}, with minima {self.best_value}")

            # running tournament selection
            self.tournament_selection(values, k)
            #print("population after selection:", self.population)
            # running crossover
            self.crossover(cr)
            #print("population after crossover:", self.population)
            # running mutation
            self.mutation(mr)
            #print("population after mutation:", self.population)
        
        print(f"Final best individual is {self.best_individual}, with minima {self.best_value}")
        

test = cec2005.F1(2)
ga = GA(test, -100, 100, 2, 100, 10)
ga.run_ga()