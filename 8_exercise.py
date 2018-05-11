elso= input("Első szó: ")
masodik= input("Második szó: ")

kozos=[]
for i in range(0,len(elso)):
    for j in range(0,len(masodik)):
        if elso[i] == masodik[j] :
            kozos.append(masodik[j])

vegso=""
for i in kozos:
    if i not in vegso:
        vegso+=i

print(vegso)
