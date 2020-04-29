
def old_Macdonalds(name):
    newName = ''
    for i in range (0,len(name)):
        if i == 0 or i == 3:
            newName = newName + name[i].capitalize()
        else:
            newName = newName + name[i]
    return newName

print(old_Macdonalds('macdonalds'))

