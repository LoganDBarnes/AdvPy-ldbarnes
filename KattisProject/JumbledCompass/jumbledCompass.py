# Logan Barnes
# Jumbled Compass

start = int(input())
end = int(input())

if start == end:
    print("0")

elif start < end:
    clockwise = (end - start)
    counterClock = ((360 - end) + start)

    if clockwise <= counterClock:
        print(clockwise)
    else:
        print(-counterClock)

elif start > end:
    counterClock = (start - end)
    clockwise = ((360 - start) + end)

    if counterClock < clockwise:
        print(-counterClock)
    else:
        print(clockwise)

else:
    print("You're off the edge of the map, mate.")