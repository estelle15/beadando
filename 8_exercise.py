elso= input("Első szó: ")
masodik= input("Második szó: ")

kozos=[]
for i in range(0,len(first)):
    for j in range(0,len(second)):
        if first[i] == second[j] :
            kozos.append(second[j])

vegso=""
for i in kozos:
    if i not in vegso:
        vegso+=i

print(vegso)
