#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  proyecto_v3.py
#  
#  Copyright 2024 Pablo Toledo <pablodbsas83@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import os			#importa la libreria OS para usar el comando del sistema operativo "borrar pantalla"
def inicio():					#Muestra un mensaje al inicio
	marco="*"
	titulo="PROYECTO FINAL PRE-ENTREGA"
	print("\t"+marco*len(titulo))	
	print("\t"+titulo)
	print("\t"+marco*len(titulo))
	input("presione una tecla para continuar")
	return 0

def login():   #función que valida el usuario del sistema
    intentos=3 
    i=0
    pw=''
    print("\t***CHECK USER***")
    print("\tIDENTIFIQUESE\n")
    users=["pablo","vero","cande","root"] #lista que guarda los usuarios válidos
    password="123456"    #pass general
    while intentos > 0:
        print(f"Tiene {intentos} Intentos")
        us = input("Login: ").lower()
        while i < len(users):			#busca el usuario en la lista users
            if us == users[i]:			#si lo encuentra pide pass
                pw=input("password: ")
                break				#rompe el bucle
            i+=1
        if pw == password:				#valida el pass
            print(f"Usuario {us.upper()} aceptado")
            return False                            #devuelve false si Es aceptado
        else:
            print("Usuario NO Autorizado")
            intentos-=1				#decrementa el contador de intentos
            i=0
    if intentos==0:			#si no tiene más intentos 
        return True                                 #devuelve True si NO es aceptado
        
    


def menu():							#función que muestra el menu
	os.system("clear")				#borra la pantalla en linux, en win cambiar "clear" por "cls"
	print("\t\t"+("*"*16))
	print("\t\tMENÚ DE OPCIONES")
	print("\t\t"+("*"*16))
	print("\t\t1-Nuevo Producto")
	print("\t\t2-Listado de Productos")
	print("\t\t3-Buscar Producto")
	print("\t\t4-Modificar Producto")
	print("\t\t5-Salir")
	return 0

def validar_producto(producto,listaProductos): #valida si el producto ya fue ingresado
	i=0
	while i < len(listaProductos):
		if producto == listaProductos[i][0]:
			print(f"el Producto {producto.upper()} ya fue ingresado")
			op=input(f"Desea actualizar Stock de {producto.upper()} S/N: ").lower()
			if op=='s':
				listaProductos[i][1]=input("NUEVO STOCK: ")
				return False
			else:
			    return False
		i+=1
	return True



def alta(listaProductos):							#función que da de alta un articulo
	articulo=[]			#Sublista donde se carga nombre y stock
	articulo.clear()   #borra cualquier residuo de ejecución anterior
	op1='s'
	no_ingresado=True		#indica si el producto ya fue ingresado
	while op1=='s':
		os.system("clear")                   #borra la pantalla en linux, en win cambiar "clear" por "cls"
		print("***ALTA DE PRODUCTO***\n")
		producto=input("Ingrese el nombre del producto: ").lower()
		no_ingresado=validar_producto(producto,listaProductos)
		if no_ingresado:							#si el producto NO fue ingresado pide el stock
		 stock=input("Ingrese el stock: ").lower()
		 articulo=[producto,stock]
		 listaProductos.append(articulo)
		 print("Producto ingresado")
		op1=input("Desea ingresar otro producto? S/N\n").lower()
	os.system("clear")						#borra la pantalla en linux, en win cambiar "clear" por "cls"
	input("Presione Enter para continuar")
	return 0

def listar(listaProductos):						#función que lista los articulos de la lista
	os.system("clear")						#borra la pantalla en linux, en win cambiar "clear" por "cls"
	print("***LISTADO DE PRODUCTOS***\n")
	i=0
	while i < len(listaProductos):
		print(f"PRODUCTO: {listaProductos[i][0]}\tSTOCK: {listaProductos[i][1]}")
		i+=1
	input("\nPresione Enter para continuar")
	return 0
	


def buscar(listaProductos):			#Busca un producto por nombre
	i=0
	no_se_encontro=True								#Bandera que indica si No se encontró el producto
	op=''
	os.system("clear")                   #borra la pantalla en linux, en win cambiar "clear" por "cls"
	print("***BUSQUEDA DE PRODUCTO***\n")
	producto=input("Ingrese el nombre del producto: ")
	while op!='n':
		while i < len(listaProductos):						#recorre la lista buscando el producto
			if producto == listaProductos[i][0]:
			 print("\n Producto en inventario")
			 print(f"PRODUCTO: {listaProductos[i][0]}\tSTOCK: {listaProductos[i][1]}")
			 no_se_encontro=False								#Si lo encuentra pasa a FALSO la bandera NO ENCONTRADO
			 input("Presione Enter para seguir ")
			 break									#Rompe el ciclo
			i+=1

		if no_se_encontro:											#Si NO encontró el producto lo indica ya que no=True
			print(f"Producto: {producto} NO hallado")
			
		op=input("Desea buscar otro producto? S/N ").lower() #pregunta si quiero buscar otro producto
		if op=='s':
			os.system("clear")                   #borra la pantalla en linux, en win cambiar "clear" por "cls"
			print("***BUSQUEDA DE PRODUCTO***\n")
			producto=input("Ingrese el nombre del producto: ")
			i=0								#resetea el indice
			no_se_encontro=True							#pasa a True por si no encuentra la nueva busqueda
	input("\nPresione enter para continuar")
	return 0
		

