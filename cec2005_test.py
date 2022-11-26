import random
import math
#import the set of functions F1 to F25
# function can have multiple variables 1 to 100 
from optproblems import cec2005
#import the Individual class that represent any individual solution
# this class has two main attributes 
# phenome: the actual values of the variables
# objective_values: the value(s) of the function after evaluation of the Individual
# the function evaluate() needs to be executed in order to get objective_values
""" DONT USE THIS """
from optproblems import Individual

# import BoundConstraintsRepair to repair variables that go out of bounds
from optproblems import BoundConstraintsRepair

#number of dimensions. 
# Note that for many functions the number of variables is limited to 2, 10, 30, 50
dims = 10
# setup objective function
#f1 = cec2005.F1(dims)
#func = f1
#set up bounds, each function has bounds on the variables
#min_bound = -100
#max_bound = 100
# the function can be anyone from CEC2005, e.g.
#f4=cec2005.F4(dims)
#func= f4
#set up bounds, each function has bounds on the variables
#min_bound = -100
#max_bound = 100
##or
#f5=cec2005.F4(dims)
#func= f5
#set up bounds, each function has bounds on the variables
#min_bound = -100
#max_bound = 100
#or
f12=cec2005.F12(dims)
func= f12
#set up bounds, each function has bounds on the variables
min_bound = -math.pi
max_bound = math.pi 

# create  bounds
bounds = ([min_bound] * dims, [max_bound] * dims)

#create the out of bounds repair method
# different options exist to repair, "reflect" is one of them
# you can also use "project", "wrap", 
repair = BoundConstraintsRepair(bounds, ["reflect"] * dims)

# obtain the global optimal solution
# global_optima is returned as a list of Individual to allow for multiple optima, usefull for some multimodal functions
global_optima = func.get_optimal_solutions()
#evaluate the global optimal solution
func.batch_evaluate(global_optima)
print("global solution and  associated objective values:")
for opt in global_optima:
    print(opt.phenome,opt.objective_values)

# create a random candidate solution (an Individual) using a random vector generated within bounds
# the solution is encapsulated in an Individual object in order to evaluate it
rand_solution = Individual(phenome=[round(random.uniform(min_bound, max_bound),4) for _ in range(dims)])

# here you might want to create a population of solutions
#  evaluate them and then 
#  evolve them according to PSO or GA

# You need to keep individual solutions within bounds
rand_solution.phenome = repair(rand_solution.phenome)
# you might want to check bounds first before repair
#  for that, you can use the class BoundConstraintError
#  with the boolea methods: min_bound_violated(value, min_bound) and max_bound_violated(value, max_bound)

#evaluate the random candidate solution
func.evaluate(rand_solution)
print("Random candidate solution and objective values:")  
#print the radom candidate solution and the associated objective values
print(rand_solution.phenome, rand_solution.objective_values)


