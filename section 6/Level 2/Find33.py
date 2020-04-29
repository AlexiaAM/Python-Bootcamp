

def has_33(mylist):
    for i in range(0,len(mylist)-1):
        contiene_33 = False
        if mylist[i] == 3 and mylist[i+1] == 3 and contiene_33 == False :
            contiene_33 = True
    return contiene_33

print(has_33([1,2,3,4,5,3,3]))
