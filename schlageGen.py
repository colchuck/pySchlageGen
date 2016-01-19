class schlageGen(object):
    #code
    masterKey = None
    tenantSet = None
    tenants= None

    def __init__(self):
        self.masterKey = None
        
    def addMasterKey(self,schlageKey):
        self.masterKey = schlageKey
        
    def genSystemSub(self,subMasters,tenantsPerSub):
        mastCuts = masterKey.getCuts()
        
    def genSystem(self,tenants):
        self.tenants=tenants
        self.tenantSet = []
        self.__recSysGen(self.masterKey.getCuts()[:],len(self.masterKey.getCuts()))
        return self.tenantSet
        
    def __recSysGen(self, tenantTemp, k):
        j=0
        while j<5:
            d = tenantTemp[-k]
            if d+2==10 or d+2==11: d = d%2
            else: d = d+2
            tenantTemp[-k] = d
            if k==1:
                if not d == self.masterKey.getCuts()[-k] and self.__maxCheck(tenantTemp):
                    self.tenantSet.append(tenantTemp[:])
                if len(self.tenantSet)>=self.tenants: return 0
            else:
                if not tenantTemp[-k] == self.masterKey.getCuts()[-k]:
                    if self.__recSysGen(tenantTemp,k-1) == 0: return 0
            j=j+1
            
    def __maxCheck(self,keyCuts, max=6):
        i = 0
        while i<len(keyCuts)-1:
            if abs(keyCuts[i]-keyCuts[i+1]) > max: return False
            i=i+1
        return True
        
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
            
        
        
        
