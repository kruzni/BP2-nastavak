import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import tkinter as tk

#konekcija

def connection(): 
    conn=pymysql.connect(host='localhost',user='root',password='root',database="baza_banke_krvi")
    return conn

def refreshTable():
    for data in my_tree3.get_children():
        my_tree3.delete(data)
        
    for array in readPrijevoznik():
        my_tree3.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
        
    my_tree3.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
    my_tree3.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
    
#GUI

root = Tk()
root.title("Prijevoznik")
root.geometry("1920x1080")
root.iconbitmap("krv.ico")
my_tree3 = ttk.Treeview(root)

#rezervirana mjesta za upis
rezmj1Prijevoznik=tk.StringVar()
rezmj2Prijevoznik=tk.StringVar()
rezmj3Prijevoznik=tk.StringVar()
rezmj4Prijevoznik=tk.StringVar()
rezmj5Prijevoznik=tk.StringVar()


#postavljanje vrijednosti za rez mjesta

def postRezMjPrijevoznik(rijecPrijevoznik, brojPrijevoznik):
    if brojPrijevoznik == 1:
        rezmj1Prijevoznik.set(rijecPrijevoznik)
    if brojPrijevoznik == 2:
        rezmj2Prijevoznik.set(rijecPrijevoznik)
    if brojPrijevoznik == 3:
        rezmj3Prijevoznik.set(rijecPrijevoznik)
    if brojPrijevoznik == 4:
        rezmj4Prijevoznik.set(rijecPrijevoznik)
    if brojPrijevoznik == 5:
        rezmj5Prijevoznik.set(rijecPrijevoznik)
       

#funkcije

def readPrijevoznik():
    connPrijevoznik=connection()
    cursorPrijevoznik=connPrijevoznik.cursor()
    cursorPrijevoznik.execute("SELECT * FROM prijevoznik")
    rezultatPrijevoznik=cursorPrijevoznik.fetchall()
    connPrijevoznik.commit()
    connPrijevoznik.close()
    return rezultatPrijevoznik

def addPrijevoznik():
    id=str(prijevoznikIDEntry.get())
    ime_prijevoznika=str(prijevoznikImePrijevoznikaEntry.get())
    kontakt=str(prijevoznikKontaktEntry.get())
    tip_vozila=str(prijevoznikTipVozilaEntry.get())
    registarska_oznaka=str(prijevoznikRegistarskaOznakaEntry.get())
    
    
    if (id=="" or id==" ") or (ime_prijevoznika=="" or ime_prijevoznika==" ")or (kontakt=="" or kontakt==" ")or (tip_vozila=="" or tip_vozila==" ")or (registarska_oznaka=="" or registarska_oznaka==" "):
        messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
        return
    else:
        try:
            connPrijevoznik=connection()
            cursorPrijevoznik=connPrijevoznik.cursor()
            cursorPrijevoznik.execute("INSERT INTO prijevoznik VALUES ('"+id+"','"+ime_prijevoznika+"','"+kontakt+"','"+tip_vozila+"','"+registarska_oznaka+"') ")
            connPrijevoznik.commit()
            connPrijevoznik.close()
        except:
            messagebox.showinfo("Pogreška!","Id prijevoznika već postoji!")
            return
        
    refreshTable()
    
    
def selectPrijevoznik():
        try:
            odabrani_prijevoznik=my_tree3.selection()[0]
            id=str(my_tree3.item(odabrani_prijevoznik)['values'][0])
            ime_prijevoznika=str(my_tree3.item(odabrani_prijevoznik)['values'][1])
            kontakt=str(my_tree3.item(odabrani_prijevoznik)['values'][2])
            tip_vozila=str(my_tree3.item(odabrani_prijevoznik)['values'][3])
            registarska_oznaka=str(my_tree3.item(odabrani_prijevoznik)['values'][4])
        
            postRezMjPrijevoznik(id,1)
            postRezMjPrijevoznik(ime_prijevoznika,2)
            postRezMjPrijevoznik(kontakt,3)
            postRezMjPrijevoznik(tip_vozila,4)
            postRezMjPrijevoznik(registarska_oznaka,5)
            
        except:
            messagebox.showinfo("Pogreška!","Molimo izaberite podatak")
            
