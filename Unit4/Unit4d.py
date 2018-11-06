def main():
    shoppingCart = [['tooth paste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    bigList = allInone(shoppingCart)
    countQtips(bigList)
    drinkMoreMilk(shoppingCart)
    mooseCookie(shoppingCart)

def allInone(myShoppingcart):
    bigList = []
    for list in myShoppingcart:
        for item in list:
            bigList.append(item)
    return bigList

def countQtips(biglist):
    count = 0
    for item in biglist:
        if item == 'q-tips':
            count += 1
    print(count)

def drinkMoreMilk(cart):
    for list in cart:
        if 'milk' not in list:
            list.append('milk')
    print(cart)

def mooseCookie(shopping):
    for list in shopping:
        if 'milk' in list:
            list.remove('milk')
            list.append('milk and cookies')
    print(shopping)

main()
