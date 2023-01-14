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
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    for array in read():
        my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
        
    my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
    my_tree.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
    
#GUI

root = Tk()
root.title("Zaposlenik")
root.geometry("1920x1080")
root.iconbitmap("krv.ico")
my_tree = ttk.Treeview(root)

#rezervirana mjesta za upis
rezmj1=tk.StringVar()
rezmj2=tk.StringVar()
rezmj3=tk.StringVar()
rezmj4=tk.StringVar()
rezmj5=tk.StringVar()
rezmj6=tk.StringVar()
rezmj7=tk.StringVar()
rezmj8=tk.StringVar()
rezmj9=tk.StringVar()

#postavljanje vrijednosti za rez mjesta

def postRezMj(rijec, broj):
    if broj == 1:
        rezmj1.set(rijec)
    if broj == 2:
        rezmj2.set(rijec)
    if broj == 3:
        rezmj3.set(rijec)
    if broj == 4:
        rezmj4.set(rijec)
    if broj == 5:
        rezmj5.set(rijec)
    if broj == 6:
        rezmj6.set(rijec)
    if broj == 7:
        rezmj7.set(rijec)
    if broj == 8:
        rezmj8.set(rijec)
    if broj == 9:
        rezmj9.set(rijec)    

#funkcije

def read():
    conn=connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM zaposlenik")
    rez=cursor.fetchall()
    conn.commit()
    conn.close()
    return rez

