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
        mastCuts = self.masterKey.getCuts()[:]
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
            if not (mastCuts[f] + 3 >=10 ): 
                mastCuts[f] = mastCuts[f] + 3
            else:
                f=f+1
    
    def bittingCalc(self,tenantKey):
        tenCuts = tenantKey[:]
        mastCuts = self.masterKey.getCuts()[:]
        i=0
        master=[]
        bottom=[]
        while i<len(mastCuts):
            chamber = [mastCuts[i],tenCuts[i]]
            bottom.append(min(chamber))
            master.append(max(chamber) - min(chamber))
            i=i+1
        return [master,bottom]
            
        
        
        
