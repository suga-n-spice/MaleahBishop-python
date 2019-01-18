import time
#possible answers from the user
answerA = ['A','a']
answerB = ['B','b']
answerC = ['C','c']
Yes = ['Yes','Y','y','yes']
No = ['No','n','N','no']


def intro():
    print("You wake up in a clearing of trees. It is high noon and the sun is shining overhead. The clearing you find yourself in is grassy. \nThe grass is tall and rustles with wind and the occasional rodent passing. The clearing is surrounded by ancient Ironwood trees.")
    print()
    print('You have no recollection of how you came to be in this place or where -this- place is, you are not even sure of who you are.'
          ' But you notice the sun hanging in the sky and feel vulnerable out in the open, \n what do you do  next?')
    print()
    print('Instructions Part 1 \n You were just given a scenario, this game is filled with scenarios which proceeding them you will be offered a selection of choices being - A, B, C-'' \n You will then be prompted to type your response, by typing your selection by either a single capital or lowercase letter corresponding to you choice.')

    print('A. Venture into the forest and search for shelter and food.')
    print('B. Search for civilization, there has to be some right?')
    print('C.Try and climb a tree to get a vantage point')
    choice = input('What do you want to do?' + '_____') #whereuser inputs a letter answer
    if choice in answerA:
        option1()
    elif choice in answerB:
        option2()
    elif choice in answerC:
        option3()
    else:
        print('Ошибка: пожалуйста попробуйте еще раз')

def option1():
    print('You start exploring the forest and find there are plenty of fallen Ironwood branches and from what looks to be a recent storm \n-Ironwood trees are very sturdy trees, only a large storm could have fallen this many branches-You are able to craft a half decent shelter with the branches and a knife you found '
          'on your belt in a sheath.')
    print('Next you must search for food, how do you intend on finding food? \n A. Searching the native flora for wild berries, mushrooms and the like.\n  B. Try to hunt and look for game. \n C. Go looking for a water source and fish.' )
    choice2 = input('What do you want to do?' + '_____')
    if choice2 in answerA:
        option1a()
    elif choice2 in answerB:
        option1b()
    elif choice2 in answerC:
        option1c()
    else:
        print('Ошибка: пожалуйста попробуйте еще раз')


def option2():
    print('You decide that finding civilization is the best way to find answers. After all, you are not sure of anything, much less who you are. \n You do not go into the forest but go to the edge so you are not in the complete open. Pretty soon the flat grassy plain becomes rocky. The clearing opens up to a vast rocky plain '
          'that is leagues long and wide. Large monoliths are scattered, ranging in sizes and shapes. \n Though clearly naturally formed, some have odd carvings that could be ritualistic or symbolic. Painted in these carvings are three colors of a pigment. An aqua blue that almost seems to glow, a deep blood red and a black.')
    print('At least a couple miles from where you started, the clearing has opened up to a valley tha leads to the foot of a mountain. The grass is no longer waist and shoulder height, but patchy and short. \n A few of the rocks you have passed have shelves carved into them. '
          'Inside of them blue flames provide light for these make shift lamps. At last a sign of life. The stone lamps increase in number and soon outline a wide path.\n The sun is setting to your left and paints the valley and mountain is gold and amber tones.'
          'You see what looks to be a wall or siding of some garrison or structure. Smoke rises from within the confines. Only several hundred yards away, you silently thank whatever Gods there are.')
    print('But your relief is short lived because while the light of the sun diminished you were being watched. You hear something that makes you freeze. Behind you 100 yards, wolves reveal come out from behind some rocks. \n '
          'You have not had anything to eat or drink all day, and you only have a knife. Added to that there are five of them and only one of you. You think if you run fast you may be able to make it to the wall.')
    FightorFlight = input('What do you do? A. Run for your life? \n B. Stay and fight')
    if FightorFlight in answerA:
        fight()
    elif FightorFlight in answerB:
        flight()
    else:
        print('Ошибка: пожалуйста попробуйте еще раз')


def option3():
    print('There are plenty of trees to climb. Though there are few low hanging branches, you manage to grab onto a knot and lift yourself up to a branch. The branches are thick and you keep climbing'
          'Once at the top you see the clearing is more than a clearing. It is a valley.')
    print()
    print('Past where you woke up to the North, the grassy plain turns rocky and large monoliths are scattered casting shadows. It opens up further and the forest thins as the topography changes.\n The rocky valley turns into a summit at the base of a mountain.')
    print()
    print('To the West, the forest goes on and on.')
    print()
    print('Though you can not see it, you can smell ocean salt from the South. All you see is more trees, but a breeze carries the salinated air')
    print('')

def option1a():
    print('You search for berries and mushrooms or some sort of edile plant. But with no knowledge of the land, you are not sure where to look. \n Using your best judgment you gather it is sprin, so there should be new growth.')
    print('You spot a badger eating some berries on a bush. If he is eating them they are likely safe to eat.')
    YandN = input('Do you try the berries? Yes or No')
    if YandN in Yes:
        print('You eat the berries after watching the badger. You feel fine at first but soon your stomach turns and your body starts convulsing. \n The badger has a thick resilient stomach lining and special enzymes that allow him to digest things like venomous animals and berries.')
    elif YandN in No:
        death()
    else:
        print('Ошибка: пожалуйста попробуйте еще раз')

def option1b():
    print('You know that there are small rodents that live in burrows hidden by the tall grass. But you know you are not likely to kill or catch a small target in a field with lots of escape routes \n Your weapons, only a large dagger like knife, limits you unless you fashion another weapon or a trap.')
    print('You sneak up on some odd forest rodent you do not recognize and kill it. Though you do not recall anything specific about yourself or your surroundings, you easily dress the animal. \n While doing so you notice your knife has characters engraved on the blade they read')
    Name = input('What is your name?' + '________')
    print(Name + 'is engraved on the blade, it means something, it is a name, but is it yours?')

def option1c():
    print('Going what you gather to be North or West or somewhere in between there, you find the a river with soliciting water fowl. Finding fresh water is a relief and you drink and splash some on your face.'
          'It is evident that it is spring time. since you have been awake you have been noting details about your surroundings to try and agitate some memory. \n Fish are swimming up stream to spawn and after watching some of the fowl snatch fish from the water, you learn and catch several fish of your own.')
def death():
    print('You died')

def fight():
    print()

def flight():
    print()


intro()
