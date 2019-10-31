# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:51:19 2019

@author: Mak Chaudhary
"""
import tkinter as tk
import numpy as np
import threading
import DataSetGenerator

 
def gens():
    #Tcall = threading.Thread();
    
    def onClick():
        #Tcall = threading.Thread(target=DataSetGenerator.Gdataset,args=(name))
            Tcall = threading.Thread(target=DataSetGenerator.Gdataset).start()
    class MainApp(tk.Frame):
        def __init__(self, parent):
            name=tk.StringVar()
            tk.Frame.__init__(self, parent, bg="grey")
            self.parent = parent
            name = tk.Label(root, text = "Name").place(x = 30,y = 50)
            e1 = tk.Entry(root, textvariable=name).place(x = 80, y = 50) 
            button = tk.Button(parent, text="Generate",command=onClick)
            button.pack(fill=tk.X, pady=80)
        
    
    root = tk.Tk()
    root.geometry("312x324")
    root.config(background="grey")
    app = MainApp(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
#gens();
'''
from tkinter import *
master = Tk() 
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
mainloop() 
'''