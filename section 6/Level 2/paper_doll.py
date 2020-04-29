
def paper_doll(mystring):
    newString = ''
    for i in range(0,len(mystring)):
        for j in range(0,3):
            newString = newString + mystring[i]
    return newString

print(paper_doll('Mississippi'))

