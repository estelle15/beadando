def convert(lista,b1,b2):
    szam=0
    helyiertek=1
    for i in range(len(lista)-1,-1,-1):
        if lista[i]>=b1:
            return None
        szam+=lista[i]*helyiertek
        helyiertek*=b1
    lista2=[]
    while szam!=0:
        lista2.append(szam%b2)
        szam//=b2
    lista2.reverse()
    return lista2
print(convert([0,1,1,0,0,1,1],2,10)) #[5,1]
print(convert([5,7,2],10,3))#[2,1,0,0,1,2]
print(convert([9,5,4,4],10,16))#[2,5,4,8]
