import re


def firstLastDigitNumber(string):
    pairs = re.findall('\d', string)
    if len(pairs) > 0: return int(pairs[0] + pairs[-1])
    else: return 0


fileName = 'input'
filePath = fileName + '.txt'
calibrationSum = 0

with open(filePath, 'r') as f:
    for line in f:
        calibrationSum += firstLastDigitNumber(line)
        
        
print(calibrationSum)