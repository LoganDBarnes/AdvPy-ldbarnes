# Logan Barnes
# Kattis
# Right of Way

# Program to determine right of way for self-driving car
# Given direction car is approaching intersection, direction leaving intersection, and direction other vehicle is approaching intersection
# Car must yield right of way if it is going straight and there is a vehicle approaching from the right
# Car must yield right of way if it is turning left and there is a vehicle approaching from the right or straight ahead
# Output Yes if car must yield right of way, No if car has right of way


def goingStraight(carEnter, carLeave):
    straight = False

    if carEnter == 'North' and carLeave == 'South':
        straight = True
    elif carEnter == 'East' and carLeave == 'West':
        straight = True
    elif carEnter == 'South' and carLeave == 'North':
        straight = True
    elif carEnter == 'West' and carLeave == 'East':
        straight = True
    
    #print("going straight " + str(straight))
    return straight

def turningLeft(carEnter, carLeave):
    left = False

    if carEnter == 'North' and carLeave == 'East':
        left = True
    elif carEnter == 'East' and carLeave == 'South':
        left = True
    elif carEnter == 'South' and carLeave == 'West':
        left = True
    elif carEnter == 'West' and carLeave == 'North':
        left = True
    
    #print("turning left " + str(left))
    return left

def vehicleAhead(carEnter, vehicleApproach):
    ahead = False

    if carEnter == 'North' and vehicleApproach == 'South':
        ahead = True
    elif carEnter == 'East' and vehicleApproach == 'West':
        ahead = True
    elif carEnter == 'South' and vehicleApproach == 'North':
        ahead = True
    elif carEnter == 'West' and vehicleApproach == 'East':
        ahead = True
    
    #print("vehicle ahead " + str(ahead))
    return ahead

def vehicleRight(carEnter, vehicleApproach):
    right = False

    if carEnter == 'North' and vehicleApproach == 'West':
        right = True
    elif carEnter == 'East' and vehicleApproach == 'North':
        right = True
    elif carEnter == 'South' and vehicleApproach == 'East':
        right = True
    elif carEnter == 'West' and vehicleApproach == 'South':
        right = True

    #print("vehicle right " + str(right))
    return right

def main():

        carEnter, carLeave, vehicleApproach = input().split()
    
        if goingStraight(carEnter, carLeave) and vehicleRight(carEnter, vehicleApproach):
            print("Yes")
        elif turningLeft(carEnter, carLeave) and (vehicleRight(carEnter, vehicleApproach) or vehicleAhead(carEnter, vehicleApproach)):
            print("Yes")
        else:
            print("No")
    
        return 0

main()
