def convert(lista,b1,b2):
    szam=0
    helyiertek=1
    for i in range(len(lista)-1,-1,-1):
        if lista[i]>=b1:
            print("Nem jó szám")
            return None
        szam+=lista[i]*helyiertek
        helyiertek*=b1
    lista2=[]
    while szam!=0:
        lista2.append(szam%b2)
        szam//=b2
    lista2.reverse()
    return lista2
print(convert([6,7,4],10,2))
