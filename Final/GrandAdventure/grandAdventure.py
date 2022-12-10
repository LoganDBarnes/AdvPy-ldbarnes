# Logan Barnes
# Kattis
# Grand Adventure

# Read first line and store in numRoutes
numRoutes = int(input())

# Initialize an array of size numRoutes containing route lists
routes = [[] for i in range(numRoutes)]

def readRoute(i):
    # Read a line from input and store each character as an element in routes[i], ignoring periods
    for e in input():
        if e != '.':
            routes[i].append(e)
    pass

def adventure(i):
    # Iterate though each route
    # If *, $, or |, add to backpack
    # If t, check if last item in backpack is |. If so, remove it, otherwise, print NO.
    # If j, check if last item in backpack is *. If so, remove it, otherwise, print NO.
    # If b, check if last item in backpack is $. If so, remove it, otherwise, print NO.

    backpack = []

    for e in routes[i]:
        #print(backpack)
        if e == '*' or e == '$' or e == '|':
            backpack.append(e)
        elif e == 't':
            if len(backpack) != 0 and backpack[-1] == '|':
                backpack.pop()
            else:
                print('NO')
                return
        elif e == 'j':
            if len(backpack) != 0 and backpack[-1] == '*':
                backpack.pop()
            else:
                print('NO')
                return
        elif e == 'b':
            if len(backpack) != 0 and backpack[-1] == '$':
                backpack.pop()
            else:
                print('NO')
                return
    
    if len(backpack) == 0:
        print('YES')
    else:
        print('NO')

def main():
    # For numRoutes, read input and store in routes
    # Determine if each route can be completed

    for i in range(numRoutes):
        readRoute(i)
        adventure(i)
    return 0

main()