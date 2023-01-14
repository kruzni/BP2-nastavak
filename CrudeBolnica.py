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
    for data in my_tree1.get_children():
        my_tree1.delete(data)
        
    for array in readBolnica():
        my_tree1.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
        
    my_tree1.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
    my_tree1.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
    
#GUI

root = Tk()
root.title("Bolnica")
root.geometry("1920x1080")
root.iconbitmap("krv.ico")
root['bg'] = '#9E5D5D'

#rezervirana mjesta za upis
rezmj1Bolnica=tk.StringVar()
rezmj2Bolnica=tk.StringVar()
rezmj3Bolnica=tk.StringVar()
rezmj4Bolnica=tk.StringVar()
rezmj5Bolnica=tk.StringVar()
rezmj6Bolnica=tk.StringVar()
rezmj7Bolnica=tk.StringVar()
rezmj8Bolnica=tk.StringVar()
rezmj9Bolnica=tk.StringVar()
rezmj10Bolnica=tk.StringVar()
rezmj11Bolnica=tk.StringVar()
rezmj12Bolnica=tk.StringVar()
rezmj13Bolnica=tk.StringVar()
rezmj14Bolnica=tk.StringVar()

#postavljanje vrijednosti za rez mjesta

def postRezMjBolnica(rijecBolnica, brojBolnica):
    if brojBolnica == 1:
        rezmj1Bolnica.set(rijecBolnica)
    if brojBolnica == 2:
        rezmj2Bolnica.set(rijecBolnica)
    if brojBolnica == 3:
        rezmj3Bolnica.set(rijecBolnica)
    if brojBolnica == 4:
        rezmj4Bolnica.set(rijecBolnica)
    if brojBolnica == 5:
        rezmj5Bolnica.set(rijecBolnica)
    if brojBolnica == 6:
        rezmj6Bolnica.set(rijecBolnica)
    if brojBolnica == 7:
        rezmj7Bolnica.set(rijecBolnica)
    if brojBolnica == 8:
        rezmj8Bolnica.set(rijecBolnica)
    if brojBolnica == 9:
        rezmj9Bolnica.set(rijecBolnica)
    if brojBolnica == 10:
        rezmj10Bolnica.set(rijecBolnica)
    if brojBolnica == 11:
        rezmj11Bolnica.set(rijecBolnica)
    if brojBolnica == 12:
        rezmj12Bolnica.set(rijecBolnica)
    if brojBolnica == 13:
        rezmj13Bolnica.set(rijecBolnica)
    if brojBolnica == 14:
        rezmj14Bolnica.set(rijecBolnica)
       

#funkcije

def readBolnica():
    connBolnica=connection()
    cursor=connBolnica.cursor()
    cursor.execute("SELECT * FROM bolnica")
    rezultat=cursor.fetchall()
    connBolnica.commit()
    connBolnica.close()
    return rezultat

