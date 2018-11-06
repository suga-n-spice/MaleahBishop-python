
for i in range(1,6):
    add = i + 10
    print(str(i) + ' + 10 =' + str(add))
    product = i * 10
    print(str(i) + ' * 10 =' + str(product))

list = [10, 20, 30, 40, 50]
print(list)
for x in range(0,len(list)):
    y = list[x] * 10
    list[x] = y
    print(x)
print(list)

