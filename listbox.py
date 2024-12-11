'''
Dajani Giulio Classe 4^C 09/05/21
Correzione Verifica Ristorante + aggiunta listbox
'''
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
import locale
locale.setlocale(locale.LC_ALL, '')

class Ristorante(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master.title('Listbox')
		self.master.minsize(770, 600)
		self.master.resizable(True, True)
		self.master.option_add('*Font', 'arial 14')
		self.grid()
		self.lancio_widgets()
	
	def lancio_widgets(self):
		fontprinc = font.Font(family = 'arial', size = 18, weight = 'bold')
		#titolo
		self.lbl1 = tk.Label(self, text = 'Ristorante Panna Montata', font = fontprinc)
		self.lbl1.grid(row = 0, column = 0, columnspan = 8)
		#lblvuoto
		self.lblv = tk.Label(self, text = '')
		self.lblv.grid(row = 1, column = 0, columnspan = 5)
		#dati-cliente
		self.lbl2 = tk.Label(self, text = 'Dati cliente:', width = 13)
		self.lbl2.grid(row = 2, column = 0, sticky = tk.W)
		#btnreset
		self.btn1 = tk.Button(self, text = 'Reset', width = 6, bg = 'red', command = self.svuota_caselle)
		self.btn1.grid(row = 2, column = 4)
		#btnesci
		self.btn2 = tk.Button(self, text = 'ESCI', width = 15, bg = 'yellow', command = self.master.destroy)
		self.btn2.grid(row = 2, column = 5)
		#cognome
		self.lbl3 = tk.Label(self, text = 'Cognome')
		self.lbl3.grid(row = 3, column = 0, sticky = tk.E)
		self.cog = tk.StringVar()
		self.txtcog = tk.Entry(self, textvariable = self.cog, justify = tk.CENTER)
		self.txtcog.grid(row = 3, column = 1, columnspan = 2)
		#listbox
		self.lble = tk.Label(self, text = 'Età')
		self.lble.grid(row = 4, column = 0, sticky = tk.E)
		self.scrollbar = tk.Scrollbar(self, orient = tk.VERTICAL)	#creo scrollbar con orientament orizzontale o verticale
		self.scrollbar.grid(row = 4, column = 1, sticky = tk.N + tk.S)
		self.lstb = tk.Listbox(self, height = 7, width = 5, bd = 4, justify = tk.CENTER)
		self.lstb['yscrollcommand'] = self.scrollbar.set	#setto lo scrollbar alla listbox
		self.lstb.grid(row = 4, column = 1, sticky = tk.W)
		self.lstb['highlightcolor'] = 'yellow'
		self.lstb['selectmode'] = 'SINGLE'
		self.lstb['selectbackground'] = 'green'
		self.scrollbar.config(command=self.lstb.yview)	#visualizzare barra scorrimento verticale
		#self.nselez = self.lstb.get(self.lstb.curselection())	salvo il numero iesimo nella variabile nselez
		for i in range(1, 101):
			self.lstb.insert(i, i)	#con insert inserisco valori all'interno della listbox insert(indice, valore)
			self.lstb.activate(i)
		#self.lstb.bind('<<ListboxSelect>>', Op_Evento)		
		#menù
		self.lbl4 = tk.Label(self, text = 'Menù:', justify = tk.CENTER)
		self.lbl4.grid(row = 5, column = 3, columnspan = 3)
		#commensali
		self.lbl5 = tk.Label(self, text = 'Commensali:')
		self.lbl5.grid(row = 6, column = 0, sticky = tk.W)
		self.comm = tk.IntVar()
		self.txtcomm = tk.Entry(self, textvariable = self.comm, justify = tk.RIGHT, width = 3)
		self.txtcomm.grid(row = 6, column = 1, sticky = tk.W)
		#btnturistico
		self.btn3 = tk.Button(self, text = 'Turistico (25€)', command = self.control1)
		self.btn3.grid(row = 6, column = 3)
		#btndegustazione
		self.btn4 = tk.Button(self, text = 'Degustazione (40€)', command = self.control2)
		self.btn4.grid(row = 6, column = 5)
		#lblvuoto
		self.lblv = tk.Label(self, text = '')
		self.lblv.grid(row = 7, column = 0, columnspan = 5)
		#totale-conto
		self.lbl6 = tk.Label(self, text = 'Totale conto:')
		self.lbl6.grid(row = 8, column = 0, sticky = tk.E)
		self.totcont = tk.StringVar()
		self.txttotcont = tk.Entry(self, textvariable = self.totcont, justify = tk.RIGHT)
		self.txttotcont.grid(row = 8, column = 1, columnspan = 2, ipady = 2)
		#sconto
		self.lbl7 = tk.Label(self, text = 'Sconto:')
		self.lbl7.grid(row = 8, column = 4, sticky = tk.E)
		self.totscont = tk.StringVar()
		self.txttotscont = tk.Entry(self, textvariable = self.totscont, justify = tk.RIGHT, width = 18)
		self.txttotscont.grid(row = 8, column = 5, ipady = 2)
		
		self.update_idletasks() #refresh
	
	def control1(self):
		if (self.cog.get() == ''):
			messagebox.showwarning('Cognome', 'Inserisci prima il cognome!')	
		if (self.cog.get() != ''):
			if (self.comm.get() == 0):
				messagebox.showinfo('Numero commensali', 'Il numero dei commensali è impostato a 0')
			if (self.comm.get() > 0 and self.comm.get() <= 6):
				self.btn3['bg'] = 'orange'
				self.btn4['bg'] = '#D2D2D2'
				c = self.comm.get()
				if (int((self.lstb.get(ACTIVE))) < 12):
					totc = c * 25 - 5
					self.totcont.set(locale.currency(totc))
					self.totscont.set(locale.currency(5))
				else:
					totc = c * 25
					self.totcont.set(locale.currency(totc))
					self.totscont.set(locale.currency(0))
			elif (self.comm.get() > 6):
				self.btn3['bg'] = 'orange'
				self.btn4['bg'] = '#D2D2D2'
				c = self.comm.get()
				if (int((self.lstb.get(ACTIVE))) < 12):
					tscont = ((c * 25) * 10) / 100 - 5
					tot = (c * 25) - tscont
					self.totcont.set(locale.currency(tot))
					self.totscont.set(locale.currency(tscont))
				else:
					tscont = ((c * 25) * 10) / 100
					tot = (c * 25) - tscont
					self.totcont.set(locale.currency(tot))
					self.totscont.set(locale.currency(tscont))
    		
	def control2(self):
		if (self.cog.get() == ''):
			messagebox.showwarning('Cognome', 'Inserisci prima il cognome!')	
		if (self.cog.get() != ''):
			if (self.comm.get() == 0):
				messagebox.showinfo('Numero commensali', 'Il numero dei commensali è impostato a 0')
			if (self.comm.get() > 0 and self.comm.get() <= 6):
				self.btn4['bg'] = 'orange'
				self.btn3['bg'] = '#D2D2D2'
				c = self.comm.get()
				if (int((self.lstb.get(ACTIVE))) < 12):				
					totc = c * 40 - 5
					self.totcont.set(locale.currency(totc))
					self.totscont.set(locale.currency(5))
				else:
					totc = c * 40
					self.totcont.set(locale.currency(totc))
					self.totscont.set(locale.currency(0))
			elif (self.comm.get() > 6):
				self.btn4['bg'] = 'orange'
				self.btn3['bg'] = '#D2D2D2'
				c = self.comm.get()
				if (int((self.lstb.get(ACTIVE))) < 12):
					tscont = ((c * 40) * 10) / 100 - 5
					tot = (c * 40) - tscont
					self.totcont.set(locale.currency(tot))
					self.totscont.set(locale.currency(tscont))
				else:
					tscont = ((c * 40) * 10) / 100
					tot = (c * 40) - tscont
					self.totcont.set(locale.currency(tot))
					self.totscont.set(locale.currency(tscont))
					

	def svuota_caselle(self):
		self.txtcog.delete(0, tk.END)
		self.comm.set(0)
		self.txttotcont.delete(0, tk.END)
		self.txttotscont.delete(0, tk.END)
		self.btn3['bg'] = '#D2D2D2'
		self.btn4['bg'] = '#D2D2D2'
		self.lstb.selection_clear(0, tk.END)	#resetta le selezioni nella listbox alla forma iniziale

R = Ristorante()
R.mainloop()
