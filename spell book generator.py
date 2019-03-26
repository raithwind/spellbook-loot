import random
from spelllist_by_level import spelllist


def get_max_spell(wizlevel):
    """ determine the highest level spells a wizard of level wizlevel would have access to"""
    spellarray = {}
    spelllevel = (wizlevel+1)//2
    #accounts for highest spell level being 9, not 10
    if spelllevel == 10:
        spelllevel = 9
    for level in range(1,spelllevel + 1):
        #magicmath determines the number of spells per level a wizard of level wizlevel would likely have, and accounts 
        #for the wizard level progression and learning spells as they adventure etc
        magicmath = (1/(level/wizlevel))/1.1
        #a wizard starts with 6 level 1 spells, this is taken care of here
        if level == 1:
            magicmath += 6
        spellarray.update({level:round(magicmath)})
    return spellarray

def get_spells(number, level):
    """ return a list of spells, length number, of spell level level"""
    spells = []
    for i in range(number):
        choice = random.choice(spelllist[level])
        try:
            assert choice not in spells
        except AssertionError:
            while choice in spells:
                if random.randint(1,2) == 1 and "{} PERSONAL".format(choice) in spells:
                    choice = random.choice(spelllist[level])
                else:
                    choice = "{} PERSONAL".format(choice)
        spells.append(choice)
    return sorted(spells)
        
        
def get_spellbook(wizlevel):
    """generate the actual spellbook"""
    spellbook = {}
    spellarray = get_max_spell(wizlevel)
    for key in spellarray:
        value = spellarray[key]
        spellbook.update({key:get_spells(value,key)})
    return(spellbook)

while True:
    lev = input("What level wizard spellbook: ")
    test = get_spellbook(int(lev))
    for line in test:
        print("Level {} spells:".format(line))
        print(", ".join(test[line]))
