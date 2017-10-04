# Read input.txt file
# f = open("input.txt","r")
#
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
#
# input = f.readline()
# # while input != '':
# #     print(input)
scoreArr = [0, 15, 30, 40]

def score(a, b, win):
    if a > 3 and a - b >= 2:
        print('A: WIN')
    elif b > 3 and b - a >=2:
        print('B: WIN')
    elif a > 3 and b> 3 and a==b:
        print(win + ': ADV')
        print('DUCE')
    elif a >= 4 and win == 'A':
        print('A: ADV')
    elif b >= 4 and win =='B':
        print('B: ADB')
    elif win == 'A':
        print('A: ' + str(scoreArr[a]))
        if a==b:
            print('DUCE')
    elif win == 'B':
        print('B: ' + str(scoreArr[b]))
    if a == b == 3:
        print('DUCE +++ ')


with open('input.txt', 'r') as input:
    for games in input:
        a = b = 0
        game = games.rstrip().split(":")
        print(game[0]) # Game X
        win = game[1].split(" ")
        for winner in win:
            if winner == 'A':
                a = a + 1
                score(a, b, winner)
            elif winner == 'B':
                b = b + 1
                score(a, b, winner)
