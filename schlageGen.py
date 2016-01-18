class schlageGen(object):
    #code
    masterKey = None
    def __init__(self):
        self.masterKey = None
        
    def addMasterKey(self,schlageKey):
        self.masterKey = schlageKey
        
    def genSystemSub(self,subMasters,tenantsPerSub):
        mastCuts = masterKey.getCuts()
        
    def genSystem(self,tenants):
        mastCuts = self.masterKey.getCuts()
        tenantTemp = mastCuts[:]
        tenantSet = []
        j=0
        f=0
        while f < len(mastCuts):
            while j < len(mastCuts):
                tenantTemp = mastCuts[:]
                while tenantTemp[j] < 8:
                    tenantTemp[j] = tenantTemp[j] + 2
                    tenantSet.append(tenantTemp[:])
                    if len(tenantSet) >= tenants:
                        return tenantSet
                j=j+1
            j=f +1    
            if not (mastCuts[f] + 2 >10 ): 
                mastCuts[f] = mastCuts[f] + 2
            else:
                f=f+1
        
        
