# Logan Barnes
# Overdraft

# Initialize list
ledger = []

# Read data
numtrans = int(input())

for i in range(numtrans):
    trans = int(input())
    ledger.append(trans)

print(ledger)

total = 0
minimum = 0

for t in range(numtrans):
    total += ledger[t]
    print("total: " + str(total))
    minimum = min(total, minimum)
    print("minimum: " + str(minimum))
print(abs(minimum))