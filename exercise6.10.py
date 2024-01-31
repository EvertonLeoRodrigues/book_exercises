#Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor
#v que também será procurado. Na impressão, indique qual dos dois valores foi achado 
#primeiro.

while(True):
    L=[15,7,27,39]
    p = int(input("Enter the value to search for or \"0\" for exit: "))
    v = int(input("Enter another value to search or \"0\" for exit: "))

    if(p==0 or v==0):
        break
    x = 0
    foundP = False
    foundV = False
    foundAll = False
    positionP = 0
    positionv = 0

    while(x<len(L)):
        if(L[x]==p):
            foundP=True
            positionP = L[x]
        elif(L[x]==v):
            foundV=True
            positionV = L[x]
        x+=1

    if(foundP and foundV):
            print(f"The value {p} and {v} is found at position respectively {positionP} and {positionV}!")
    elif(foundP):
        print(f"Only the value {p} was found at position {positionP}!")
    elif(foundV):
        print(f"Only the value {v} was found at position {positionV}!")
    else:
        print(f"No value was found!")