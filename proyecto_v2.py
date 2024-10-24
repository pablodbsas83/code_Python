#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  proyecto_v2.py
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

def menu():							#función que muestra el menu
	os.system("clear")				#borra la pantalla en linux, en win cambiar "clear" por "cls"
	print("\t\t"+("*"*16))
	print("\t\tMENÚ DE OPCIONES")
	print("\t\t"+("*"*16))
	print("\t\t1-Nuevo Producto")
	print("\t\t2-Listado de Productos")
	print("\t\t3-Buscar Producto")
	print("\t\t4-Salir")
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
		producto=input("Ingrese el nombre del producto: ")
		no_ingresado=validar_producto(producto,listaProductos)
		if no_ingresado:							#si el producto NO fue ingresado pide el stock
		 stock=input("Ingrese el stock: ")
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
		op='4'
		return op




def main():							#función principal
	listaProductos=[]	#lista donde se almacenan los productos y el stock
	listaProductos.clear()   #borra cualquier residuo de ejecución anterior
	op=""
	inicio()							#muestra el mensaje de inicio
	while op != '4':					# sale del programa si se ingresa la opción 4
		menu()
		op=input("Ingrese una opción: ")
		if op=='1':
			alta(listaProductos)	#Alta de producto
		elif op=='2':
			listar(listaProductos)	#muestra el listado de productos
		elif op=='3':
			buscar(listaProductos) #busca el producto
		elif op=='4':
			op=salir()		#sale del programa
		else:
			print("Error, presione Enter para continuar")
			input()
	return 0

main()
