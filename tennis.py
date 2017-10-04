import sys
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("text", default="input.txt", action='store_true')
# t = parser.parse_args().text
# print(t)
# print(t is bool)
# print(isinstance(t, bool))
if len(sys.argv) > 1:
    input = sys.argv[1]
else:
    input = "input.txt"

scoreArr = [0, 15, 30, 40]

def score(a, b, win):
    if a > 3 and a - b >= 2:
        print('A: WIN')
        return True
    elif b > 3 and b - a >=2:
        print('B: WIN')
        return True
    elif a > 3 and b> 3 and a==b:
        print(win + ': ADV')
        print('DUCE')
    elif a >= 4 and win == 'A':
        print('A: ADV')
    elif b >= 4 and win =='B':
        print('B: ADV')
    elif win == 'A':
        print('A: ' + str(scoreArr[a]))
    elif win == 'B':
        print('B: ' + str(scoreArr[b]))
    if a == b == 3:
        print('DUCE')

try:
    with open(input, 'r') as input:
        for games in input:
            a = b = 0
            game = games.rstrip().split(":")
            print(game[0]) # Game X
            win = game[1].split(" ")
            for winner in win:
                if winner == 'A':
                    a = a + 1
                elif winner == 'B':
                    b = b + 1
                if(score(a, b, winner)):
                    break
            print('\n')
except IOError:
    print("Error %s file not found." % input)
