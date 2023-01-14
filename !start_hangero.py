from tkinter import *
import winsound
from tkinter import messagebox
import os
from tkinter.ttk import *
from time import strftime
import subprocess, sys


def time():
    string = strftime('%Y.%m.%d %H:%M')
    clock.config(text=string)
    clock.after(1000, time)
def exemaker():
    tt=str(text_box.get())
    if tt.isnumeric()==False:
         messagebox.showerror("Figyelem!","Betűt vagy negatív számot nem adhatsz meg!")
         text_box.delete(0, END)
    elif int(tt)<0:
        messagebox.showerror("Figyelem!","0-nál kisebb értéket nem adhatsz meg!")
        text_box.delete(0, END)
    elif int(tt)>100:
         messagebox.showerror("Figyelem!","100-nál nagyobb értéket nem adhatsz meg!")
         text_box.delete(0, END)
    
    else:
        file = open('hh.ps1','r')
        lines = file.readlines()[:-1]
        if tt=="100":
            lines.append("1")
            
        elif len(tt)==1:
            lines.append("0.0"+str(tt))
        else:
            lines.append("0."+str(tt))
        file.close()
        file = open('hh.ps1','w')
        file.writelines(lines)
        file.close()
        p = subprocess.Popen(["powershell.exe", 
                "Invoke-ps2exe hh.ps1 hangero_"+tt+".exe -noConsole"], 
                stdout=sys.stdout)
        p.communicate()
        winsound.PlaySound('kk.wav', winsound.SND_FILENAME)
        messagebox.showinfo("Sikeres exe készítés","Az exe elkészült!\nJó trollkodást!") 
        text_box.delete(0, END)


mainw=Tk()
mainw.geometry("1080x720")
mainw.title("Gépfelhangosító exe maker")
mainw.iconbitmap("vol.ico")
mainw.minsize(1080,720)
clock = Label(mainw, font=('calibri', 18, 'bold'), foreground='black')
clock.pack(anchor = "e", side = "bottom")
time()
weltitle="Szia "+str(os.getlogin())+"!"
maintitle = Label(mainw,text= weltitle)
os.getlogin( ) 
welcome_settings = ("Comic Sans MS", 20, "bold")
maintitle.configure(font=welcome_settings)
maintitle.place(x=440, y=0)
choo="Kérlek add meg, hogy az exe milyen\n hangerőre állítsa be a gépet!"
chootitle=Label(mainw,text=choo)
chootitle.configure(font=welcome_settings)
chootitle.place(x=360, y=50)
warnmm = ("Comic Sans MS", 15, "bold")
warnme="0-100 közötti értéket adj meg!"
warn=Label(mainw,text=warnme,foreground="red")
warn.configure(font=warnmm)
warn.place(x=410, y=200)
text_box=Entry(mainw,width=9,font=('Arial', 28))
text_box.place(x=460, y=250)
submit_btn=Button(mainw, text="Exe készítése", width=20,command=exemaker)
submit_btn.place(x=494, y=303)

mainw.mainloop()