def searchPrijevoznik():
    id=str(prijevoznikIDEntry.get())
    ime_prijevoznika=str(prijevoznikImePrijevoznikaEntry.get())
    kontakt=str(prijevoznikKontaktEntry.get())
    tip_vozila=str(prijevoznikTipVozilaEntry.get())
    registarska_oznaka=str(prijevoznikRegistarskaOznakaEntry.get())
    if id is None or id == "":
        id = '%'
    if ime_prijevoznika is None or ime_prijevoznika == "":
        ime_prijevoznika = '%'
    if kontakt is None or kontakt == "":
        kontakt = '%'
    if tip_vozila is None or tip_vozila == "":
        tip_vozila = '%'
    if registarska_oznaka is None or registarska_oznaka == "":
        registarska_oznaka = '%'
    connPrijevoznik=connection()
    cursorPrijevoznik=connPrijevoznik.cursor()
    query = "SELECT * FROM prijevozjnik WHERE id like %s or ime_prijevoznika like %s or kontakt like %s or tip_vozila like %s or registarska_oznaka like %s"
    cursorPrijevoznik.execute(query, (id, ime_prijevoznika, kontakt, tip_vozila, registarska_oznaka))
    rows = cursorPrijevoznik.fetchall()
    match = False
    for row in rows:
        if str(row[0]) == id:
            match = True
            for i in range(0,9):
                postRezMjPrijevoznik(row[i],(i+1))
    if not match:
        messagebox.showinfo("Pogreška!","Nema odgovarajućeg podatka!")
    connPrijevoznik.commit()
    connPrijevoznik.close()
    


#GUI
frame1Prijevoznik_Zaposlenik = Frame()

frame1Prijevoznik_Zaposlenik['bg'] = '#9E5D5D'

labelPrijevoznik = Label(root, text = "Sustav upravljanja prijevoznicima", font=('Arial Bold',30))
labelPrijevoznik.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

prijevoznikIDLabel = Label(root,text = "id",font=('Arial',15))
prijevoznikImePrijevoznikaLabel = Label(root,text = "ime_prijevoznika",font=('Arial',15))
prijevoznikKonaktLabel = Label(root,text = "kontakt",font=('Arial',15))
prijevoznikTipVozilaLabel = Label(root,text = "tip_vozila",font=('Arial',15))
prijevoznikRegistarskaOznakaLabel = Label(root,text = "registarska_oznaka",font=('Arial',15))
  

prijevoznikIDLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
prijevoznikImePrijevoznikaLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
prijevoznikKonaktLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
prijevoznikTipVozilaLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
prijevoznikRegistarskaOznakaLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)


prijevoznikIDEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj1Prijevoznik)
prijevoznikImePrijevoznikaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj2Prijevoznik)
prijevoznikKontaktEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj3Prijevoznik)
prijevoznikTipVozilaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj4Prijevoznik)
prijevoznikRegistarskaOznakaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj5Prijevoznik)


prijevoznikIDEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
prijevoznikImePrijevoznikaEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
prijevoznikKontaktEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
prijevoznikTipVozilaEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
prijevoznikRegistarskaOznakaEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)



addBtnPrijevoznik=Button(root, text="Dodaj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=addPrijevoznik)
searchBtnPrijevoznik=Button(root, text="Pretraži",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=searchPrijevoznik)
selectBtnPrijevoznik=Button(root, text="Izaberi",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=selectPrijevoznik)

addBtnPrijevoznik.grid(row=3,column=5,columnspan=1,rowspan=2)
searchBtnPrijevoznik.grid(row=5,column=5,columnspan=1,rowspan=2)
selectBtnPrijevoznik.grid(row=7,column=5,columnspan=1,rowspan=2)

style=ttk.Style()
style.configure("Treeview.Heading",font=('Arial Bold',15))
my_tree3['columns']=("id","ime_prijevoznika","kontakt","tip_vozila","registarska_oznaka")
my_tree3.column('#0',width=0,stretch=NO)

my_tree3.column("id",anchor=W,width=200)
my_tree3.column("ime_prijevoznika",anchor=W,width=200)
my_tree3.column("kontakt",anchor=W,width=200)
my_tree3.column("tip_vozila",anchor=W,width=200)
my_tree3.column("registarska_oznaka",anchor=W,width=200)


my_tree3.heading("id",text="id",anchor=W)
my_tree3.heading("ime_prijevoznika",text="ime_prijevoznika",anchor=W)
my_tree3.heading("kontakt",text="kontakt",anchor=W)
my_tree3.heading("tip_vozila",text="tip_vozila",anchor=W)
my_tree3.heading("registarska_oznaka",text="registarska_oznaka",anchor=W)


refreshTable()

root.mainloop()