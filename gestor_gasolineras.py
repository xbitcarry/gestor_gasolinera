#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ***********************************************************
# * Gestor de Gasolineras                                   *
# * ---------------------                                   *
# * Esta aplicación ayudará en la gestión de una gasolinera *
# * al realizar los cortes de turno tanto de las bombas     *
# * despachadoras de gasolina, como el control de aceites   *
# * y depósitos en efectivo.                                *
# * *********************************************************
# * Desarrollado por:                                       *
# *  xbitcarry - xbitcarry(at)gmail.com                     *
# ***********************************************************
# * Aplicacion desarrollada con herramientas libres         *
# * - Python, Pygtk, MySQL -                                *
# * -= Contenido bajo licencia GPL V3 =-                    *
# ***********************************************************
# * Pre-requisitos:                                         *
# *  - Servidor de base de datos MySQL                      *
# *  - Usuario       : xbitcarry                            *
# *  - Contraseña    : xbitcarry                            *
# *  - Base de datos :    contur                            *
# *  - Tabla         : main_control                         *
#                         bomba       int         not null  *
# *                       despachador varchar(20) not null  *
# *                       magna       int         not null  *
# *                       premium     int         not null  *
# *                       diesel      int         not null  *
# *                       aditivos    int         not null  *
# *                       turno       int         not null  *
# *                       depositos   real        not null  *
# * -Tip: en la linea de comandos de mysql escribir:        *
# * create table main_contol (bomba int not null, despachad *
# * or varchar(20) not null, magna int not null, premium in *
# * t not null, diesel int not null, aditivos int not null, *
# * turno int not null, depositos real not null);           *
# ***********************************************************

# importo los módulos que voy a ocupar
import pygtk
# checo la versión
pygtk.require('2.0')
import gtk
# importo el módulo para trabajar con la base de datos
import MySQLdb
# creo la conexión a la base de datos
conn = MySQLdb.connect(host="localhost", user="xbitcarry", passwd="xbitcarry", db="contur")
# creo el cursor para MySQL
cursor = conn.cursor()

