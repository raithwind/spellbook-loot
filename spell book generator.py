import random

from spelllist_by_level import spelllist


def getmaxspell(wizlevel):
    spellarray = {}
    spelllevel = (wizlevel+1)//2
    if spelllevel == 10:
        spelllevel = 9
    for level in range(1,spelllevel + 1):
        magicmath = (1/(level/wizlevel))/1.1
        if level == 1:
            magicmath += 6
        spellarray.update({level:round(magicmath)})
    return spellarray

def getspells(number, level):
    spells = []
    for i in range(number):
        choice = random.choice(spelllist[level])
        if choice not in spells:
            spells.append(choice)
        else:
            random.choice([getspells(1,level),spells.append("Personalized {}".format(choice))])
    return spells
        
        
def spellbook(wizlevel):
    spellbook = {}
    spellarray = getmaxspell(wizlevel)
    for key in spellarray:
        value = spellarray[key]
        spellbook.update({key:getspells(value,key)})
    return(spellbook)

while True:


    lev = input("What level wizard spellbook: ")
    test = spellbook(int(lev))

    for line in test:
        print(line)
        print(", ".join(test[line]))
