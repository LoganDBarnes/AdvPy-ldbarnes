# Logan Barnes
# Jumbled Compass

start = int(input())
end = int(input())

def startGreater():
    clockwise = (end - start)
    counterClock = ((360 - end) + start)

    if clockwise <= counterClock:
        print(clockwise)
    else:
        print(-counterClock)

    pass

def endGreater():
    counterClock = (start - end)
    clockwise = ((360 - start) + end)

    if counterClock < clockwise:
        print(-counterClock)
    else:
        print(clockwise)

    pass

def compass():

    if start == end:
        print("0")

    elif start < end:
        startGreater()

    elif start > end:
        endGreater()

    else:
        print("You're off the edge of the map, mate.")

    return 0

compass()