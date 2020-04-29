def lesser(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    elif a%2!=0 or b%2!=0:
        return max(a,b)

print(lesser(2,3))