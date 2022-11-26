class particle(): 
    def __init__(self):
        self.position = []
        self.velocity = []
        self.pbest = []
        self.gbest = []
        self.dims = []
        self.inertia = 0
        self.alpha = 0
        self.beta = 0

    def evaluate(self):
        pass

    def updatePos(self):
        self.updateVal()
        pass

    def updateVel(self):
        pass
        
        