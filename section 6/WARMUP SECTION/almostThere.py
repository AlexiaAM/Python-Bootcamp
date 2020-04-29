
def almost_there(n):
    if abs(n-10) <= 10 or abs(n-100) <=10 or abs(n-200) <=10:
        return True
    else:
        return False

print(almost_there(140))