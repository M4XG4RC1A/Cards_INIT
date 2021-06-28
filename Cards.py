import random

class Card:
    def __init__(self,Type = 0,Value = 0):
        self.Type = Type
        self.Value = Value

Translate = {1:'♢',2:'♣',3:'♤',4:'♥'}
TranslateVal = {1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
Types = list(range(1,5))
Values = list(range(1,14))
Cards = []
UsedCards = []

print("Let's play 21, the rules for this game are simple\n1. We start with 2 cards\n2. Try to reach 21\n3. if you have more than 21 you lose\n4. Win who is closest to 21\nA=1, J=11, Q=12, K=13\nHave Fun :)\n")

for t in Types:
    for v in Values:
        Cards.append(Card(t,v))

NPlayers = 2
NCards = 2

Players = []
PlayerState = []

for p in range(1,NPlayers+1):
    PCards = []
    for c in range(1,NCards+1):
        RCard = random.randint(0,len(Cards)-1)
        while RCard in UsedCards:
            RCard = random.randint(0,len(Cards)-1)
        UsedCards.append(RCard)
        PCards.append(Cards[RCard])
    Players.append(PCards)
    PlayerState.append('Ok')

EndGame = False
EndPlayers = 0
while not(EndGame):
    for p in range(0,len(Players)):
        if PlayerState[p] == 'Ok':
            print("\nPlayer {} is your turn".format(str(p+1)))
            print("Your Cards:")
            for c in Players[p]:
                print("{}{}".format(Translate[c.Type],str(TranslateVal[c.Value])))
            other = input("Your want other card?")
            while not(other == 'N' or other == 'Y'):
                other = input("Your want other card?")
            if other == 'Y':
                RCard = random.randint(0,len(Cards)-1)
                while RCard in UsedCards:
                    RCard = random.randint(0,len(Cards)-1)
                UsedCards.append(RCard)
                Players[p].append(Cards[RCard])
                print("{}{}".format(Translate[Cards[RCard].Type],str(TranslateVal[Cards[RCard].Value])))
            else:
                PlayerState[p] = 'End'
                EndPlayers = EndPlayers+1
            if EndPlayers >= len(Players) or len(UsedCards) == len(Cards):
                EndGame = True

print("\nGame End...")
lastBig = 0
winner = []
actual = 0
for play in Players:
    actual = actual+1
    sum = 0
    for c in play:
        sum = sum+c.Value
    print("Player {}, reach {} points".format(str(actual),str(sum)))
    if sum > lastBig and sum<=21:
        winner = [actual]
        lastBig = sum
    elif sum == lastBig:
        winner.append(actual)
if len(winner) > 1:
    stringWin = ""
    for w in winner:
        stringWin = stringWin+str(w)+","
    stringWin = stringWin[0:-1]
    print("Theres a tie between {}".format(stringWin))
else:
    if lastBig == 0:
        print("Players Lose")
    else:
        print("The winner is player {}".format(str(winner[0])))
