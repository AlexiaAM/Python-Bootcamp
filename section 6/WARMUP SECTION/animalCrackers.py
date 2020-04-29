

def animal_craker(phrase):
    x = phrase.split(' ')
    if x[0][0] == x[1][0]:
        return True
    else:
        return False

print(animal_craker('Levelheaded Llama'))
print(animal_craker('a o'))