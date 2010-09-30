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

import pygtk
pygtk.require('2.0')
import gtk
import MySQLdb
# Conexión a la base de datos
conn = MySQLdb.connect(host="localhost", user="xbitcarry", passwd="xbitcarry", db="contur")
# Creamos el cursor para MySQL
cursor = conn.cursor()

class main_control:
	def __init__(self):
		# Inicializamos los Widgets y los empacamos en una ventana
		self.mainWindow = gtk.Window()
		self.mainWindow.set_title("Gestion de Gasolineras")
		self.mainWindow.set_size_request(600, 300)
		self.mainWindow.connect("destroy", gtk.main_quit)

		self.vbox = gtk.VBox()
		self.vbox.set_border_width(10)
		self.mainWindow.add(self.vbox)

		# Creamos una tabla para manejar los controles del menú
		self.table = gtk.Table(7, 2, True)
		self.table.set_border_width(10)
		self.table.set_row_spacings(3)
		self.table.set_col_spacings(3)
		self.vbox.pack_start(self.table, True, False, 0)
		# Mostramos todos los controles
		self.mainWindow.show_all()
		
	def main(self):
		gtk.main()

if __name__ == "__main__":
	control = main_control()
	control.main()
