
class particle(): 
    def __init__(self, dims, size):

        self.swarmsize = size #no. of particles in the swarm/population

        self.position = []   # current particle's position
        self.velocity = []   # current particle's velocity
        self.informants = [] # current particle's neighbours

        # current best positions
        self.infbest = self # the best position among neighbours
        self.pbest = self   # the particle's best
        self.gbest = self   # the swarm's best

        # hyperparameters
        self.inertia = 0 # weight for previous velocity
        self.alpha = 0  # acceleration coefficient for personal best
        self.beta = 0   # acc. coeff. for informants best
        self.gamma = 0  # acc. coeff. for global best


    def updatePos(self):
        self.updateVal()
        pass

    def updateVel(self):
        pass
        
        