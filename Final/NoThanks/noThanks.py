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
    # Sort cards in reverse order
    cards.sort(reverse = True)
    pass

def calcScore():
    # Iterate through cards
    # For any cards that are sequential, only add the first card in the sequence to the score
    # Add any cards that are not sequential to the score

    score = 0
    i = 0

    while i < len(cards):
        if i + 1 < len(cards) and cards[i] - 1 == cards[i + 1]:
            i += 2 # Skip the next card
        else:
            score += cards[i] # Count the current card
            i += 1

    return score

def main():

    readCards()
    sortCards()
    print(cards)
    print(calcScore())

    return 0

main()