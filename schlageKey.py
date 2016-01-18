class schlageKey(object):
    
    def __init__(self, cutList = [0,0,0,0,0], numCuts=5):
        self.cutList = cutList
        self.numCuts = numCuts
        
    def getCuts(self):
        return self.cutList
    
    def getNumCuts(self):
        return self.numCuts
        
