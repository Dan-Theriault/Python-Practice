import random

white_pot = range(69)
for ball in white_pot:
    ball += 1
red_pot = range(25)
for ball in red_pot:
    ball += 1

def draw():
    nums = []
    powerball = -1
    white_pot_temp = list(white_pot) 
    red_pot_temp = list(red_pot)
    random.shuffle(white_pot_temp)
    random.shuffle(red_pot_temp)
    for j in range(5):
        nums.append(white_pot_temp.pop())
    powerball = red_pot_temp.pop()

    temp_nums = []
    for num in nums:
        num = str(num)
        if len(num) < 2:
            num = '0'+num
        temp_nums.append(num)
    nums = temp_nums
    del temp_nums

    powerball = str(powerball)
    if len(powerball) < 2:
        powerball = '0'+powerball
    return [nums, powerball]

if __name__ == '__main__':
    import sys
    tickets = []
    try:
        for i in range(int(sys.argv[1])):
            tickets.append(draw())
    except(IndexError):
        tickets.append(draw())

    for tick in tickets:
        for num in tick[0]:
            print(num, end = ' ')
        print(tick[1])


        


