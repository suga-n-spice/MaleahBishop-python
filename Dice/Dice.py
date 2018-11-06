import random
def main():
    dicelist = diceComponents()
    rollList = []
    roll = rollDice()
    roll2 = rollDice()
    rollList.append(roll)
    rollList.append(roll2)
    print(rollList)
    printedDice = [dicelist[roll], dicelist[roll2]]
    printDice(printedDice)


def diceComponents():
    diceList=[]
    TopBottom = '---------'
    RowA = '|       |'
    RowB = '| *   * |'
    RowC = '|   *   |'
    RowD = '| *     |'
    RowE = '|     * |'
    diceList.append([TopBottom,RowA,RowC,RowA,TopBottom])
    diceList.append([TopBottom,RowD,RowA,RowE,TopBottom])
    diceList.append([TopBottom, RowD, RowC, RowE, TopBottom])
    diceList.append([TopBottom,RowB,RowA, RowB,TopBottom])
    diceList.append([TopBottom,RowB,RowC,RowB,TopBottom])
    diceList.append([TopBottom,RowB,RowB,RowB,TopBottom])
    return diceList

def rollDice():
    return random.randint(0,5)

def printDice(dice):
    # for line in dice[0]:
    #     print(line)

    for row in range(0,len(dice[0])):
        for line in range(0,len(dice)):
           print(dice[line][row],end=' ')
        print()

main()
