# Logan Barnes
# Kattis
# Grand Adventure

# Read first line and store in numRoutes
numRoutes = int(input())

# Initialize an array of route lists
routes = [[] for i in range(numRoutes)]

def readRoute(i):
    # Read a line from input and store in route[i], ignoring periods
    routes[i] = input().replace('.', '').split()

def adventure(i):
    # Iterate though each route
    # If *, $, or |, add to backpack
    # If t, check if last item in backpack is |. If so, remove it, otherwise, print NO.
    # If j, check if last item in backpack is *. If so, remove it, otherwise, print NO.
    # If b, check if last item in backpack is $. If so, remove it, otherwise, print NO.

    backpack = []

    for e in range(len(routes[i])):
        if routes[i][e] == '*':
            backpack.append('*')
        elif routes[i][e] == '$':
            backpack.append('$')
        elif routes[i][e] == '|':
            backpack.append('|')
        elif routes[i][e] == 't':
            if backpack[-1] == '|':
                backpack.pop()
            else:
                print("NO")
                pass
        elif routes[i][e] == 'j':
            if backpack[-1] == '*':
                backpack.pop()
            else:
                print("NO")
                pass
        elif routes[i][e] == 'b':
            if backpack[-1] == '$':
                backpack.pop()
            else:
                print("NO")
                pass
        else:
            # If backpack is empty, print YES, else print NO
            if len(backpack) == 0:
                print("YES")
                pass
            else:
                print("NO")
                pass

def main():
    # For numRoutes, read input and store in routes
    # For each route, determine if the adventurer can finish his adventure
    for i in range(numRoutes):
        readRoute(i)
        print(routes[i])
        adventure(i)
    return 0

main()