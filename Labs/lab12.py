def insert_sort(cards) -> None:
    '''
    Sorts a list in decreasing order using the insertion sort algorithm.
    '''
    for i in range(1, len(cards)):
        aux = cards[i]
        j = i - 1
        while (j >= 0 and cards[j] < aux):
            cards[j + 1] = cards[j]
            j = j - 1
        cards[j + 1] = aux

def binary_search(cards, search) -> int:
    '''
    Finds the index of an element in a list using a reverse binary search algorithm.
    '''
    low = 0
    high = len(cards) - 1
    while low <= high:
        mid = (high + low) // 2
        if cards[mid] < search:
            high = mid - 1
        elif cards[mid] > search:
            low = mid + 1
        else:
            return mid
    return -1

def trasform_cards_to_num(cards):
    '''
    Gets the data from a list of cards, then transforms it in an int that can be manipulated
    to retrieve the card number (A to K) and the card suit (O, E, C, P).
    '''
    cards_num = [0 for x in range(len(cards))]
    for i in range(len(cards)):
        if cards[i][0] == "A":
            cards_num[i] += 10
        elif cards[i][0] == "2":
            cards_num[i] += 20
        elif cards[i][0] == "3":
            cards_num[i] += 30
        elif cards[i][0] == "4":
            cards_num[i] += 40
        elif cards[i][0] == "5":
            cards_num[i] += 50
        elif cards[i][0] == "6":
            cards_num[i] += 60
        elif cards[i][0] == "7":
            cards_num[i] += 70
        elif cards[i][0] == "8":
            cards_num[i] += 80
        elif cards[i][0] == "9":
            cards_num[i] += 90
        elif cards[i][0] == "1":
            cards_num[i] += 100
        elif cards[i][0] == "J":
            cards_num[i] += 110
        elif cards[i][0] == "Q":
            cards_num[i] += 120
        elif cards[i][0] == "K":
            cards_num[i] += 130
        
        if cards[i][1] == "O":
            cards_num[i] += 1
        elif cards[i][1] == "E":
            cards_num[i] += 2
        elif cards[i][1] == "C":
            cards_num[i] += 3
        elif cards[i][1] == "P":
            cards_num[i] += 4
        elif cards[i][2] == "O":
            cards_num[i] += 1
        elif cards[i][2] == "E":
            cards_num[i] += 2
        elif cards[i][2] == "C":
            cards_num[i] += 3
        elif cards[i][2] == "P":
            cards_num[i] += 4
    return cards_num

def transform_num_to_cards(cards_num):
    '''
    Gets a list of card ints information and transforms it into a list of list with its number (A to K)
    and suit (O, E, C, P).
    '''
    cards = [[0, 0] for x in range(len(cards_num))]
    for i in range(len(cards_num)):
        if cards_num[i] > 130:
            cards[i][0] = "K"
            cards_num[i] -= 130
        elif cards_num[i] > 120:
            cards[i][0] = "Q"
            cards_num[i] -= 120
        elif cards_num[i] > 110:
            cards[i][0] = "J"
            cards_num[i] -= 110
        elif cards_num[i] > 100:
            cards[i][0] = "10"
            cards_num[i] -= 100
        elif cards_num[i] > 90:
            cards[i][0] = "9"
            cards_num[i] -= 90
        elif cards_num[i] > 80:
            cards[i][0] = "8"
            cards_num[i] -= 80
        elif cards_num[i] > 70:
            cards[i][0] = "7"
            cards_num[i] -= 70
        elif cards_num[i] > 60:
            cards[i][0] = "6"
            cards_num[i] -= 60
        elif cards_num[i] > 50:
            cards[i][0] = "5"
            cards_num[i] -= 50
        elif cards_num[i] > 40:
            cards[i][0] = "4"
            cards_num[i] -= 40
        elif cards_num[i] > 30:
            cards[i][0] = "3"
            cards_num[i] -= 30
        elif cards_num[i] > 20:
            cards[i][0] = "2"
            cards_num[i] -= 20
        elif cards_num[i] > 10:
            cards[i][0] = "A"
            cards_num[i] -= 10

        if cards_num[i] == 1:
            cards[i][1] = "O"
        elif cards_num[i] == 2:
            cards[i][1] = "E"
        elif cards_num[i] == 3:
            cards[i][1] = "C"
        elif cards_num[i] == 4:
            cards[i][1] = "P"

    return cards

