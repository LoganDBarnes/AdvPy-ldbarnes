# Logan Barnes
# Overdraft

# Initialize list
ledger = []

def readInput():

    numtrans = int(input())

    for i in range(numtrans):
        trans = int(input())
        ledger.append(trans)
    pass

def calcBudget():

    total = 0
    minimum = 0

    for t in range(len(ledger)):
        total += ledger[t]
        #print("total: " + str(total))
        minimum = min(total, minimum)
        #print("minimum: " + str(minimum))
    print(abs(minimum))
    return 0

readInput()
#print(ledger)
calcBudget()