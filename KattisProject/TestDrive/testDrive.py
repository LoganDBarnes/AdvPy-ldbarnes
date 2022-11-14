# Logan Barnes
# Test Drive

import sys

# Determine car movement
def calcMovt():
    # if direction changed
    if (pos[2] - pos[1]) > 0 and (pos[1] - pos[0] < 0) or (pos[2] - pos[1]) < 0 and (pos[1] - pos[0] > 0):
        print("turned")

    elif abs(pos[2] - pos[1]) > abs(pos[1] - pos[0]):
        print("accelerated")

    elif abs(pos[2] - pos[1]) < abs(pos[1] - pos[0]):
        print("braked")

    elif abs(pos[2] - pos[1]) == abs(pos[1] - pos[0]):
        print("cruised")

    else:
        return 0

# Read position data
data = input()
 
# Convert string to tuple
pos = tuple(map(int, data.split()))
 
# Print position data
#print("positions: " + str(pos))

calcMovt()