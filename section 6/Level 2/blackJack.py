
def black_jack(a,b,c):
    if a+b+c <= 21:
        return a+b+c
    elif a+b+c > 21 and (a== 11 or b==11 or c==11):
        sum = (a+b+c) - 10
        if sum > 21:
            return 'BUST'
        else:
            return sum
    elif a+b+c > 21 and a!=11 and b!=11 and c!=11:
        return 'BUST'

print(black_jack(9,9,9))