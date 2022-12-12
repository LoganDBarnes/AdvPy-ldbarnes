# Logan Barnes
# Kattis
# No Thanks

numCards = int(input())

# Initialize cards array
cards = []

def readCards():
    # Read a line from input and store each integer as an element in cards

    for e in input().split():
        cards.append(int(e))
    pass

def sortCards():
    cards.sort()
    pass

def calcScore():
    # Iterate through cards, starting at the second card
    # If the current card is 1 greater than the previous card, don't add it to the score
    # Else, add it to the score

    score = cards[0]
    prevCard = cards[0]

    for i in range(1, len(cards)):
        if cards[i] == prevCard + 1:
            prevCard = cards[i]
        else:
            score += cards[i]
        prevCard = cards[i]

    return score

def main():

    readCards()
    sortCards()
    #print(cards)
    print(calcScore())

    return 0

main()