def modificar(listaProductos):    #busca un producto y permite modificar el nombre o el stock
	no_se_encontro=True
	op=''
	op1=''
	i=0
	os.system("clear")                   #borra la pantalla en linux, en win cambiar "clear" por "cls"
	print("***MODIFICAR DE PRODUCTO***\n")
	producto=input("Ingrese el nombre del producto: ")
	while op!='n':
		while i < len(listaProductos):						#recorre la lista buscando el producto
			if producto == listaProductos[i][0]:
			 print("\n Producto en inventario")
			 print(f"PRODUCTO: {listaProductos[i][0]}\tSTOCK: {listaProductos[i][1]}")
			 op1=input("Desea Modificar el producto? S/N: ").lower()
			 if op1=='s':
				 no_se_encontro=False								#Si lo encuentra pasa a FALSO la bandera NO ENCONTRADO
				 mod=input("Indique lo que desea modificar:\nA=Artículo\nS=Stock\nC=Cancelar\n--> ").lower()
				 if mod=='a':
					 listaProductos[i][0]=input("Nuevo Nombre Artículo: ").lower()
					 print("Nombre modificado\n")
					 print(f"PRODUCTO: {listaProductos[i][0]}\tSTOCK: {listaProductos[i][1]}")
				 if mod=='s':
					 listaProductos[i][1]=input("Nuevo stock: ").lower()
					 print("Stock modificado\n")
					 print(f"PRODUCTO: {listaProductos[i][0]}\tSTOCK: {listaProductos[i][1]}")
				 if mod=='c':
					 print("No se modificó el Artículo")
					 print(f"PRODUCTO: {listaProductos[i][0]}\tSTOCK: {listaProductos[i][1]}")
					 break			 
			 if op1=='n':
				 no_se_encontro=False								#Si lo encuentra pasa a FALSO la bandera NO ENCONTRADO
				 input("Presione Enter para seguir ")
			i+=1
		if no_se_encontro:											#Si NO encontró el producto lo indica ya que no=True
			print(f"Producto: {producto} NO hallado")
			
		op=input("Desea buscar otro producto? S/N ").lower() #pregunta si quiero buscar otro producto
		if op=='s':
			os.system("clear")                   #borra la pantalla en linux, en win cambiar "clear" por "cls"
			print("***BUSQUEDA DE PRODUCTO***\n")
			producto=input("Ingrese el nombre del producto: ").lower()
			i=0								#resetea el indice
			no_se_encontro=True							#pasa a True por si no encuentra la nueva busqueda
	input("\nPresione enter para continuar")
	return 0


def salir():						#función para salir del programa
	print("¿Desea Salir? S/N")
	op2=input().lower()
	if op2 == 'n':
		op=''
		return op
	else:
		os.system("clear")				#borra la pantalla en linux, en win cambiar "clear" por "cls"
		print("***Saliendo***")
		input("\nPRESIONE ENTER PARA SALIR")
		op='5'
		return op

"""
En la función principal se usan las funciones de login(), alta de productos, busqueda, listar productos y la función de salir
"""


def main():			#función principal				
	listaProductos=[]	#lista donde se almacenan los productos y el stock
	listaProductos.clear()   #borra cualquier residuo de ejecución anterior
	op=""
	noAutorizado=login()  #login()= false Usuario AUTORIZADO, login()=True usuario No AUTORIZADO
	if noAutorizado:            #si el usuario no esta AUTORIZADO sale del programa
	    print("Error de Login\n")
	    print("***ACCESO NO AUTORIZADO***")
	    return 1
	inicio()							#muestra el mensaje de inicio
	while op != '5':					# sale del programa si se ingresa la opción 4
		menu()
		op=input("Ingrese una opción: ")
		if op=='1':
			alta(listaProductos)	#Alta de producto
		elif op=='2':
			listar(listaProductos)	#muestra el listado de productos
		elif op=='3':
			buscar(listaProductos) #busca el producto
		elif op=='4':
			modificar(listaProductos) #busca y modifica un producto, su nombre o stock
		elif op=='5':
			op=salir()		#sale del programa
		else:
			print("Error, presione Enter para continuar")
			input()
	return 0

main()   #Llamado de la función principal
