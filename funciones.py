import Operaciones
repetir = "si"

while repetir[0].lower() == "s":
    num1 = float(input("ingrese un numero: "))
    num2 = float(input("ingrese otro numero: "))
    oper = str(input(f"ingrese una opcion:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n"))
    
    if oper=="1" or oper.lower()=="suma":
        print(f"el resutado es {Operaciones.sumar(num1,num2)}")
    elif oper=="2" or oper.lower()=="resta":
        print(f"el resutado es {Operaciones.restar(num1,num2)}")
    elif oper=="3" or oper.lower()=="multiplicacion":
        print(f"el resutado es {Operaciones.multiplicar(num1,num2)}")
    elif oper=="4" or oper.lower()=="division":
        print(f"el resutado es {Operaciones.dividir(num1,num2)}")
    else:
        print("ERROR, \n Volver a digitar operacion")
        oper = str(input(f"ingrese una opcion:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n"))
        if oper=="1" or oper.lower()=="suma":
            print(f"el resutado es {Operaciones.sumar(num1,num2)}")
        elif oper=="2" or oper.lower()=="resta":
            print(f"el resutado es {Operaciones.restar(num1,num2)}")
        elif oper=="3" or oper.lower()=="multiplicacion":
            print(f"el resutado es {Operaciones.multiplicar(num1,num2)}")
        elif oper=="4" or oper.lower()=="division":
            print(f"el resutado es {Operaciones.dividir(num1,num2)}")   
        
    
    
    repetir = str(input("desea hacer otra operacion: "))