import sys

#initialize string
data = "5 2 5"

# sample data
data1 = "1 2 3"
data2 = "5 4 1"
data3 = "8 9 7"
data4 = "10 20 25"
 
# convert string to tuple
pos = tuple(map(int, data.split()))

# convert sample data
pos1 = tuple(map(int, data.split()))
pos2 = tuple(map(int, data2.split()))
pos3 = tuple(map(int, data3.split()))
pos4 = tuple(map(int, data4.split()))
 
# print postions
print("positions: " + str(pos))
print("pos2: " + str(pos2))
print("pos3: " + str(pos3))
print("pos4: " + str(pos4))

if (pos[2] - pos[1]) > 0 and (pos[1] - pos[0] < 0) or (pos[2] - pos[1]) < 0 and (pos[1] - pos[0] > 0):
    print("turned")

elif abs(pos[2] - pos[1]) > abs(pos[1] - pos[0]):
    print("accelerated")

elif abs(pos[2] - pos[1]) < abs(pos[1] - pos[0]):
    print("braked")

elif abs(pos[2] - pos[1]) == abs(pos[1] - pos[0]):
    print("cruised")

else:
    print("error")