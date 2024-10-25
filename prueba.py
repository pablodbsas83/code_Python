def modificar(listaProductos):
    i=0
    no_se_encontro=True					#Bandera que indica si No se encontró el producto
    op=''
    os.system("clear")                   #borra la pantalla en linux, en win cambiar "clear" por "cls"
    print("***MODIFICAR PRODUCTO***\n")
    producto=input("Ingrese el nombre del producto: ")
    while op!='n':
        while i < len(listaProductos):
            if producto == listaProductos[i][0]:
                print("\n PRODUCTO ENCONTRADO")
                print(f"PRODUCTO: {listaProductos[i][0]}\tSTOCK: {listaProductos[i][1]}")
                no_se_encontro=False		#Si lo encuentra pasa a FALSO la bandera NO ENCONTRADO
                print("Ingrese la Opción deseada")
                opcion=input("Desea modificar:\n Articulo: A \n Stock: S\nCancelar: C").lower()
                if opcion == 'a':
                    listaProductos[i][0]=input("Nuevo Nombre de Articulo")
                if opcion== 's':
                    listaProductos[i][1]=input("Nuevo Stock de Articulo")
                if opcion=='c':
                    print("Sin Cambios\n")
            input("Presione Enter para seguir ")
            break									#Rompe el ciclo
            i+=1

    if no_se_encontro:						#Si NO encontró el producto lo indica ya que no=True
        print(f"Producto: {producto} NO hallado")
    op=input("Desea buscar otro producto? S/N ").lower() #pregunta si quiero buscar otro producto
    if op=='s':
        os.system("clear")                   #borra la pantalla en linux, en win cambiar "clear" por "cls"
        print("***MODIFICAR PRODUCTO***\n")
        producto=input("Ingrese el nombre del producto: ")
        i=0								#resetea el indice
        no_se_encontro=True							#pasa a True por si no encuentra la nueva busqueda
        input("\nPresione enter para continuar")
    return 0
