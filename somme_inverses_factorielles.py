def e(n):
    i = 0
    e = 0
    while i != n:
        e += 1/factorielle(i)
        i += 1
    print(e)

def factorielle(i):
    if i == 0:
        return 1
    return i*factorielle(i-1)
    
    
    
