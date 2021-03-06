class schlageGen(object):
    masterKey = None
    tenantSet = None
    tenants= None

    def __init__(self):
        self.masterKey = None
        
    def addMasterKey(self,master):
        self.masterKey = master
        
    def setTenants(self,tenSet):
        self.tenantSet = tenSet[:]
    def getMasterKey(self):
        return self.masterKey
    def genSystemSub(self,subMasters,tenantsPerSub):
        mastCuts = masterKey
        
    def getSystem(self):
        return self.tenantSet
    
    def genSystem(self,tenants,inc=2):
        self.tenants=tenants
        self.tenantSet = []
        self.__recSysGen(self.masterKey[:],len(self.masterKey),inc)
        return self.tenantSet
        
    def __recSysGen(self, tenantTemp, k, inc=2):
        j=0
        if inc%2==1: m =10
        else: m =5   
        while j<m:
            d = tenantTemp[-k]
            if d+inc>9:
                d = int(str(d+inc)[-1])
            else: d = d+inc
            tenantTemp[-k] = d
            if k==1:
                if not d == self.masterKey[-k] and self.__maxJumpCheck(tenantTemp) and self.__minPinCheck(tenantTemp):
                    self.tenantSet.append(tenantTemp[:])
                if len(self.tenantSet)>=self.tenants: return 0
            else:
                if not tenantTemp[-k] == self.masterKey[-k]:
                    if self.__recSysGen(tenantTemp,k-1, inc) == 0: return 0
            j=j+1
            
    def __maxJumpCheck(self,keyCuts, max=6):
        i = 0
        while i<len(keyCuts)-1:
            if abs(keyCuts[i]-keyCuts[i+1]) > max: return False
            i=i+1
        return True
    
    def __minPinCheck(self, keyCuts, min=2):
        i=0
        while i<len(keyCuts):
            if abs(self.masterKey[i]-keyCuts[i]) < min: return False
            i=i+1
        return True

    def bittingCalc(self,tenantKey):
        tenCuts = tenantKey[:]
        mastCuts = self.masterKey[:]
        i=0
        master=[]
        bottom=[]
        while i<len(mastCuts):
            chamber = [mastCuts[i],tenCuts[i]]
            bottom.append(min(chamber))
            master.append(max(chamber) - min(chamber))
            i=i+1
        return [master,bottom]