def addBolnica():
    id=str(bolnicaIDEntry.get())
    naziv=str(bolnicaIDEntry.get())
    adresa=str(bolnicaIDEntry.get())
    grad=str(bolnicaIDEntry.get())
    kontakt=str(bolnicaIDEntry.get())
    email=str(bolnicaIDEntry.get())
    zaliha_krvne_grupe_A_poz=str(zaliha_Krvne_Grupe_A_PozEntry.get())
    zaliha_krvne_grupe_A_neg=str(zaliha_Krvne_Grupe_A_NegEntry.get())
    zaliha_krvne_grupe_B_poz=str(zaliha_Krvne_Grupe_B_PozEntry.get())
    zaliha_krvne_grupe_B_neg=str(zaliha_Krvne_Grupe_B_NegEntry.get())
    zaliha_krvne_grupe_AB_poz=str(zaliha_Krvne_Grupe_AB_PozEntry.get())
    zaliha_krvne_grupe_AB_neg=str(zaliha_Krvne_Grupe_AB_NegEntry.get())
    zaliha_krvne_grupe_0_poz=str(zaliha_Krvne_Grupe_0_PozEntry.get())
    zaliha_krvne_grupe_0_neg=str(zaliha_Krvne_Grupe_0_NegEntry.get())
    
    
    if (id=="" or id==" ") or (naziv=="" or naziv==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ")or (zaliha_krvne_grupe_A_poz=="" or zaliha_krvne_grupe_A_poz==" ") or (zaliha_krvne_grupe_A_neg=="" or zaliha_krvne_grupe_A_neg==" ") or (zaliha_krvne_grupe_B_poz=="" or zaliha_krvne_grupe_B_poz==" ") or (zaliha_krvne_grupe_B_neg=="" or zaliha_krvne_grupe_B_neg==" ") or (zaliha_krvne_grupe_AB_poz=="" or zaliha_krvne_grupe_AB_poz==" ") or (zaliha_krvne_grupe_AB_neg=="" or zaliha_krvne_grupe_AB_neg==" ") or (zaliha_krvne_grupe_0_poz=="" or zaliha_krvne_grupe_0_poz==" ") or (zaliha_krvne_grupe_0_neg=="" or zaliha_krvne_grupe_0_neg==" "):
        messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
        return
    else:
        try:
            connBolnica=connection()
            cursorBolnica=connBolnica.cursor()
            cursorBolnica.execute("INSERT INTO bolnica VALUES ('"+id+"','"+naziv+"','"+adresa+"','"+grad+"','"+kontakt+"','"+email+"','"+zaliha_krvne_grupe_A_poz+"','"+zaliha_krvne_grupe_A_neg+"','"+zaliha_krvne_grupe_B_poz+"','"+zaliha_krvne_grupe_B_neg+"','"+zaliha_krvne_grupe_AB_poz+"','"+zaliha_krvne_grupe_AB_neg+"','"+zaliha_krvne_grupe_0_poz+"','"+zaliha_krvne_grupe_0_neg+"') ")
            connBolnica.commit()
            connBolnica.close()
        except:
            messagebox.showinfo("Pogreška!","Id bolnice već postoji!")
            return
        
    refreshTable()
    
def resetBolnica():
    odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati sve podatke")
    if odluka != "Da":
        return
    else:
        try:
            connBolnica=connection()
            cursorBolnica=connBolnica.cursor()
            cursorBolnica.execute("DELETE FROM bolnica")
            connBolnica.commit()
            connBolnica.close()
        except:
            messagebox.showinfo("Pogreška!","Nema podataka za izbrisati!")
            return
        
    refreshTable()

def deleteBolnica():
    odluka=messagebox.askquestion("Upozorenje!!","Želite li izbrisati bolnicu?")
    if odluka != "yes":
        return
    else:
        odabrana_bolnica=my_tree1.selection()[0]
        izbrisiPodatak=str(my_tree1.item(odabrana_bolnica)['values'][0])
        connBolnica=connection()
        cursorBolnica=connBolnica.cursor()
        query = "DELETE FROM bolnica WHERE id = %s"
        cursorBolnica.execute(query, (izbrisiPodatak,))
        connBolnica.commit()
        cursorBolnica.close()
        connBolnica.close()
        messagebox.showinfo("Info","Bolnica uspješno izbrisana!")
    refreshTable()
    
def selectBolnica():
        try:
            odabrana_bolnica=my_tree1.selection()[0]
            id=str(my_tree1.item(odabrana_bolnica)['values'][0])
            naziv=str(my_tree1.item(odabrana_bolnica)['values'][1])
            adresa=str(my_tree1.item(odabrana_bolnica)['values'][2])
            grad=str(my_tree1.item(odabrana_bolnica)['values'][3])
            kontakt=str(my_tree1.item(odabrana_bolnica)['values'][4])
            email=str(my_tree1.item(odabrana_bolnica)['values'][5])
            zaliha_krvne_grupe_A_poz=str(my_tree1.item(odabrana_bolnica)['values'][6])
            zaliha_krvne_grupe_A_neg=str(my_tree1.item(odabrana_bolnica)['values'][7])
            zaliha_krvne_grupe_B_poz=str(my_tree1.item(odabrana_bolnica)['values'][8])
            zaliha_krvne_grupe_B_neg=str(my_tree1.item(odabrana_bolnica)['values'][9])
            zaliha_krvne_grupe_AB_poz=str(my_tree1.item(odabrana_bolnica)['values'][10])
            zaliha_krvne_grupe_AB_neg=str(my_tree1.item(odabrana_bolnica)['values'][11])
            zaliha_krvne_grupe_0_poz=str(my_tree1.item(odabrana_bolnica)['values'][12])
            zaliha_krvne_grupe_0_neg=str(my_tree1.item(odabrana_bolnica)['values'][13])
        
            postRezMjBolnica(id,1)
            postRezMjBolnica(naziv,2)
            postRezMjBolnica(adresa,3)
            postRezMjBolnica(grad,4)
            postRezMjBolnica(kontakt,5)
            postRezMjBolnica(email,6)
            postRezMjBolnica(zaliha_krvne_grupe_A_poz,7)
            postRezMjBolnica(zaliha_krvne_grupe_A_neg,8)
            postRezMjBolnica(zaliha_krvne_grupe_B_poz,9)
            postRezMjBolnica(zaliha_krvne_grupe_B_neg,10)
            postRezMjBolnica(zaliha_krvne_grupe_AB_poz,11)
            postRezMjBolnica(zaliha_krvne_grupe_AB_neg,12)
            postRezMjBolnica(zaliha_krvne_grupe_0_poz,13)
            postRezMjBolnica(zaliha_krvne_grupe_0_neg,14)
        except:
            messagebox.showinfo("Pogreška!","Molimo izaberite podatak")
            
def searchBolnica():
    id=str(bolnicaIDEntry.get())
    naziv=str(bolnicaIDEntry.get())
    adresa=str(bolnicaIDEntry.get())
    grad=str(bolnicaIDEntry.get())
    kontakt=str(bolnicaIDEntry.get())
    email=str(bolnicaIDEntry.get())
    zaliha_krvne_grupe_A_poz=str(zaliha_Krvne_Grupe_A_PozEntry.get())
    zaliha_krvne_grupe_A_neg=str(zaliha_Krvne_Grupe_A_NegEntry.get())
    zaliha_krvne_grupe_B_poz=str(zaliha_Krvne_Grupe_B_PozEntry.get())
    zaliha_krvne_grupe_B_neg=str(zaliha_Krvne_Grupe_B_NegEntry.get())
    zaliha_krvne_grupe_AB_poz=str(zaliha_Krvne_Grupe_AB_PozEntry.get())
    zaliha_krvne_grupe_AB_neg=str(zaliha_Krvne_Grupe_AB_NegEntry.get())
    zaliha_krvne_grupe_0_poz=str(zaliha_Krvne_Grupe_0_PozEntry.get())
    zaliha_krvne_grupe_0_neg=str(zaliha_Krvne_Grupe_0_NegEntry.get())
    if id is None or id == "":
        id = '%'
    if naziv is None or naziv == "":
        naziv = '%'
    if adresa is None or adresa == "":
        adresa = '%'
    if grad is None or grad == "":
        grad = '%'
    if kontakt is None or kontakt == "":
        kontakt = '%'
    if email is None or email == "":
        email = '%'
    if zaliha_krvne_grupe_A_poz is None or zaliha_krvne_grupe_A_poz == "":
        zaliha_krvne_grupe_A_poz = '%'
    if zaliha_krvne_grupe_A_neg is None or zaliha_krvne_grupe_A_neg == "":
        zaliha_krvne_grupe_A_neg = '%'
    if zaliha_krvne_grupe_B_poz is None or zaliha_krvne_grupe_B_poz == "":
        zaliha_krvne_grupe_B_poz = '%'
    if zaliha_krvne_grupe_B_neg is None or zaliha_krvne_grupe_B_neg == "":
        zaliha_krvne_grupe_B_neg = '%'
    if zaliha_krvne_grupe_AB_poz is None or zaliha_krvne_grupe_AB_poz == "":
        zaliha_krvne_grupe_AB_poz = '%'
    if zaliha_krvne_grupe_AB_neg is None or zaliha_krvne_grupe_AB_neg == "":
        zaliha_krvne_grupe_AB_neg = '%'
    if zaliha_krvne_grupe_0_poz is None or zaliha_krvne_grupe_0_poz == "":
        zaliha_krvne_grupe_0_poz = '%'
    if zaliha_krvne_grupe_0_neg is None or zaliha_krvne_grupe_0_neg == "":
        zaliha_krvne_grupe_0_neg = '%'
    connBolnica=connection()
    cursorBolnica=connBolnica.cursor()
    query = "SELECT * FROM bolnica WHERE id like %s or naziv like %s or adresa like %s or grad like %s or kontakt like %s or email like %s or zaliha_krvne_grupe_A_poz like %s or zaliha_krvne_grupe_A_neg like %s or zaliha_krvne_grupe_B_poz like %s  or zaliha_krvne_grupe_B_neg like %s or zaliha_krvne_grupe_AB_poz like %s or zaliha_krvne_grupe_AB_neg like %s or zaliha_krvne_grupe_0_poz like %s or zaliha_krvne_grupe_0_neg like %s" 
    cursorBolnica.execute(query, (id, naziv, adresa, grad, kontakt, email, zaliha_krvne_grupe_A_poz, zaliha_krvne_grupe_A_neg, zaliha_krvne_grupe_B_poz, zaliha_krvne_grupe_B_neg, zaliha_krvne_grupe_AB_poz, zaliha_krvne_grupe_AB_neg, zaliha_krvne_grupe_0_poz, zaliha_krvne_grupe_0_neg))
    rows = cursorBolnica.fetchall()
    match = False
    for row in rows:
        if str(row[0]) == id:
            match = True
            for i in range(0,9):
                postRezMjBolnica(row[i],(i+1))
    if not match:
        messagebox.showinfo("Pogreška!","Nema odgovarajućeg podatka!")
    connBolnica.commit()
    connBolnica.close()
    
def updateBolnica():
    try:
        odabrana_bolnica=my_tree1.selection()[0]
        odabranaBolnica=str(my_tree1.item(odabrana_bolnica)['values'][0])
    except:
        messagebox.showinfo("Pogreška!","Odaberite bolnicu!")
        return
        
    id=str(bolnicaIDEntry.get())
    naziv=str(nazivEntry.get())
    adresa=str(adresaEntry.get())
    grad=str(gradEntry.get())
    kontakt=str(kontaktEntry.get())
    email=str(emailEntry.get())
    zaliha_krvne_grupe_A_poz=str(zaliha_Krvne_Grupe_A_PozEntry.get())
    zaliha_krvne_grupe_A_neg=str(zaliha_Krvne_Grupe_A_NegEntry.get())
    zaliha_krvne_grupe_B_poz=str(zaliha_Krvne_Grupe_B_PozEntry.get())
    zaliha_krvne_grupe_B_neg=str(zaliha_Krvne_Grupe_B_NegEntry.get())
    zaliha_krvne_grupe_AB_poz=str(zaliha_Krvne_Grupe_AB_PozEntry.get())
    zaliha_krvne_grupe_AB_neg=str(zaliha_Krvne_Grupe_AB_NegEntry.get())
    zaliha_krvne_grupe_0_poz=str(zaliha_Krvne_Grupe_0_PozEntry.get())
    zaliha_krvne_grupe_0_neg=str(zaliha_Krvne_Grupe_0_NegEntry.get())
    
    if (id=="" or id==" ") or (naziv=="" or naziv==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (email=="" or email==" ")or (zaliha_krvne_grupe_A_poz=="" or zaliha_krvne_grupe_A_poz==" ") or (zaliha_krvne_grupe_A_neg=="" or zaliha_krvne_grupe_A_neg==" ") or (zaliha_krvne_grupe_B_poz=="" or zaliha_krvne_grupe_B_poz==" ") or (zaliha_krvne_grupe_B_neg=="" or zaliha_krvne_grupe_B_neg==" ") or (zaliha_krvne_grupe_AB_poz=="" or zaliha_krvne_grupe_AB_poz==" ") or (zaliha_krvne_grupe_AB_neg=="" or zaliha_krvne_grupe_AB_neg==" ") or (zaliha_krvne_grupe_0_poz=="" or zaliha_krvne_grupe_0_poz==" ") or (zaliha_krvne_grupe_0_neg=="" or zaliha_krvne_grupe_0_neg==" "):
        messagebox.showinfo("Pogreška!","Molimo upotpunite prazan obrazac!")
        return
    else:
        try:
            connBolnica=connection()
            cursorBolnica=connBolnica.cursor()
            cursorBolnica.execute(f"UPDATE bolnica SET id='{id}', naziv='{naziv}', adresa='{adresa}', grad='{grad}', kontakt='{kontakt}', email='{email}', zaliha_krvne_grupe_A_poz='{zaliha_krvne_grupe_A_poz}', zaliha_krvne_grupe_A_neg='{zaliha_krvne_grupe_A_neg}', zaliha_krvne_grupe_B_poz='{zaliha_krvne_grupe_B_poz}', zaliha_krvne_grupe_B_neg='{zaliha_krvne_grupe_B_neg}', zaliha_krvne_grupe_AB_poz='{zaliha_krvne_grupe_AB_poz}', zaliha_krvne_grupe_AB_neg='{zaliha_krvne_grupe_AB_neg}', zaliha_krvne_grupe_0_poz='{zaliha_krvne_grupe_0_poz}', zaliha_krvne_grupe_0_neg='{zaliha_krvne_grupe_0_neg}' WHERE id={odabranaBolnica}")
            connBolnica.commit()
            connBolnica.close()
            refreshTable()
        except Exception as e:
            messagebox.showinfo("Pogreška!", f"Došlo je do problema prilikom ažuriranja podataka.\n Razlog: {e}")
        return
    

#GUI
my_tree1 = ttk.Treeview(root)
frame1BolnicaAdmin = Frame(root)
frame1BolnicaAdmin['bg'] = '#9E5D5D'
frame2 = Frame(root)

frame1BolnicaAdmin.grid(row = 0, column = 0, sticky='nsew')
frame2.grid(row = 0, column = 1, sticky='nsew')

labelBolnica = Label(frame1BolnicaAdmin, text = "Sustav upravljanja bolnicama", font=('Arial Bold',20))
labelBolnica.grid(row=5,column=3,columnspan=50,rowspan=5,padx=60,pady=30)

bolnicaIDLabel = Label(frame1BolnicaAdmin,text = "id",font=('Arial',11))
bolnicaNazivLabel = Label(frame1BolnicaAdmin,text = "Naziv bolnice",font=('Arial',11)) 
bolnicaAdresaLabel = Label(frame1BolnicaAdmin,text = "Adresa bolnice",font=('Arial',11)) 
bolnicaGradLabel = Label(frame1BolnicaAdmin,text = "Grad bolnice",font=('Arial',11)) 
bolnicaKontaktLabel = Label(frame1BolnicaAdmin,text = "Kontakt bolnice",font=('Arial',11)) 
bolnicaEmailLabel = Label(frame1BolnicaAdmin,text = "Email bolnice",font=('Arial',11)) 
bolnicaZalihaKrvneGrupeAPoz = Label(frame1BolnicaAdmin,text= "A+",font=('Arial',11))
bolnicaZalihaKrvneGrupeANeg = Label(frame1BolnicaAdmin,text= "A-",font=('Arial',11))
bolnicaZalihaKrvneGrupeBPoz = Label(frame1BolnicaAdmin,text= "B+",font=('Arial',11))
bolnicaZalihaKrvneGrupeBNeg = Label(frame1BolnicaAdmin,text= "B-",font=('Arial',11))
bolnicaZalihaKrvneGrupeABPoz = Label(frame1BolnicaAdmin,text= "AB+",font=('Arial',11))
bolnicaZalihaKrvneGrupeABNeg = Label(frame1BolnicaAdmin,text= "AB-",font=('Arial',11))
bolnicaZalihaKrvneGrupe0Poz = Label(frame1BolnicaAdmin,text= "0+",font=('Arial',11))
bolnicaZalihaKrvneGrupe0Neg = Label(frame1BolnicaAdmin,text= "0-",font=('Arial',11)) 

bolnicaIDLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
bolnicaNazivLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
bolnicaAdresaLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
bolnicaGradLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
bolnicaKontaktLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
bolnicaEmailLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupeAPoz.grid(row=9,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupeANeg.grid(row=10,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupeBPoz.grid(row=11,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupeBNeg.grid(row=12,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupeABPoz.grid(row=13,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupeABNeg.grid(row=14,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupe0Poz.grid(row=15,column=0,columnspan=1,padx=50,pady=5)
bolnicaZalihaKrvneGrupe0Neg.grid(row=16,column=0,columnspan=1,padx=50,pady=5)

bolnicaIDEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj1Bolnica)
nazivEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj2Bolnica)
adresaEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj3Bolnica)
gradEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj4Bolnica)
kontaktEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj5Bolnica)
emailEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj6Bolnica)
zaliha_Krvne_Grupe_A_PozEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj7Bolnica)
zaliha_Krvne_Grupe_A_NegEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj8Bolnica)
zaliha_Krvne_Grupe_B_PozEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj9Bolnica)
zaliha_Krvne_Grupe_B_NegEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj10Bolnica)
zaliha_Krvne_Grupe_AB_PozEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj11Bolnica)
zaliha_Krvne_Grupe_AB_NegEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj12Bolnica)
zaliha_Krvne_Grupe_0_PozEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj13Bolnica)
zaliha_Krvne_Grupe_0_NegEntry=Entry(frame1BolnicaAdmin,width=55,bd=3,font=('Arial',11), textvariable=rezmj14Bolnica)


bolnicaIDEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
nazivEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
adresaEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
gradEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
kontaktEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
emailEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_A_PozEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_A_NegEntry.grid(row=10,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_B_PozEntry.grid(row=11,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_B_NegEntry.grid(row=12,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_AB_PozEntry.grid(row=13,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_AB_NegEntry.grid(row=14,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_0_PozEntry.grid(row=15,column=1,columnspan=4,padx=5,pady=0)
zaliha_Krvne_Grupe_0_NegEntry.grid(row=16,column=1,columnspan=4,padx=5,pady=0)


addBtnBolnica=Button(frame1BolnicaAdmin, text="Dodaj",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=addBolnica)
updateBtnBolnica=Button(frame1BolnicaAdmin, text="Ažuriraj",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=updateBolnica)
deleteBtnBolnica=Button(frame1BolnicaAdmin, text="Izbriši",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=deleteBolnica)
searchBtnBolnica=Button(frame1BolnicaAdmin, text="Pretraži",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=searchBolnica)
resetBtnBolnica=Button(frame1BolnicaAdmin, text="Resetiraj",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=resetBolnica)
selectBtnBolnica=Button(frame1BolnicaAdmin, text="Izaberi",padx=25,pady=25,width=5,bd=5,font=('Arial',15),bg="white",fg="red", command=selectBolnica)

addBtnBolnica.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtnBolnica.grid(row=3,column=7,columnspan=1,rowspan=2)
deleteBtnBolnica.grid(row=3,column=9,columnspan=1,rowspan=2)
searchBtnBolnica.grid(row=3,column=11,columnspan=1,rowspan=2)
resetBtnBolnica.grid(row=3,column=13,columnspan=1,rowspan=2)
selectBtnBolnica.grid(row=3,column=15,columnspan=1,rowspan=2)

my_tree1 = ttk.Treeview(root, columns=("id","naziv","adresa","grad","kontakt","email","zaliha_krvne_grupe_A_poz","zaliha_krvne_grupe_A_neg","zaliha_krvne_grupe_B_poz","zaliha_krvne_grupe_B_neg","zaliha_krvne_grupe_AB_poz","zaliha_krvne_grupe_AB_neg","zaliha_krvne_grupe_0_poz","zaliha_krvne_grupe_0_neg"), displaycolumns=("id","naziv","adresa","grad","kontakt","email","zaliha_krvne_grupe_A_poz","zaliha_krvne_grupe_A_neg","zaliha_krvne_grupe_B_poz","zaliha_krvne_grupe_B_neg","zaliha_krvne_grupe_AB_poz","zaliha_krvne_grupe_AB_neg","zaliha_krvne_grupe_0_poz","zaliha_krvne_grupe_0_neg"))
my_tree1.grid(column=1, row=0)
my_tree1.column('#0',width=0,stretch=NO)


my_tree1.column("id",anchor=W,width=170)
my_tree1.column("naziv",anchor=W,width=170)
my_tree1.column("adresa",anchor=W,width=170)
my_tree1.column("grad",anchor=W,width=170)
my_tree1.column("kontakt",anchor=W,width=170)
my_tree1.column("email",anchor=W,width=170)
my_tree1.column("zaliha_krvne_grupe_A_poz",anchor=W,width=50)
my_tree1.column("zaliha_krvne_grupe_A_neg",anchor=W,width=50)
my_tree1.column("zaliha_krvne_grupe_B_poz",anchor=W,width=50)
my_tree1.column("zaliha_krvne_grupe_B_neg",anchor=W,width=50)
my_tree1.column("zaliha_krvne_grupe_AB_poz",anchor=W,width=50)
my_tree1.column("zaliha_krvne_grupe_AB_neg",anchor=W,width=50)
my_tree1.column("zaliha_krvne_grupe_0_poz",anchor=W,width=50)
my_tree1.column("zaliha_krvne_grupe_0_neg",anchor=W,width=50)


my_tree1.heading("id",text="id",anchor=W)
my_tree1.heading("naziv",text="naziv",anchor=W)
my_tree1.heading("adresa",text="adresa",anchor=W)
my_tree1.heading("grad",text="grad",anchor=W)
my_tree1.heading("kontakt",text="kontakt",anchor=W)
my_tree1.heading("email",text="email",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_A_poz",text="zaliha_krvne_grupe_A_poz",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_A_neg",text="zaliha_krvne_grupe_A_neg",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_B_poz",text="zaliha_krvne_grupe_B_poz",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_B_neg",text="zaliha_krvne_grupe_B_neg",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_AB_poz",text="zaliha_krvne_grupe_AB_poz",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_AB_neg",text="zaliha_krvne_grupe_AB_neg",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_0_poz",text="zaliha_krvne_grupe_0_poz",anchor=W)
my_tree1.heading("zaliha_krvne_grupe_0_neg",text="zaliha_krvne_grupe_0_neg",anchor=W)


refreshTable()

root.mainloop()