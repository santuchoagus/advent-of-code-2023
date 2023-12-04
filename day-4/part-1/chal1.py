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

score = 0
for game in games:
    winNums, yourNums = game
    commonNums = [num for num in yourNums if num in winNums]
    score += 2**(len(commonNums)-1) if len(commonNums) > 0 else 0
    
print(score)