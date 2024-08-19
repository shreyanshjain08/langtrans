#PROGRAM TO CREATE LANGUAGE TRANSLATOR 
#import GUI library tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk


#import googletrans library
from googletrans import Translator
from googletrans import LANGUAGES
#creating object window 
root = Tk()
root.geometry("500x650")#Geometry
root.title("Translator")#Title
root.config(bg='Grey')#config meand color and all


#Function for translation
def get_data():
    trans = Translator()
    comb_sou_option=comb_sou.get()
    comb_des_option=comb_des.get()
    txt = sou_txt.get(1.0,tk.END)
    trans1 = trans.translate(text=txt,src = comb_sou_option,dest=comb_des_option)
    
    des_txt.insert(tk.END,trans1.text)

#Function for clearing all values       
def clearall():
    sou_txt.delete(1.0,tk.END)
    des_txt.delete(1.0,tk.END)


#Creating a label text and placing it in object window
lbl_txt = Label(root,text="Translator",font=("Time New roman",20,"bold") )
lbl_txt.place(x=100,y=20,height=40,width=300)


#Creating label Source text
lbl_txt = Label(root,text="Source Text",font=("Time New roman",16) )
lbl_txt.place(x=10,y=80,height=30,width=150)
sou_txt = Text(root,font=("Time New roman",18))
sou_txt.place(x=10,y=120,height=200,width=480)


#creating list for languages
list_txt = list(LANGUAGES.values()) 


#Creating combobox for from language
comb_sou= ttk.Combobox(root,values = list_txt)
comb_sou.place(x=10,y =340,height = 30,width= 100)
comb_sou.set("english")


#Creating combobox for to language
comb_des= ttk.Combobox(root,values = list_txt)
comb_des.place(x=230,y =340,height = 30,width= 100)
comb_des.set("hindi")


#Creating label for output 
lbl_txt = Label(root,text="Output",font=("Time New roman",16) )
lbl_txt.place(x=10,y=400,height=30,width=150)
des_txt = Text(root,font=("Time New roman",18),wrap=WORD)
des_txt.place(x=10,y=440,height=200,width=480)


#Button for translation
Btn1=Button(root,text='<->',relief=RAISED,command=get_data)
Btn1.place(x=120,y=340,height = 30,width = 100)


#Button for Clear all
Btn2=Button(root,text='Clear all',relief=RAISED,command=clearall)
Btn2.place(x=340,y=340,height = 30,width = 100)

root.mainloop()