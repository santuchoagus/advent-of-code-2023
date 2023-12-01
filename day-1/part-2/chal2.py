import re

pairs = {
        'zero':'0','one':'1','two':'2','three':'3','four':'4',
        'five':'5','six':'6','seven':'7','eight':'8','nine':'9'
    }

numbers = 'one|two|three|four|five|six|seven|eight|nine'

fileName = 'input'
filePath = fileName + '.txt'
calibrationSum = 0

with open(filePath, 'r') as f:
    for line in f:
        line_digits = re.findall(r'(?=(\d|{}))'.format(numbers), line)
        digit_list = [pairs.get(digit) if digit in pairs.keys() else digit for digit in line_digits]

        if len(digit_list) > 0:
            value = int(digit_list[0] + digit_list[-1])
        else:
            value = 0
    
        calibrationSum += value


print(calibrationSum)