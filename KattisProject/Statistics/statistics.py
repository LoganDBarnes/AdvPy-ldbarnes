# Logan Barnes
# Statistics

# Initialize list
stats = []

def calcStats():

    i=0

    # Read input and append to list
    
    for line in iter(input, ''):
        line = line.replace(' ', '')
        stats.append(int(line))

        #Calculate stats
        minimum = min(line)
        maximum = max(line)
        #rng = abs(int(maximum)) - abs(int(minimum))
        rng = 0

        # Print stats
        print("Case " + str(i+1) + ": " + str(minimum) + " " + str(maximum) + " " + str(rng))
        i+=1

    return 0

calcStats()