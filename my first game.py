import tiknter
def again ():
    print("do you want to play again?")
    
    print("----> Kayles Game <----")
    import random
    player= str(input("player 1 Name :"))
    x = int(input("enter the number (x) of coins:"))
    counter = 0
    gap = []
    lista = []
    i=0
    while x > 0 :
        for i in range (1,x+1) :
            gap+="_"
            lista.append(i)
            if x==len(lista):
                break
        break        

    print ("start the game :",lista)
    while lista != gap :
        if counter % 2 ==0:
            print(player,"it's your turn")
            m = int(input("how many numbers do you want to remove ? :"))
            if m == 1 :
                z = int(input("enter the number :"))
                if z not in lista or (z-1) not in lista  or (z+1) not in lista:
                    print("the number not in the list  choose another")
                    z = int(input("enter the number :"))
                
                lista[z-1]="_"
                print(lista)
                counter+=1

            elif m == 2 :
                z = int(input("enter the number:"))
                y = int(input("enter the adjacent number:"))
                if z !=(y-1) and z!=(y+1)or y not in lista:
                    print("make sure",y,"the adjacent number..")
                    z = int(input("enter the number:"))
                    y = int(input("enter the adjacent number:"))
                lista[z-1]="_"
                lista[y-1]="_"
                print(lista)
                counter =+1
            else :
                print("you just allowed to choose 1 or 2 numbers ..")
        else :
            if lista == gap :
                break
            print ("CPU's turn")
            x = random.randint(1,len(lista))
            while lista[x-1]=="_" :
                x = random.randint(1,len(lista))
            if x==1 :
                a=[-1,2]
            elif x== len(lista) :
                a = [-1,range(lista-1)]
            else :
                a = [x-1,x+1,-1]
                y=a[random.randint(0,len(a)-1)]
            if y == -1 :
                lista[x-1]="_"
                print(lista)
                counter+=1
            elif y!=-1:
                lista[x-1]="_"
                lista[y-1]="_"
                print(lista)
                counter+=1
    if counter%2==0 :
        print ("CPU is the winner")
    elif counter%2!=0 :
        print(player,"is the winner")
    
#game start from here..........
print("----> Kayles Game <----")
import random
player= str(input("player 1 Name :"))
x = int(input("enter the number (x) of coins:"))
counter = 0
gap = []
lista = []
i=0
while x > 0 :
    for i in range (1,x+1) :
        gap+="_"
        lista.append(i)
        if x==len(lista):
            break
    break        

print ("start the game :",lista)
while lista != gap :
    if counter % 2 ==0:
        
        print(player,"it's your turn")
        m = int(input("how many numbers do you want to remove ? :"))
        if m == 1 :
            z = int(input("enter the number :"))
            if z not in lista or (z-1) not in lista  or (z+1) not in lista:
                print("the number not in the list  choose another")
                z = int(input("enter the number :"))
                

            lista[z-1]="_"
            print(lista)
            counter+=1

        elif m == 2 :
            z = int(input("enter the number:"))
            y = int(input("enter the adjacent number:"))
            if z !=(y-1) and z!=(y+1):
                
                
                print("make sure",y,"the adjacent number..")
                z = int(input("enter the number:"))
                y = int(input("enter the adjacent number:"))
            lista[z-1]="_"
            lista[y-1]="_"
            print(lista)
            counter =+1
        else :
            print("you just allowed to choose 1 or 2 numbers ..")
            
    else :
        if lista == gap :
            break
        print ("CPU's turn")
        x = random.randint(1,len(lista))
        while lista[x-1]=="_" :
            x = random.randint(1,len(lista))
        if x==1 :
            a=[-1,2]
        elif x== len(lista) :
            a = [-1,range(lista-1)]
        else :
            a = [x-1,x+1,-1]
            y=a[random.randint(0,len(a)-1)]
        if y == -1 :
            lista[x-1]="_"
            print(lista)
            counter+=1
        elif y!=-1:
            lista[x-1]="_"
            lista[y-1]="_"
            print(lista)
            counter+=1
if counter%2==0 :
    print ("CPU is the winner")
elif counter%2!=0 :
    print(player,"is the winner")
again()
        
