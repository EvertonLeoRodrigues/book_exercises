#Escrever o programa 6.9 de exemplo sem a variável "found".
while(True):
    L=[15,7,27,39]
    p = int(input("Enter the value to search for or \"0\" for exit: "))
    if(p==0):
        break
    x = 0

    while(x<len(L)):
        if(L[x]==p):
            break
        x+=1
    if(x<len(L)):
        print(f"{p} found at position {x}")
    else:
        print(f"{p} is not found")