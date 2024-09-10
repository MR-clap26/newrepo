import random
print("hola mundo")

numrand=random.randint(1,20)
numuser=-1
contints=0
for i in range (4):
    numuser=int(input("ingrese un numero"))
    if numrand==numuser:
        print("felizidades le achuntaste")
        break

    else:
        if numrand>numuser:
            print("es mayor")
        elif numrand<numuser:
            print("es menor")
        contints+=1    
if contints==4:
    print("se te acabaron los intentos,perdiste saco wea, el numero era",numrand)