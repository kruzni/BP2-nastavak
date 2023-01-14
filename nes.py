import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import tkinter as tk
# import CrudeBolnica
# import CrudeBolnicaObicanZaposlenik
# import CrudeZaposlenik
# import CrudeBolnicaZaposlenikSaOvlastima
# import CrudeDarivateljObicanZaposlenik
# import CrudeDarivateljZaposlenikSaOvlastima
# import CrudePrijevoznikObicanZaposlenik
# import CrudePrijevoznikZaposlenikSaOvlastima
# import CrudeZaposlenikObicanZaposlenik
# import CrudeZaposlenikZaposlenikSaOvlastima
# import DarivateljCrude
# import PrijevoznikCrude

def login():
    # Get user input

    user_id = id_entry.get()

    # Connect to database
    conn = pymysql.connect(host="localhost", user="root", password="root", database="baza_banke_krvi")
    cursor = conn.cursor()

    # Execute SQL query to check if the entered ID exists in the database
    cursor.execute("SELECT * FROM zaposlenik WHERE id=%s", (user_id))
    result = cursor.fetchone()
    def admin_options():
        option = tk.StringVar()
        admin_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label="Admin", menu=admin_menu)
        admin_menu.add_radiobutton(label="Option 1", variable=option, value="Option 1", command=lambda: open_gui(option.get()))
        admin_menu.add_radiobutton(label="Option 2", variable=option, value="Option 2", command=lambda: open_gui(option.get()))
        admin_menu.add_radiobutton(label="Option 3", variable=option, value="Option 3", command=lambda: open_gui(option.get()))
    if result:
        # Login successful
        print("Dobrodošli: ", user_id)
        # Create main menu
        main_menu = tk.Menu(root)
        root.config(menu=main_menu)

        # Create submenus
        admin_menu = tk.Menu(main_menu)
        zaposlenikc = tk.Menu(main_menu)
        darivateljc = tk.Menu(main_menu)
        prijevoznikc = tk.Menu(main_menu)
        bolnicac = tk.Menu(main_menu)

        ovlastima_menu = tk.Menu(main_menu)
        zaposlenik_menu = tk.Menu(main_menu)

        # Check the user_id and configure the menu
        if user_id == '1':
                admin_window = Toplevel(root)
                admin_window.geometry("600x600")
                def open_gui(option):
                    if option == "Bolnica":
                        import CrudeBolnica
                        CrudeBolnica.gui()
                    elif option == "Zaposlenik":
                        import CrudeZaposlenik
                        CrudeZaposlenik.gui()
                    elif option == "Prijevoznik":
                        import PrijevoznikCrude
                        PrijevoznikCrude.gui()
                    elif option == "Darivatelj":
                        import DarivateljCrude
                        DarivateljCrude.gui()

                option = tk.StringVar()
                admin_menu = tk.Menu(main_menu)
                main_menu.add_cascade(label="Admin", menu=admin_menu)
                admin_menu.add_radiobutton(label="Bolnica", variable=option, value="Bolnica", command=lambda: open_gui(option.get()))
                admin_menu.add_radiobutton(label="Zaposlenik", variable=option, value="Zaposlenik", command=lambda: open_gui(option.get()))
                admin_menu.add_radiobutton(label="Prijevoznik", variable=option, value="Prijevoznik", command=lambda: open_gui(option.get()))
                admin_menu.add_radiobutton(label="Darivatelj", variable=option, value="Darivatelj", command=lambda: open_gui(option.get()))
        
       #----------------------------------------------------------------------------------------------------------------------------
       
       
       
       
        elif 2 <= int(user_id) <= 10:
            zaposlenik_s_ovlastima_window = Toplevel(root)
            zaposlenik_s_ovlastima_window.geometry("600x600")
            ovlastima_menu = tk.Menu(main_menu)
            main_menu.add_cascade(label="Zaposlenik s ovlastima",menu=ovlastima_menu)
            def open_gui_s_ovlastima(option):
                #Dodaj jos opcija i promjeni importove
                if option == "Bolnica":
                    import CrudeBolnica
                    CrudeBolnica.gui()
                elif option == "Zaposlenik":
                    import CrudeZaposlenik
                    CrudeZaposlenik.gui()
                elif option == "Prijevoznik":
                    import PrijevoznikCrude
                    PrijevoznikCrude.gui()
                elif option == "Darivatelj":
                    import DarivateljCrude
                    DarivateljCrude.gui()
            option = tk.StringVar()
            ovlastima_menu.add_cascade(label="Zaposlenik_S_Ovlastima", menu=ovlastima_menu)
            admin_menu.add_radiobutton(label="Bolnica", variable=option, value="Bolnica", command=lambda: open_gui_s_ovlastima(option.get()))
            admin_menu.add_radiobutton(label="Zaposlenik", variable=option, value="Zaposlenik", command=lambda: open_gui_s_ovlastima(option.get()))
            admin_menu.add_radiobutton(label="Prijevoznik", variable=option, value="Prijevoznik", command=lambda: open_gui_s_ovlastima(option.get()))
            admin_menu.add_radiobutton(label="Darivatelj", variable=option, value="Darivatelj", command=lambda: open_gui_s_ovlastima(option.get()))
        
        
        #_-----------------------------------------------------------------------------------------------------------------------
        
        
        elif 11 <= int(user_id) <= 35:
            main_menu.add_cascade(label="Zaposlenik", menu=zaposlenik_menu)
            zaposlenik_menu.add_command(label="Zaposlenik options", command=lambda: print("Zaposlenik options"))
    else:
        # Login failed
        print("Invalid ID")

    # Close cursor and connection
    cursor.close()
    conn.close()

root = tk.Tk()
root.geometry("600x600")


# Create label and entry for ID
id_label = tk.Label(root, text="ID:")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

# Create login button
login_button = tk.Button(root, text="Prijava", command=login)
login_button.grid(row=1, column=0, columnspan=2)

root.mainloop()