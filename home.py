# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:43:16 2019
@author: Mak Chaudhary
"""

import tkinter as tk
import threading
import os
import diff
import ghome
os.chdir('C:\\Users\\Mak Chaudhary\\Desktop\\sdp_dataset')



Tcall = threading.Thread(target=diff.captureFrame)
scall = threading.Thread(target=ghome.gens)
def search():
    Tcall.start()
    
def btn_generate():
    scall.start()
  
    
class MainApp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="grey")
        self.parent = parent
        
        button = tk.Button(parent, text="Search",command=lambda:search())
        button.pack(fill=tk.X, pady=10)
        button = tk.Button(parent, text="Generate",command = lambda: btn_generate())
        button.pack(fill=tk.X, pady=10)

root = tk.Tk()
w = tk.Label(root, text="User Home", bg="grey", fg="white")
w.pack(fill=tk.X, pady=10)
root.geometry("312x324")
root.config(background="grey")
app = MainApp(root)
app.pack(fill="both", expand=True)
root.mainloop()

'''
window = Tk()
window.geometry("312x324") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("Calcualtor")
'''