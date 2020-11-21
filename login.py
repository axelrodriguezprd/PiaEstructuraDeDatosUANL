from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3


class Login_window:
    def __init__(self, login):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #==========Background Colors========================
        self.bg=ImageTk.PhotoImage(file="imagenes/uanl_bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #=========Frames==============================
        login_frame=Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800,height=500)

        title=Label(login_frame,text="Sistema de Logueo", font=("times new roman", 30, "bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="Email", font=("times new roman", 18, "bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame, font=("times new roman", 15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        pass_=Label(login_frame,text="Contraseña", font=("times new roman", 18, "bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame, font=("times new roman", 15),bg="lightgray",show="*")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="¿Registrar nueva cuenta?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=405,y=320)
        btn_login=Button(login_frame, text="Login",command=self.login,font=("times new roman",20, "bold"),fg="white",bg="#B00857",cursor="hand2").place(x=335,y=380,width=180,height=40)

        #self.lbl=Label(self.root, text="Sistema de logueo\nUANL",font=("Book Antiqua",25,"bold"),fg="white",bg="black")

        #self.lbl.place(x=90,y=120,height=450,width=350)

    def register_window(self):
        self.root.destroy()
        import register_user
    
    def main_window(self):
        self.root.destroy()
        import main

    def main_user_window(self):
        self.root.destroy()
        import main_user



    def login(self):
        #Metodo que verifica el login con los datos de la tabla usuarios de la base de datos
        if self.txt_email.get()=="" or self.txt_pass_.get() =="":
            messagebox.showerror("Error", "Todos los campos son requeridos", parent=self.root)
        else:
            try:
                con = sqlite3.connect("uanl.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM usuarios WHERE email='"+self.txt_email.get()+"' AND password='"+self.txt_pass_.get()+"'")
                row=cur.fetchone()
                #print(row)
                if row ==None:
                    messagebox.showerror("Error", "EMAIL y CONTRASEÑA Invalidos!", parent=self.root)
                else:
                    messagebox.showinfo("Exito al entrar", "Bienvenido al sistema!", parent=self.root)
                    #Comprobamos que privilegios tiene
                    if row[7] == "Administrador":
                        self.main_window()
                    elif row[7] == "Usuario":
                        self.main_user_window()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error debido a: {str(es)}", parent=self.root)

root=Tk()
obj=Login_window(root)
root.mainloop()