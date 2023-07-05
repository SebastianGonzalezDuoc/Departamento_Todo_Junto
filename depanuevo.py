import numpy as np

edificio=np.empty((10,4),object)
dueños={} #para almacenar información sobre los dueños de los departamentos.
print(edificio)
while True:
    print("""
    1) Ver edificio
    2) Comprar edificio
    3) Buscar Dueño
    4) Total ganancias
    5) Salir
    """)
    opcion=int(input("Ingrese una opcion:"))
    if opcion==1:
        print("Ver edificio")
        nro_piso=11 #Esta variable se utilizará para mostrar el número de piso mientras se itera sobre ellos.
        print("\t    A   B   C   D")
        for piso in range(10,0,-1): # itera desde 10 hasta 1 en orden descendente, iterando sobre cada piso del edificio.
            nro_piso-=1 #Resta 1 a nro_piso en cada iteración para actualizar el número de piso que se muestra.
            print(f"Nro Piso:{nro_piso}",end=" ") #Imprime piso actual / End añade espacio despues del cuadrado
            for letra in range (4):#: itera desde 0 hasta 3, representa A, B, C y D
                if edificio[piso-1,letra]==None:
                    print("🟩",end=" ")
                else:
                    print("🟥",end=" ")
            print(" ") # Imprime un espacio en blanco al final de cada línea para separar los pisos.
        print("Los departamentos de los pisos del 10 al 8 tienen un valor de 200 millones.")
        print("Los departamentos de los pisos del 1 al 7 tienen un valor de 150 millones.")

        print("Disponible=🟩")
        print("Vendido=🟥")
    elif opcion==2:
        pass
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        break
    else:
        print("Has ingresado una opcion no valida")
