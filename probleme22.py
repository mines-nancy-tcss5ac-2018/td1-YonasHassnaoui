def alphabet(lettre):
    res=0
    al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(al)):
        if al[i]==lettre:
            res=i+1
    return res

fichier=open('p022_names.txt','r')
for i in fichier:
    print(i)
    p=i.split(',')
    print(p)
    
def solve():
    res=0
    for k in range(len(p)):
        somme=0
        for x in p[k]:
            somme=somme+alphabet('x')
        res=res+somme*k
    return res
print(solve())