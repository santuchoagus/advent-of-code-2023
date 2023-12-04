import re

filepath = 'input.txt'
lines = list()

f = open(filepath)
games = list()
for line in f:
    winNums, yourNums = re.sub(r'Card.*: ','', line).split('|')
    winNumsArr = [int(n) for n in re.findall(r'\d+', winNums)]
    yourNumsArr = [int(n) for n in re.findall(r'\d+', yourNums)]
    games.append((winNumsArr, yourNumsArr))
    
cards = dict()
for gameNum, game in enumerate(games):
    winNums, yourNums = game
    commonNums = [num for num in yourNums if num in winNums]
    cards[gameNum+1] = [len(commonNums), 1]   
   
cardCount = 0
for k, (v, copies) in cards.items():
    cardCount += copies
    for i in range(1,v+1):
        if(k+i in cards.keys()):
            cards[k+i][1] += 1*copies
        
print(cardCount)