# creo la clase base de la aplicación
class main_control:
	# defino main con el ciclo gtk.main()
	def main(self):
		gtk.main()
	
	# creo la función para ocultar la ventana entdat
	def destroy_entdat(self, widget):
		self.entdatWindow.hide()

	# defino entdat * Entrada de Datos *
	def entdat(self, widget):
		# creo la ventana y le doy atributos
		self.entdatWindow = gtk.Window()
		self.entdatWindow.set_title("Ingreso de datos de turno e isla")
		self.entdatWindow.set_size_request(900, 275)
		# conecto la función cerrar ventana con gtk.main_quit para terminar la aplicación
		self.entdatWindow.connect("destroy", gtk.main_quit)
		
		# agrego un contenedor vertical a la ventana
		self.vbox = gtk.VBox()
		self.vbox.set_border_width(10)
		self.entdatWindow.add(self.vbox)
		
		# creo una tabla para insertar las etiquetas y los campos de entrada de texto
		self.table = gtk.Table(8,8, False)
		self.table.set_border_width(10)
		self.table.set_row_spacings(3)
		self.table.set_col_spacings(3)
		self.vbox.pack_start(self.table, False, True, 0)
		
		# inserto los datos a la tabla
		label = gtk.Label("Inicial Magna")
		self.table.attach(label, 0,1,0,1)
		self.entry1 = gtk.Entry(max = 10)
		self.table.attach(self.entry1, 1,2,0,1)
		
		label = gtk.Label("Inicial Premium")
		self.table.attach(label, 0,1,1,2)
		self.entry2 = gtk.Entry(max = 10)
		self.table.attach(self.entry2, 1,2,1,2)
		
		label = gtk.Label("Inicial Monogrado")
		self.table.attach(label, 0,1,2,3)
		self.entry3 = gtk.Entry(max = 10)
		self.table.attach(self.entry3, 1,2,2,3)
		
		label = gtk.Label("Inicial Multigrado")
		self.table.attach(label, 0,1,3,4)
		self.entry4 = gtk.Entry(max = 10)
		self.table.attach(self.entry4, 1,2,3,4)
		
		label = gtk.Label("Inicial 2 Tiempos")
		self.table.attach(label, 0,1,4,5)
		self.entry5 = gtk.Entry(max = 10)
		self.table.attach(self.entry5, 1,2,4,5)
		
		label = gtk.Label("Inicial Aditivo")
		self.table.attach(label, 0,1,5,6)
		self.entry6 = gtk.Entry(max = 10)
		self.table.attach(self.entry6, 1,2,5,6)
		
		label = gtk.Label("Inicial Limpiador")
		self.table.attach(label, 0,1,6,7)
		self.entry7 = gtk.Entry(max = 10)
		self.table.attach(self.entry7, 1,2,6,7)
		
		label = gtk.Label("Final Magna")
		self.table.attach(label, 2,3,0,1)
		self.entry1 = gtk.Entry(max = 10)
		self.table.attach(self.entry1, 3,4,0,1)
		
		label = gtk.Label("Final Premium")
		self.table.attach(label, 2,3,1,2)
		self.entry2 = gtk.Entry(max = 10)
		self.table.attach(self.entry2, 3,4,1,2)
		
		label = gtk.Label("Final Monogrado")
		self.table.attach(label, 2,3,2,3)
		self.entry3 = gtk.Entry(max = 10)
		self.table.attach(self.entry3, 3,4,2,3)
		
		label = gtk.Label("Final Multigrado")
		self.table.attach(label, 2,3,3,4)
		self.entry4 = gtk.Entry(max = 10)
		self.table.attach(self.entry4, 3,4,3,4)
		
		label = gtk.Label("Final 2 Tiempos")
		self.table.attach(label, 2,3,4,5)
		self.entry5 = gtk.Entry(max = 10)
		self.table.attach(self.entry5, 3,4,4,5)
		
		label = gtk.Label("Final Aditivo")
		self.table.attach(label, 2,3,5,6)
		self.entry6 = gtk.Entry(max = 10)
		self.table.attach(self.entry6, 3,4,5,6)
		
		label = gtk.Label("Final Limpiador")
		self.table.attach(label, 2,3,6,7)
		self.entry7 = gtk.Entry(max = 10)
		self.table.attach(self.entry7, 3,4,6,7)
		
		label = gtk.Label("Diferencia Magna")
		self.table.attach(label, 4,5,0,1)
		self.entry1 = gtk.Entry(max = 10)
		self.table.attach(self.entry1, 5,6,0,1)
		
		label = gtk.Label("Diferencia Premium")
		self.table.attach(label, 4,5,1,2)
		self.entry2 = gtk.Entry(max = 10)
		self.table.attach(self.entry2, 5,6,1,2)
		
		label = gtk.Label("Diferencia Monogrado")
		self.table.attach(label, 4,5,2,3)
		self.entry3 = gtk.Entry(max = 10)
		self.table.attach(self.entry3, 5,6,2,3)
		
		label = gtk.Label("Diferencia Multigrado")
		self.table.attach(label, 4,5,3,4)
		self.entry4 = gtk.Entry(max = 10)
		self.table.attach(self.entry4, 5,6,3,4)
		
		label = gtk.Label("Diferencia 2 Tiempos")
		self.table.attach(label, 4,5,4,5)
		self.entry5 = gtk.Entry(max = 10)
		self.table.attach(self.entry5, 5,6,4,5)
		
		label = gtk.Label("Diferencia Aditivo")
		self.table.attach(label, 4,5,5,6)
		self.entry6 = gtk.Entry(max = 10)
		self.table.attach(self.entry6, 5,6,5,6)
		
		label = gtk.Label("Diferencia Limpiador")
		self.table.attach(label, 4,5,6,7)
		self.entry7 = gtk.Entry(max = 10)
		self.table.attach(self.entry7, 5,6,6,7)
		
		# inserto una caja horizontal dentro de la caja vertical y dentro un botón
		self.hbox = gtk.HBox(False, 0)
		self.vbox.pack_start(self.hbox, True, True, 0)
		
		button = gtk.Button("Continuar")
		self.hbox.pack_start(button, True, True, 0)
		# conecto la señal de cerrar ventana con gtk.main_quit para terminar la aplicación
		button.connect("clicked", gtk.main_quit)
		
		# muestro todos los controles
		self.entdatWindow.show_all()
	
	# defino la función para ocultar la ventana contra
	def destroy_contra(self,widget):
		self.mainWindow.hide()
	
	# defino contra * Control de Trabajador *
	def contra(self, widget):
		# creo la ventana y le doy atributos
		self.mainWindow = gtk.Window()
		self.mainWindow.set_title("Control de Trabajo")
		self.mainWindow.set_size_request(400, 125)
		# conecto la señal de cerrar ventana con gtk.main_quit para terminar la aplicación
		self.mainWindow.connect("destroy", gtk.main_quit)
		
		# agrego un control vertical a la ventana
		self.vbox = gtk.VBox()
		self.vbox.set_border_width(10)
		self.mainWindow.add(self.vbox)
		
		# creo una tabla para insertar las etiquetas y las campos de entrada de texto
		self.table = gtk.Table(3,2,False)
		self.table.set_border_width(10)
		self.table.set_row_spacings(3)
		self.table.set_col_spacings(3)
		self.vbox.pack_start(self.table, False, True, 0)
		
		label = gtk.Label("Turno")
		self.table.attach(label,0,1,0,1)
		self.entry1 = gtk.Entry(max = 2)
		self.table.attach(self.entry1, 1,2,0,1)
		
		label = gtk.Label("Isla")
		self.table.attach(label, 0,1,2,3)
		self.entry2 = gtk.Entry(max = 2)
		self.table.attach(self.entry2, 1,2,2,3)
		
		# inserto una caja horizontal dentro de la caja vertical y dentro un botón
		self.hbox = gtk.HBox(False, 0)
		self.vbox.pack_start(self.hbox, True, True, 0)
		
		button = gtk.Button("Continuar")
		self.hbox.pack_start(button, True, True, 0)
		# conecto el evento de clickear el botón con entdat y con destroy_contra
		button.connect("clicked", self.entdat)
		button.connect( "clicked", self.destroy_contra)
		
		# muestro todos los controles
		self.mainWindow.show_all()
		
	# defino la funcion para ocultar la ventana intro	
	def destroy_intro(self, widget):
		self.introWindow.hide()
	
	# defino intro * Control de Acceso a la aplicación *
	def intro(self):
		# creo la ventana y le doy atributos
		self.introWindow = gtk.Window()
		self.introWindow.set_title("Control de acceso")
		self.introWindow.set_size_request(400, 125)
		# conecto la señal de cerrar ventana con gtk.main_quit para cerrar la aplicación
		self.introWindow.connect("destroy", gtk.main_quit)
		
		# agrego un control vertical a la ventana
		self.vbox = gtk.VBox()
		self.vbox.set_border_width(10)
		self.introWindow.add(self.vbox)
		
		# creo una tabla para insertar las etiquetas y los campos de entrada de texto
		self.table = gtk.Table(3,2,False)
		self.table.set_border_width(10)
		self.table.set_row_spacings(3)
		self.table.set_col_spacings(3)
		self.vbox.pack_start(self.table, False, True, 0)
		
		label = gtk.Label("Despachador")
		self.table.attach(label, 0,1,0,1)
		self.entry1 = gtk.Entry(max = 8)
		self.table.attach(self.entry1,1,2,0,1)
		
		label = gtk.Label("Clave")
		self.table.attach(label, 0,1,2,3)
		self.entry2 = gtk.Entry(max = 8)
		self.table.attach(self.entry2, 1,2,2,3)
		
		# inserto un caja horizontal dentro de la caja vertical y dentro dos botones
		self.hbox = gtk.HBox(False, 0)
		self.vbox.pack_start(self.hbox, True, True, 0)
		
		button = gtk.Button("Entrar")
		self.hbox.pack_start(button, True, True, 0)
		# conecto el evento de clickear el botón con contra y destroy_intro
		button.connect("clicked", self.contra)
		button.connect("clicked", self.destroy_intro)
		
		button = gtk.Button("Salir")
		self.hbox.pack_start(button, True, True, 0)
		# conecto el evento de clickear el botón con gtk.main_quit para terminar la aplicación
		button.connect("clicked", gtk.main_quit)
		
		# muestro todos los controles
		self.introWindow.show_all()

	def __init__(self):
		self.intro()

if __name__ == "__main__":
	intro = main_control()
	intro.main()
