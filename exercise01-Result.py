basedatos= []
totalCostos= 0
continuar =1
while continuar>=0:
        cliente = input('nombre del cliente:')
        producto = input('producto: ')
        costo = float(input('costo ($0.00):'))
        totalCostos +=costo
        registro= {'cliente':cliente, 'producto':producto, 'costo': costo}
#agregando a una lista
        basedatos.append(registro)

        print('Para seguir añadiendo datos presione ¨a¨')
        print('Cualquier otro carácter se tomará como detener')
        caracter= input()
        if caracter == ('a'):
            continuar+=1
        else: 
            breakpoint
            print ('Costo total es')
            print (totalCostos)
            for registro in basedatos:
                print(registro)
