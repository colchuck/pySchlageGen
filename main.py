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
i=1
for e in output:
    if i< 9:
        o= "  " + str(i)
    if i < 100 and i>9:
        o= " " + str(i)
    print(o + ":  ", end="")
    for f in e:
        print(str(f) + " ", end="")
    print("\n--------------------")
    bitting = gen.bittingCalc(e)
    print("  M:  ",end="")
    for f in bitting[0]:
        if f==0:
            f="x"
        print(str(f) + " ",end="")
    print()
    print("  B:  ",end="")
    for l in bitting[1]:
        print(str(l) + " ",end="")
    print("\n")
    i=i+1
