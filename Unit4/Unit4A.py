def main():
    horsebreeds = ('American Pharoah')
    print(horsebreeds)
    print(deVowel(horsebreeds))
    number = [1, 2, 3]
    print(mathStuff(number,9))


def deVowel(tripleCrown):
    newWord = tripleCrown
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for x in tripleCrown:
        if x in vowels:
            newWord = newWord.replace(x,"")

    return newWord

def mathStuff(num, mult):
    for i in range(len(num)):
        num[i] *= mult
    return num

main()