def add():
    id=str(zaposlenikIDEntry.get())
    ime=str(zaposlenikImeEntry.get())
    prezime=str(zaposlenikPrezimeEntry.get())
    datum_rodenja=str(zaposlenikDatumRodenjaEntry.get())
    adresa=str(zaposlenikAdresaEntry.get())
    grad=str(zaposlenikGradEntry.get())
    kontakt=str(zaposlenikKontaktEntry.get())
    email=str(zaposlenikEmailEntry.get())
    datum_zaposlenja=str(zaposlenikDatumZaposlenjaEntry.get())
    
    if (id=="" or id==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ") or (datum_zaposlenja=="" or datum_zaposlenja==" "):
        messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
        return
    else:
        try:
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("INSERT INTO zaposlenik VALUES ('"+id+"','"+ime+"','"+prezime+"','"+datum_rodenja+"','"+adresa+"','"+grad+"','"+kontakt+"','"+email+"','"+datum_zaposlenja+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Pogreška!","Id zaposlenika već postoji!")
            return
        
    refreshTable()
    
def reset():
    odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati sve podatke")
    if odluka != "Da":
        return
    else:
        try:
            conn=connection()
            cursor=conn.cursor()
            cursor.execute("DELETE FROM zaposlenik")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Pogreška!","Nema podataka za izbrisati!")
            return
        
    refreshTable()

def delete():
    odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati zaposlenika")
    if odluka != "yes":
        return
    else:
        odabrani_zaposlenik=my_tree.selection()[0]
        izbrisiPodatak=str(my_tree.item(odabrani_zaposlenik)['values'][0])
        conn=connection()
        cursor=conn.cursor()
        query = "DELETE FROM zaposlenik WHERE id = %s"
        cursor.execute(query, (izbrisiPodatak,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Info","Zaposlenik uspješno izbrisan!")
    refreshTable()
    
def select():
        try:
            odabrani_zaposlenik=my_tree.selection()[0]
            id=str(my_tree.item(odabrani_zaposlenik)['values'][0])
            ime=str(my_tree.item(odabrani_zaposlenik)['values'][1])
            prezime=str(my_tree.item(odabrani_zaposlenik)['values'][2])
            datum_rodenja=str(my_tree.item(odabrani_zaposlenik)['values'][3])
            adresa=str(my_tree.item(odabrani_zaposlenik)['values'][4])
            grad=str(my_tree.item(odabrani_zaposlenik)['values'][5])
            kontakt=str(my_tree.item(odabrani_zaposlenik)['values'][6])
            email=str(my_tree.item(odabrani_zaposlenik)['values'][7])
            datum_zaposlenja=str(my_tree.item(odabrani_zaposlenik)['values'][8])
        
            postRezMj(id,1)
            postRezMj(ime,2)
            postRezMj(prezime,3)
            postRezMj(datum_rodenja,4)
            postRezMj(adresa,5)
            postRezMj(grad,6)
            postRezMj(kontakt,7)
            postRezMj(email,8)
            postRezMj(datum_zaposlenja,9)
        except:
            messagebox.showinfo("Pogreška!","Molimo izaberite podatak")
            
def search():
    id=str(zaposlenikIDEntry.get())
    ime=str(zaposlenikImeEntry.get())
    prezime=str(zaposlenikPrezimeEntry.get())
    datum_rodenja=str(zaposlenikDatumRodenjaEntry.get())
    adresa=str(zaposlenikAdresaEntry.get())
    grad=str(zaposlenikGradEntry.get())
    kontakt=str(zaposlenikKontaktEntry.get())
    email=str(zaposlenikEmailEntry.get())
    datum_zaposlenja=str(zaposlenikDatumZaposlenjaEntry.get())
    if id is None or id == "":
        id = '%'
    if ime is None or ime == "":
        ime = '%'
    if prezime is None or prezime == "":
        prezime = '%'
    if datum_rodenja is None or datum_rodenja == "":
        datum_rodenja = '%'
    if adresa is None or adresa == "":
        adresa = '%'
    if grad is None or grad == "":
        grad = '%'
    if kontakt is None or kontakt == "":
        kontakt = '%'
    if email is None or email == "":
        email = '%'
    if datum_zaposlenja is None or datum_zaposlenja == "":
        datum_zaposlenja = '%'
    conn=connection()
    cursor=conn.cursor()
    query = "SELECT * FROM zaposlenik WHERE id like %s or ime like %s or prezime like %s or datum_rodenja like %s or adresa like %s or grad like %s or kontakt like %s or email like %s or datum_zaposlenja like %s"
    cursor.execute(query, (id, ime, prezime, datum_rodenja, adresa, grad, kontakt, email, datum_zaposlenja))
    rows = cursor.fetchall()
    match = False
    for row in rows:
        if str(row[0]) == id:
            match = True
            for i in range(0,9):
                postRezMj(row[i],(i+1))
    if not match:
        messagebox.showinfo("Pogreška!","Nema odgovarajućeg podatka!")
    conn.commit()
    conn.close()
    
def update():
    try:
        odabrani_zaposlenik=my_tree.selection()[0]
        odabraniZaposlenik=str(my_tree.item(odabrani_zaposlenik)['values'][0])
    except:
        messagebox.showinfo("Pogreška!","Odaberite zaposlenika!")
        return
        
    id=str(zaposlenikIDEntry.get())
    ime=str(zaposlenikImeEntry.get())
    prezime=str(zaposlenikPrezimeEntry.get())
    datum_rodenja=str(zaposlenikDatumRodenjaEntry.get())
    adresa=str(zaposlenikAdresaEntry.get())
    grad=str(zaposlenikGradEntry.get())
    kontakt=str(zaposlenikKontaktEntry.get())
    email=str(zaposlenikEmailEntry.get())
    datum_zaposlenja=str(zaposlenikDatumZaposlenjaEntry.get())
    
    if (id=="" or id==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ") or (datum_zaposlenja=="" or datum_zaposlenja==" "):
        messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
        return
    else:
        try:
            conn=connection()
            cursor=conn.cursor()
            cursor.execute(f"UPDATE zaposlenik SET id='{id}', ime='{ime}', prezime='{prezime}', datum_rodenja='{datum_rodenja}', adresa='{adresa}', grad='{grad}', kontakt='{kontakt}', email='{email}', datum_zaposlenja='{datum_zaposlenja}' WHERE id={odabraniZaposlenik}")
            conn.commit()
            conn.close()
            refreshTable()
        except Exception as e:
            messagebox.showinfo("Pogreška!", f"Došlo je do problema prilikom ažuriranja podataka.\n Razlog: {e}")
        return
    

#GUI
frameZaposlenikAdmin = Frame(root)
frameZaposlenikAdmin.grid(row = 0, column = 0, sticky='nsew')
frameZaposlenikAdmin['bg'] = '#9E5D5D'
frame2 = Frame(root) 
frame2.grid(row = 0, column = 1, sticky='nsew')


label = Label(frameZaposlenikAdmin, text = "Sustav upravljanja zaposlenicima", font=('Arial Bold',30))
label.grid(row=0,column=0,columnspan=1,rowspan=1,padx=1,pady=1)

zaposlenikIDLabel = Label(frameZaposlenikAdmin,text = "id",font=('Arial',15))
zaposlenikImeLabel = Label(frameZaposlenikAdmin,text = "Ime zaposlenika",font=('Arial',15)) 
zaposlenikPrezimeLabel = Label(frameZaposlenikAdmin,text = "Prezime zaposlenika",font=('Arial',15)) 
zaposlenikDatumRodenjaLabel = Label(frameZaposlenikAdmin,text = "Datum rođenja zaposlenika",font=('Arial',15)) 
zaposlenikAdresaLabel = Label(frameZaposlenikAdmin,text = "Adresa zaposlenika",font=('Arial',15)) 
zaposlenikGradLabel = Label(frameZaposlenikAdmin,text = "Grad zaposlenika",font=('Arial',15)) 
zaposlenikKontaktLabel = Label(frameZaposlenikAdmin,text = "Kontakt zaposlenika",font=('Arial',15)) 
zaposlenikEmailLabel = Label(frameZaposlenikAdmin,text = "Email zaposlenika",font=('Arial',15)) 
zaposlenikDatumZaposlenjaLabel = Label(frameZaposlenikAdmin,text = "Datum zaposlenja zaposlenika",font=('Arial',15))


zaposlenikIDLabel.grid(row=1,column=0,columnspan=1,padx=50,pady=5)
zaposlenikImeLabel.grid(row=2,column=0,columnspan=1,padx=50,pady=5)
zaposlenikPrezimeLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
zaposlenikDatumRodenjaLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
zaposlenikAdresaLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
zaposlenikGradLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
zaposlenikKontaktLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
zaposlenikEmailLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
zaposlenikDatumZaposlenjaLabel.grid(row=9,column=0,columnspan=1,padx=50,pady=5)

zaposlenikIDEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj1)
zaposlenikImeEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj2)
zaposlenikPrezimeEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj3)
zaposlenikDatumRodenjaEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj4)
zaposlenikAdresaEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj5)
zaposlenikGradEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj6)
zaposlenikKontaktEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj7)
zaposlenikEmailEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj8)
zaposlenikDatumZaposlenjaEntry=Entry(frameZaposlenikAdmin,width=55,bd=5,font=('Arial',15), textvariable=rezmj9)

