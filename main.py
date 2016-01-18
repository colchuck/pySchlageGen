import schlageGen
import schlageKey

mastRaw = input("Master Key:")
tenants = int(input("Tenants:"))
mastCuts = mastRaw.split(" ")
mastCuts = list(map(int, mastCuts))
mastKey = schlageKey.schlageKey(mastCuts,len(mastCuts))
gen = schlageGen.schlageGen()
gen.addMasterKey(mastKey)
output = gen.genSystem(tenants)
for e in output:
    print(e)