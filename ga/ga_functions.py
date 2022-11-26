import numpy as np
import matplotlib.pyplot as plt
import random

class GA:

    def __init__(self, function, min_bound, max_bound, dims, pop, gen):
        self.function = function
        
        self.npop = pop
        self.gen = gen

        self.population = []
        
        for i in range(self.npop):
            individual = [round(random.uniform(min_bound, max_bound),4) for _ in range(dims)]
            self.population.append(individual)