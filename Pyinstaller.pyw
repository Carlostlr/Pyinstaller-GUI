from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import subprocess


root=Tk()
root.geometry("+450+200")
root.title("Compilador")


def abreficheros():
    ''' Funcion para buscar nuestro programa e insertar la ruta del mismo en un campo text '''

    global fichero

    fichero=filedialog.askopenfilename(title="Programas Python", initialdir="C:", filetypes=(("Python","*.py*"),("Todos los ficheros","*.*")))

    fichero='"'+fichero+'"'

    program.delete("1.0", END)
    program.insert(INSERT, fichero)



def abreimagenes():
    ''' Funcion para buscar un icono para nuestro programa e insertar la ruta del mismo en un campo text '''

    global foto

    foto=filedialog.askopenfilename(title="Imagenes", initialdir="C:", filetypes=(("Imágen PNG","*.png*"),("Imágen ICO","*.ico*"),("Todos los ficheros","*.*")))

    icon.delete("1.0", END)
    icon.insert(INSERT, foto)


def compila():
    ''' Funcion para compilar el programa, si se ha seleccionado una imagen pasará al else directamente si no entrara en el if para hacerlo sin ella '''

    program.delete("1.0", END)
    icon.delete("1.0", END)

    if foto=="":
        try:
            ruta="pyinstaller --onefile --noconsole "+fichero
            prom=os.system(ruta)
            messagebox.showinfo("Pyinstaller","Su programa se ha compilado correctamente.")
        except:
            print("Ha fallado")
    else:
        try:
            ruta="pyinstaller --onefile --noconsole --icon="+foto+" "+fichero
            prom=os.system(ruta)
            messagebox.showinfo("Pyinstaller","Su programa se ha compilado correctamente.")
        except:
            print("Ha fallado")


''' creamos las variables para usarlas en las funciones anteriores '''

fichero=""
foto=""

''' Creamos el menú'''

def help():
    messagebox.showinfo("Ayuda","Este programa sirve para compilar programas creados en Python 3.\n\n ¡¡¡¡¡ ATENCIÓN !!!!!\n\n No añadir iconos a la ventana de tkinter porque fallará.")

#creamos la barra de MENU y de indicamos que va a estar asociado a la raiz root
barraMenus=Menu(root)

#le asignamos el menu barraMenus a la raiz root
root.config(menu=barraMenus)

#creamos los elementos del menu y le asignamos su nombre
ayuda=Menu(barraMenus, tearoff=0)
barraMenus.add_cascade(label="Ayuda", menu=ayuda)

#creamos los elementos del menu Ayuda
ayuda.add_command(label="Ayuda", command=help)

#-------------------------------------------------------------------

Label(root,text="Seleccione su programa para compilar",font=("Arial", 13)).grid(row=0,columnspan=4,padx=10,pady=10)

#-------------------------------------------------------------------

program=Text(root,width=25,height=1,font=("Arial", 10))
program.grid(row=2,column=2,padx=5,pady=5)

scrollprogram=Scrollbar(root,orient=HORIZONTAL,command=program.yview)
scrollprogram.grid(row=2,column=3)
program.config(yscrollcommand=scrollprogram.set)

buscafichero=Button(root, text="Programa", command=abreficheros)
buscafichero.grid(row=2,column=1,padx=10,pady=10)

#--------------------------------------------------------------------

icon=Text(root,width=25,height=1,font=("Arial", 10))
icon.grid(row=3,column=2,padx=5,pady=5)

scrollicon=Scrollbar(root,orient=HORIZONTAL,command=icon.yview)
scrollicon.grid(row=3,column=3)
icon.config(yscrollcommand=scrollicon.set)

icono=Button(root, text="Icono", command=abreimagenes)
icono.grid(row=3,column=1,padx=10,pady=10)

#------------------------------------------------------------------

compilar=Button(root, text="Compilar", command=compila)
compilar.grid(row=4,column=2,padx=10,pady=10)


''' instalara pyinstaller, con la libreria subprocess utilizamos la clausula where para comprobar si pyinstaller existe o no, si existe devovlera 0,
si no existe devolvera 1'''

rc=subprocess.call(['where','pyinstaller'])

if rc==0:
    print("Está instalado")

else:
    print(rc)
    exi=messagebox.askokcancel("Pyinstaller","El programa PyInstaller no está instalado ¿Desea instalarlo en este momento? si no lo instala no funcionara este compilador.")

    if exi==True:
        prom=os.system("pip install pyinstaller")

    else:
        messagebox.showinfo("Pyinstaller","Pyinstaller no se instalará, por lo tanto este programa no podrá funcionar, por favor, instalelo.")
        root.destroy()

root.mainloop()