def sort_hand(cards):
    '''
    Sorts a hand of cards in decreasing order using the insert_sort function.
    '''
    cards = [list(x) for x in cards]
    for i in range(len(cards)):
        j = []
        if len(cards[i]) == 3:
            j.append("10")
            j.append(cards[i][2])
            cards[i] = j
    cards_num = trasform_cards_to_num(hand)
    insert_sort(cards_num)
    return cards_num

def print_gamestate(player_cards, pile_cards):
    '''
    Prints the current gamestate into the console.
    '''
    for i in range(len(player_cards)):
        player_cards[i] = transform_num_to_cards(player_cards[i])
        player_cards[i] = ["".join(x) for x in player_cards[i]]
        print("Jogador ", i + 1, sep="")
        print("Mão:", *player_cards[i])
        player_cards[i] = trasform_cards_to_num(player_cards[i])
    print("Pilha:", *pile_cards)
    return None

def get_lowest(cards, min):
    '''
    Gets the lowest card in a hand using the binary_search function.
    '''
    cards_10 = cards.copy()
    for i in range(len(cards_10)):
        cards_10[i] = cards_10[i] // 10
    for i in range(1, 14):
        result = binary_search(cards_10, i)
        if result != -1 and cards_10[result] >= min:
            return cards_10[result]
    return -1

def print_pile(pile):
    '''
    Prints the cards currently in the pile into the console.
    '''
    pile_ = []
    for i in pile:
        pile_.append(i[0])
    pile_ = transform_num_to_cards(pile_)
    pile_ = ["".join(x) for x in pile_]
    print("Pilha:", *pile_)
    pile_ = trasform_cards_to_num(pile_)
    return None

if __name__ == "__main__":
    #Initial gamestate
    N_players = int(input())
    player_hands = []
    for i in range(N_players):
        hand = input().split(", ")
        hand = sort_hand(hand)
        player_hands.append(hand)
    bluff_timer = int(input())
    pile = []
    print_gamestate(player_hands, pile)

    #Game begins
    winner = -1
    current_player = 0
    min_card = 1
    round = 1
    bluffed = 0
    while winner == -1:
        #check the hands for the lowest card to discard or bluff
        if player_hands[current_player][0] // 10 >= min_card:
            count = 0
            lowest = get_lowest(player_hands[current_player], min_card)
            for i in range(len(player_hands[current_player]) - 1, -1, -1):
                if player_hands[current_player][i] // 10 == lowest:
                    discard = player_hands[current_player][i]
                    min_card = player_hands[current_player][i] // 10
                    pile.append([player_hands[current_player][i]])
                    player_hands[current_player].pop(i)
                    count += 1
                    discard = transform_num_to_cards([discard])
            print("[Jogador ", current_player + 1, "] ", count, " carta(s) ", discard[0][0], sep="")
            print_pile(pile)
        else:
            bluffed = 1
            count = 0
            lowest = get_lowest(player_hands[current_player], 1)
            for i in range(len(player_hands[current_player]) - 1, -1, -1):
                if player_hands[current_player][i] // 10 == lowest:
                    pile.append([player_hands[current_player][i]])
                    player_hands[current_player].pop(i)
                    count += 1
            print("[Jogador ", current_player + 1, "] ", count, " carta(s) ", discard[0][0], sep="")
            print_pile(pile)
        
        #timer to call the bluff
        if round % bluff_timer == 0:
            if bluffed == 1:
                for x in pile:
                    player_hands[current_player].append(*x)
                pile.clear()
                insert_sort(player_hands[current_player])
            else:
                for x in pile:
                    player_hands[(current_player + 1) % N_players].append(*x)
                pile.clear()
                insert_sort(player_hands[(current_player + 1) % N_players])
            print("Jogador", (current_player + 1) % N_players + 1, "duvidou.")
            print_gamestate(player_hands, pile)
            min_card = 1
        bluffed = 0
        
        #checking if the game is over
        if len(player_hands[current_player]) == 0:
            winner = 1
            print("Jogador", current_player + 1, "é o vencedor!")

        #reseting the player count
        if current_player + 1 == N_players:
            current_player = -1

        current_player += 1
        round += 1