zaposlenikIDEntry.grid(row=1,column=1,columnspan=4,padx=5,pady=0)
zaposlenikImeEntry.grid(row=2,column=1,columnspan=4,padx=5,pady=0)
zaposlenikPrezimeEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
zaposlenikDatumRodenjaEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
zaposlenikAdresaEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
zaposlenikGradEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
zaposlenikKontaktEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
zaposlenikEmailEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
zaposlenikDatumZaposlenjaEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)


addBtn=Button(frameZaposlenikAdmin, text="Dodaj",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=add)
updateBtn=Button(frameZaposlenikAdmin, text="Ažuriraj",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=update)
deleteBtn=Button(frameZaposlenikAdmin, text="Izbriši",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=delete)
searchBtn=Button(frameZaposlenikAdmin, text="Pretraži",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=search)
resetBtn=Button(frameZaposlenikAdmin, text="Resetiraj",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=reset)
selectBtn=Button(frameZaposlenikAdmin, text="Izaberi",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=select)

addBtn.grid(row=1,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
deleteBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
resetBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=11,column=5,columnspan=1,rowspan=2)

style=ttk.Style()
style.configure("Treeview.Heading",font=('Arial Bold',15))
my_tree['columns']=("id","ime","prezime","datum_rodenja","adresa","grad","kontakt","email","datum_zaposlenja")
my_tree.column('#0',width=0,stretch=NO)

my_tree.column("id",anchor=W,width=170)
my_tree.column("ime",anchor=W,width=170)
my_tree.column("prezime",anchor=W,width=170)
my_tree.column("datum_rodenja",anchor=W,width=170)
my_tree.column("adresa",anchor=W,width=170)
my_tree.column("grad",anchor=W,width=170)
my_tree.column("kontakt",anchor=W,width=170)
my_tree.column("email",anchor=W,width=170)
my_tree.column("datum_zaposlenja",anchor=W,width=200)

my_tree.heading("id",text="id",anchor=W)
my_tree.heading("ime",text="ime",anchor=W)
my_tree.heading("prezime",text="prezime",anchor=W)
my_tree.heading("datum_rodenja",text="datum_rodenja",anchor=W)
my_tree.heading("adresa",text="adresa",anchor=W)
my_tree.heading("grad",text="grad",anchor=W)
my_tree.heading("kontakt",text="kontakt",anchor=W)
my_tree.heading("email",text="email",anchor=W)
my_tree.heading("datum_zaposlenja",text="datum_zaposlenja",anchor=W)

refreshTable()

root.mainloop()