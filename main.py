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
    if i < 10:
        o= "   " + str(i)
    elif i < 100:
        o= "  " + str(i)
    elif i < 1000:
        o= " " + str(i)
    else:
        o = str(i)
    print(o + ":  ", end="")
    for f in e:
        print(str(f) + " ", end="")
    print("\n--------------------")
    bitting = gen.bittingCalc(e)
    print("   M:  ",end="")
    for f in bitting[0]:
        if f==0:
            f="x"
        print(str(f) + " ",end="")
    print()
    print("   B:  ",end="")
    for l in bitting[1]:
        print(str(l) + " ",end="")
    print("\n")
    i=i+1
