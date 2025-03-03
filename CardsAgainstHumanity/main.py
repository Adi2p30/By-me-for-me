import random
def setup():
    black_cards_text = open("black.txt", 'r')
    black_cards = []
    for line in black_cards_text:
        black_cards.append(line[:-1])

    white_cards_text = open("white.txt", 'r')
    white_cards = []
    for line in white_cards_text:
        white_cards.append(line[:-1])
    return white_cards, black_cards

def shuffle(deck, seed=1):
    random.seed(seed)
    random.shuffle(deck)
    return deck

def main():
    white_cards, black_cards = setup()
    print("Welcome to Cards Against Humanity Online! [CLI]")
    playersno = int(input("How many players are there? "))
    players = {}
    for i in range(playersno):
        tempname = input(f"Name of Player {i+1}: ")
        players[tempname] = {"white_cards":[], "black_cards":[]}
    leader = list(players.keys())[0]
    seed = int(input("Tell me the shuffle seed: "))
    white_cards = shuffle(white_cards, seed)
    you = input("Who are you? ")
    currcount = 0
    for i in players.keys():
        players[i]["white_cards"]= white_cards[currcount*5:(currcount+1)*5]
        currcount += 1
    white_cards = white_cards[currcount+1*5:]
    print(players)
    random.seed = seed
    nextround(you, players, leader)

def nextround(you, players, winner):
    leader = winner
    curr_blackcard_index = random.randint(0, 106)
    blackcard = black_cards[curr_blackcard_index]
    black_cards.pop(curr_blackcard_index)
    le
    if you == leader:
        asleader()
    else:
        asplayer(you, players, blackcard)
    print(players)
def asleader(you, players, blackcard):
    print("Wait for everyone to put forward a card")
    for i in players.keys():
        players[i]["option"] = 0
    while flag == 0:
        for i in players.keys():
            code = int(input(f"What option did {i} choose?"))
            players[i]["option"] = players[i]["white_cards"][code-1]
            # TODO: Make the code continue even in exceptions
            for j in players.keys():
                print(f"Option Chosen by {i}: {players[j]["option"]}")
                if i == 0:
                    flag = 1
    options = {}
    j = 1
    for i in random.shuffle(players.keys()):
        options[i] = players[i]["white_cards"][player[i]["option"]]
        replaced_line = str(j)+ ". " + blackcard.replace("_____", options[i])
        print(replaced_line)
        j = j+1
    chosen = int(input("Choose the best option"))
    winner = ""
    for i in players.keys():
        if players[i]["option"] == options.values()[chosen-1]:
            winner = options[i]
            break
    print(f"The winner is {winner}!")
    nextroundcode = int(str(random.randint(1,100) + str(players.keys().indexof(winner))))
    print(f"Next Round Code: {nextroundcode}")
    nextround(you, players, winner)
    #TODO: Work on the leader and how they recieve the options put forward by everyone else

def asplayer(you, players, blackcard):
    for line in range(len(players[you]["white_cards"])):
        replaced_line = blackcard.replace("_____", players[you]["white_cards"][line])
        print(f"Option {line+1}: {replaced_line}")
    chosen = int(input("Which option do you choose (number)? "))
    print(f"Send this number to the leader: {chosen}")
    nextroundcode = random.randint(0,100)
    inputtedcode = 0
    while nextroundcode != inputtedcode:
        inputtedcode = int(input("What is the next round code? "))
    winner = str(inputtedcode)[:-1]
    players[winner]["black_cards"].append(blackcard)
    nextround(you, players, winner)

def playerstats(players):
    print(players)

main()






#TODO: Add next round white card reshuffling and a new blak card to be added





