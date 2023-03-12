def somme(n):
    i = 0
    somme = 0
    while i != n:
        somme += 1/factorielle(i)
        i += 1
    print(somme)

def factorielle(i):
    if i == 0:
        return 1
    return i*factorielle(i-1)
    
    
    
