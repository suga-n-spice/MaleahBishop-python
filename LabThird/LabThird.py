from random import randint


def main():
    school()
    yearsInschool()
    answer = input('what city are you from?')
    city(answer)
    randomNumber()
    areabox()

def school():
    print('Bellarmine')
    print('History')

def yearsInschool():
    print('What grade are you in?')
    grade = input()
    years = (int(grade) + 1)
    print(years)


def city(myanswer):
    print(myanswer)
    yourCity = input()
    print(yourCity)

def randomNumber():
    x = input('what is a number-?')
    y = input('what is another number?')
    myNumber = randint(int(x),int(y))
    print(myNumber)

def areabox():
   w = input('what is the length?-')
   z = input('what is the width?-')
   area = (float(int(w)) * float(int(z)))
   print(area)
   perimeter = str((int(w) * float(2)) + (int(z) * float(2)))
   print(perimeter)






main()




