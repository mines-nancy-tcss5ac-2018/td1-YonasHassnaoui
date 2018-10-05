def solve(n):
    somme=0
    k=0
    while 2**n<10**k:                   #on identifie la puissance de la plus grande décimale
        k=k+1
    nombre=2**n
    for i in range(1,k+1):               
        dec=int(nombre/10**(k-i))        #on divise par les puissances de 10 succesives entrer 0 et la plus grande
        print(dec)
        somme=somme+dec                  #on ajoute la décimale obtenue
        nombre=nombre-dec*10**(k-i)      #on enlève la plus grande décimale
    return somme
assert(solve(10)==23)
print(solve(1000))


def solvecor(n):
    res=0
    while n !=0:
        r+=n%10
        n=n//10
    return r