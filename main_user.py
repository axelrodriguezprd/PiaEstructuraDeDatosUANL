from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk #pip install pillow en caso de error
import sqlite3

class Student:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema Administrador de Estudiantes")
        #Dimension de la ventana
        self.ventana.geometry("1270x700+0+0")
        #Bloquea el maximiar por el usuario
        self.ventana.resizable(False,False)

        #=====Background Imagen=========
        self.bg=ImageTk.PhotoImage(file="imagenes/uanl_bg.jpg")
        bg=Label(self.ventana,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(self.ventana, text="Sistema Administrador de Estudiantes", bd=10, relief=RAISED, font=("Arial",40,"bold"), bg="black", fg="white")
        title.pack(side=TOP)

        exit_btn=Button(ventana, text="Salir", width=7, bg="red", font=("Arial", 15, "bold"), command=self.mensaje)
        exit_btn.place(x=1150, y=40)

        cambiar_btn=Button(ventana, text="Regresar", width=7, bg="red", font=("Arial", 15, "bold"), command=self.login_window)
        cambiar_btn.place(x=30, y=40)

        #===================VARIABLES===================
        self.matricula_var=StringVar()
        self.nombre_var=StringVar()
        self.appat_var=StringVar()
        self.apmat_var=StringVar()
        self.f_nacimiento_var=StringVar()
        self.curp_var=StringVar()
        self.telefono_var=StringVar()
        self.direccion_var=StringVar()
        self.email_var=StringVar()
        #self.carrera_var=StringVar()

        self.buscar_por=StringVar()
        self.buscar_txt=StringVar()
        #================================================

        #Marco donde vendran los textbox
        Manage_Frame=Frame(self.ventana, bd=4, relief=RIDGE, bg="grey")
        Manage_Frame.place(x=20, y=100, width=520, height=590)

        m_title=Label(Manage_Frame, text="Control de Estudiantes", bg="grey", fg="black", font=("Arial", 18, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)


        #Etiqueta de matricula
        lbl_roll=Label(Manage_Frame, text="Matricula:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para matricula
        txt_roll=Entry(Manage_Frame, textvariable=self.matricula_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de nombre
        lbl_name=Label(Manage_Frame, text="Nombre:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para nombre
        txt_name=Entry(Manage_Frame, textvariable=self.nombre_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de apellido paterno
        lbl_appat=Label(Manage_Frame, text="Primer apellido:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_appat.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para apellido paterno
        txt_appat=Entry(Manage_Frame, textvariable=self.appat_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_appat.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de apellido materno
        lbl_apmat=Label(Manage_Frame, text="Segundo apellido:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_apmat.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para apellido materno
        txt_apmat=Entry(Manage_Frame, textvariable=self.apmat_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_apmat.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de fecha de nacimiento
        lbl_f_nacimiento=Label(Manage_Frame, text="Fecha de nacimiento:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_f_nacimiento.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para fecha de nacimiento
        txt_f_nacimiento=Entry(Manage_Frame, textvariable=self.f_nacimiento_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_f_nacimiento.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de CURP
        lbl_CURP=Label(Manage_Frame, text="CURP:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_CURP.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para CURP
        txt_CURP=Entry(Manage_Frame, textvariable=self.curp_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_CURP.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de telefono
        lbl_telefono=Label(Manage_Frame, text="Telefono:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_telefono.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para telefono
        txt_telefono=Entry(Manage_Frame, textvariable=self.telefono_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_telefono.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de direccion
        lbl_direccion=Label(Manage_Frame, text="Direccion:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_direccion.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para direccion
        txt_direccion=Entry(Manage_Frame, textvariable=self.direccion_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_direccion.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de email
        lbl_email=Label(Manage_Frame,text="Email:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        lbl_email.grid(row=9, column=0, pady=10, padx=20, sticky="w")
        #TextBox de entrada para email
        txt_email=Entry(Manage_Frame,textvariable=self.email_var, font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=9, column=1, pady=10, padx=20, sticky="w")

        #Etiqueta de carrera
        #lbl_carrera=Label(Manage_Frame, text="Carrera:", bg="grey", fg="white", font=("Arial", 8, "bold"))
        #lbl_carrera.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        #ComboBox de carrera
        #combo_carrera=ttk.Combobox(Manage_Frame,textvariable=self.carrera_var, width=9, font=("Arial", 8, "bold"), state='readonly')
        #combo_carrera['values']=("Lic. Tecnologias de la Informacion", "Contador Publico", "Lic. Negocios Internacionales", "Lic. Administracion")
        #combo_carrera.grid(row=10, column=1, padx=20, pady=10)

        #Botones Agregar, Actualiza, Borrar, Limpiar
        btn_frame=Frame(Manage_Frame, bd=4, relief=RIDGE, bg="black")
        btn_frame.place(x=20, y=540, width=420)

        add_btn=Button(btn_frame, text="Agregar", width=7, command=self.agregar_estudiantes)
        add_btn.grid(row=0, column=2, padx=30, pady=0)

        clear_btn=Button(btn_frame, text="Limpiar", width=7, command=self.clear)
        clear_btn.grid(row=0, column=3, padx=20, pady=0)

        #Marco donde vendran los detalles de la tabla
        Detail_Frame=Frame(self.ventana, bd=4, relief=RIDGE, bg="grey")
        Detail_Frame.place(x=550, y=100, width=710, height=580)

        lbl_search=Label(Detail_Frame, text="Buscar por:", bg="grey", fg="black", font=("Arial", 18, "bold"))
        lbl_search.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        #Combobox
        combo_search=ttk.Combobox(Detail_Frame, textvariable=self.buscar_por, width=10, font=("Arial", 12, "bold"), state='readonly')
        combo_search['values']=("Matricula", "Nombre", "Telefono")
        combo_search.grid(row=0, column=1, padx=10, pady=20)

        txt_search=Entry(Detail_Frame, textvariable=self.buscar_txt, width=20, font=("Arial", 11, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        search_btn=Button(Detail_Frame, text="Buscar", width=7, command=self.buscar_data)
        search_btn.grid(row=0, column=4, padx=10, pady=10)

        showall_btn=Button(Detail_Frame, text="Mostrar todo", width=10, command=self.fetch_data)
        showall_btn.grid(row=0, column=5, padx=10, pady=10)

        #Tabla de datos
        table_frame=Frame(Detail_Frame,bd=4, relief=RIDGE, bg="black")
        table_frame.place(x=10, y=70, width=680, height=500)

        scroll_x=Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, columns=("matricula", "nombre", "apellido paterno", "apellido materno", "fecha nacimiento", "curp", "telefono", "direccion", "email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("matricula", text="Matricula")
        self.student_table.heading("nombre", text="Nombre")
        self.student_table.heading("apellido paterno", text="Apellido paterno")
        self.student_table.heading("apellido materno", text="Apellido materno")
        self.student_table.heading("fecha nacimiento", text="Fecha de nacimiento")
        self.student_table.heading("curp", text="CURP")
        self.student_table.heading("telefono", text="Telefono")
        self.student_table.heading("direccion", text="Direccion")
        self.student_table.heading("email", text="Email")
        #self.student_table.heading("carrera", text="Carrera")
        self.student_table['show']='headings'
        #Personalizacion de ancho de cada columna
        self.student_table.column("matricula", width=100)
        self.student_table.column("nombre", width=100)
        self.student_table.column("apellido paterno", width=100)
        self.student_table.column("apellido materno", width=100)
        self.student_table.column("fecha nacimiento", width=100)
        self.student_table.column("curp", width=90)
        self.student_table.column("telefono", width=100)
        self.student_table.column("direccion", width=160)
        self.student_table.column("email", width=100)
        #self.student_table.column("carrera", width=100)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        self.student_table.pack(fill=BOTH, expand=1)

    def agregar_estudiantes(self):
        #Condicion para el messagebox en validacion de los campos
        if self.matricula_var.get() == "" or self.nombre_var.get()=="" or self.f_nacimiento_var=="" or self.curp_var =="" or self.direccion_var=="" or self.email_var.get()== "":
            messagebox.showerror("Error","Todos los campos son requeridos!")
        else:
            con=sqlite3.connect("uanl.db")
            cur=con.cursor()
            cur.execute("INSERT INTO alumnos(matricula,nombre, apellido_p, apellido_m, f_nacimiento, curp, telefono, direccion, email)VALUES('"+self.matricula_var.get()+"','"+self.nombre_var.get()+"','"+self.appat_var.get()+"','"+self.apmat_var.get()+"','"+self.f_nacimiento_var.get()+"','"+self.curp_var.get()+"','"+self.telefono_var.get()+"','"+self.direccion_var.get()+"','"+self.email_var.get()+"')")
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Exito", "Se agrego correctamente el registro!")


    def fetch_data(self):
        con=sqlite3.connect("uanl.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM alumnos")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.matricula_var.set("")
        self.nombre_var.set("")
        self.appat_var.set("")
        self.apmat_var.set("")
        self.f_nacimiento_var.set("")
        self.curp_var.set("")
        self.telefono_var.set("")
        self.direccion_var.set("")
        self.email_var.set("")
        #self.carrera_var.set("")

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.matricula_var.set(row[0])
        self.nombre_var.set(row[1])
        self.appat_var.set(row[2])
        self.apmat_var.set(row[3])
        self.f_nacimiento_var.set(row[4])
        self.curp_var.set(row[5])
        self.telefono_var.set(row[6])
        self.direccion_var.set(row[7])
        self.email_var.set(row[8])
        #self.carrera_var.set(row[9])

    def update_data(self):
        #Condicion para el messagebox en validacion de los campos
        if self.matricula_var.get() == "" or self.nombre_var.get()=="" or self.f_nacimiento_var=="" or self.curp_var =="" or self.direccion_var=="" or self.email_var.get()== "":
            messagebox.showerror("Error","Seleccione el registro que desea actualizar.")
        else:
            con=sqlite3.connect("uanl.db")
            cur=con.cursor()
            cur.execute("UPDATE alumnos SET nombre='"+self.nombre_var.get()+"', apellido_p='"+self.appat_var.get()+"', apellido_m='"+self.apmat_var.get()+"', f_nacimiento='"+self.f_nacimiento_var.get()+"', curp='"+self.curp_var.get()+"', telefono='"+self.telefono_var.get()+"', direccion='"+self.direccion_var.get()+"', email='"+self.email_var.get()+"' WHERE matricula='"+self.matricula_var.get()+"'")
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Actualizado", "Se actualizo correctamente el registro!")
    
    def delete_data(self):
        #Condicion para el messagebox en validacion de los campos
        if self.matricula_var.get() == "" or self.nombre_var.get()=="" or self.f_nacimiento_var=="" or self.curp_var =="" or self.direccion_var=="" or self.email_var.get()== "":
            messagebox.showerror("Error","Seleccione el registro que desea eliminar.")
        else:
            con=sqlite3.connect("uanl.db")
            cur=con.cursor()
            cur.execute("DELETE FROM alumnos WHERE matricula='"+self.matricula_var.get()+"'")
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Eliminado", "Se elimino correctamente el registro!")

    def buscar_data(self):
        con=sqlite3.connect("uanl.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM alumnos WHERE "+str(self.buscar_por.get())+" LIKE '%"+str(self.buscar_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def mensaje(self):
        #Funcion que pregunta si desea salir del programa
        answer = messagebox.askyesno("Salir", "¿Desea salir del sistema?")
        if answer:
            ventana.destroy()        
    
    def login_window(self):
        self.ventana.destroy()
        import login

ventana = Tk()
ob = Student(ventana)
ventana.mainloop()