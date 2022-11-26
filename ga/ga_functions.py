import numpy as np
import matplotlib.pyplot as plt
import random

class GA:

    def __init__(self, function, min_bound, max_bound, dims, pop, gen):
        self.function = function
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.dims = dims
        
        self.npop = pop
        self.gen = gen

        self.population = []
        
        for i in range(self.npop):
            individual = [round(random.uniform(self.min_bound, self.max_bound),4) for _ in range(self.dims)]
            self.population.append(individual)
        
