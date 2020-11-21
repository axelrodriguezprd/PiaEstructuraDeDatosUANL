from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk #pip install pillow en caso de error
import sqlite3

class Register:
    def __init__(self,root):
        #Metodo contstrucor
        self.root=root
        self.root.title("Formulario de Registro de Usuarios")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #=====Background Imagen=========
        self.bg=ImageTk.PhotoImage(file="imagenes/uanl_bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #=====Imagen Izquierda========
        self.left=ImageTk.PhotoImage(file="imagenes/logo.jpg")
        left=Label(self.root,image=self.left,bg="white").place(x=80,y=100,width=400,height=500)

        #=======Frame de registro=========
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTRA EL USUARIO AQUI", font=("times new roman",20,"bold"),bg="white", fg="green").place(x=50,y=30)

        #======Fila 1======
        self.var_fname=StringVar()
        f_name=Label(frame1, text="Nombre", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_fname)
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1, text="Apellidos", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #======Fila 2======
        contact=Label(frame1, text="Telefono", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1, text="E-mail", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        #======Fila 3=======
        question=Label(frame1,text="Pregunta de Seguridad", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)

        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly', justify=CENTER)
        self.cmb_quest['values']=("Seleccionar", "Nombre de tu mascota", "Lugar de nacimiento", "Nombre de mejor amigo")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1, text="Respuesta", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1, font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #======Fila4=========
        password=Label(frame1,text="Contraseña",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("time new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirmar contraseña",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("time new roman",15),bg="lightgray",show="*")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        #======Fila5==========
        priv=Label(frame1,text="Privilegio", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=380)
        self.cmb_priv=ttk.Combobox(frame1,font=("times new roman",13),state='readonly', justify=CENTER)
        self.cmb_priv['values']=("Seleccionar", "Administrador", "Usuario")
        self.cmb_priv.place(x=50,y=410,width=250)
        self.cmb_priv.current(0)

        #======Admin checbox=======
        self.var_chk = IntVar()
        chk=Checkbutton(frame1,text="Acepto los terminos & condiciones",bg="white",font=("times new roman",12),variable=self.var_chk, onvalue=1, offvalue=0).place(x=370,y=410)
        
        btn_register=Button(frame1,cursor="hand2",command=self.register_data,text="Registrar",font=("times new roman",14),bg="green",fg="white").place(x=50,y=450)
        btn_login=Button(self.root,text="¿Ya tienes cuenta?\nIngresar",command=self.login_window,font=("times new roman",16),bd=0, cursor="hand2",bg="red",fg="white").place(x=200,y=520,width=180)

    def login_window(self):
        #Metodo que cierra la ventana actual y abre la de login
        self.root.destroy()
        import login

    def clear(self):
        #Metodo que vacia los campos
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)
        self.cmb_priv.current(0)

    def register_data(self):
        #Metodo que registra los datos
        #Verifica que los campos no esten vacios, de ser asi marcara error
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email=="" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.cmb_quest.get()=="Seleccionar" or self.cmb_priv.get()=="Seleccionar":
            messagebox.showerror("Error", "Todos los campos son requeridos", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            #Verifica que las contrasenas coincidan
            messagebox.showerror("Error","Las contraseñas no coinciden", parent=self.root)
        elif self.var_chk.get()==0:
            #Verifica que este activada el checkbox de terminos y condiciones
            messagebox.showerror("Error","Por favor, acepta los terminos & condiciones", parent=self.root)
        else:
            try:
                #Intenta conectar, consultar el email de la tabla usuarios
                con = sqlite3.connect("uanl.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM usuarios WHERE email='"+self.txt_email.get()+"'")
                row=cur.fetchone()
                #Si el email ya existe en la tabla entonces marca error
                if row!=None:
                    messagebox.showerror("Error",f"Usuario ya existe\nPor favor, ingrese otro Email", parent=self.root)
                else:
                    cur.execute("INSERT INTO usuarios(p_nombre,apellidos,telefono,email,question,answer,privilegio,password) VALUES('"+self.txt_fname.get()+"','"+self.txt_lname.get()+"','"+self.txt_contact.get()+"','"+self.txt_email.get()+"','"+self.cmb_quest.get()+"','"+self.txt_answer.get()+"','"+self.cmb_priv.get()+"','"+self.txt_password.get()+"')")
                    con.commit()
                    con.close()
                    messagebox.showinfo("Exito","Registro Satisfactorio", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error debido a: {str(es)}", parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()