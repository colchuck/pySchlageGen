import schlageGen
import signal
import sys
def ctrlc_handler(signal, frame):
        print('\nCtrl+C pressed')
        sys.exit(0)
signal.signal(signal.SIGINT, ctrlc_handler)
mastRaw = input("Master Key:").rstrip()
tenants = int(input("Tenants:"))
inc = int(input("Increment:"))
mastCuts = mastRaw.split(" ")
mastCuts = list(map(int, mastCuts))
gen = schlageGen.schlageGen()
gen.addMasterKey(mastCuts)
output = gen.genSystem(tenants,inc)
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
    print("\n---------------------")
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
exit(0)
