def main():
    draw7()
    starsAndStripes()
    list = [1,2,3,4,5,6,7]
    incTriangle(list)

def draw7():
    stars = ''
    for x in range(0,7):
        for y in range(0,7):
            print('*', end="")
        print()

def starsAndStripes():
    dash = ''
    star = ''
    for m in range(0,3):
        for i in range(0, 7):
            print('*', end='')
        print()
        for x in range(0, 7):
            print('-', end='')
        print()

def incTriangle(anotherlist):
    for k in range(1,8):
        string = ''
        for w in range(0,k):
            string+= str(k)
        print(string)

main()
