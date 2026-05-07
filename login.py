from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Ensure these files (main.py and register.py) exist in the same folder
from main import Face_Recognition_System
from register import Register

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Face Recognition System")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.var_email = StringVar()
        self.var_password = StringVar()

        # Background Image
        img_bg = Image.open(r"d:\New Folder\istockphoto-1964406389-612x612.webp")
        img_bg = img_bg.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, width=1550, height=800)

        # Login Frame
        login_frame = Frame(self.root, bg="white", bd=5, relief=RIDGE)
        login_frame.place(x=550, y=150, width=450, height=500)

        # User Icon / Logo
        img_logo = Image.open(r"d:\New Folder\dev.jpg") 
        img_logo = img_logo.resize((100, 100), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(img_logo)
        lbl_logo = Label(login_frame, image=self.logo, bg="white")
        lbl_logo.place(x=175, y=20, width=100, height=100)

        get_started = Label(login_frame, text="Get Started", font=("times new roman", 25, "bold"), fg="black", bg="white")
        get_started.place(x=140, y=130)

        # Email Entry
        lbl_email = Label(login_frame, text="Email Address", font=("times new roman", 15, "bold"), fg="grey", bg="white")
        lbl_email.place(x=50, y=200)
        self.txt_email = ttk.Entry(login_frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=50, y=230, width=350, height=35)

        # Password Entry
        lbl_pass = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), fg="grey", bg="white")
        lbl_pass.place(x=50, y=280)
        self.txt_pass = ttk.Entry(login_frame, textvariable=self.var_password, font=("times new roman", 15), show="*")
        self.txt_pass.place(x=50, y=310, width=350, height=35)

        # Checkbutton for Show Password
        self.var_check = IntVar()
        check_btn = Checkbutton(login_frame, text="Show Password", variable=self.var_check, command=self.show_pass, font=("times new roman", 10, "bold"), bg="white", activebackground="white")
        check_btn.place(x=50, y=350)

        # Login Button
        btn_login = Button(login_frame, text="Login", command=self.login_logic, font=("times new roman", 18, "bold"), bg="darkblue", fg="white", cursor="hand2")
        btn_login.place(x=50, y=400, width=350, height=45)

        # Register Button (Linked to function)
        lbl_reg = Button(login_frame, text="New User? Register Here", command=self.register_window, font=("times new roman", 12), bg="white", fg="blue", bd=0, cursor="hand2", activebackground="white")
        lbl_reg.place(x=150, y=460)
    

    # ========================== Functions ==========================

    def show_pass(self):
        if self.var_check.get() == 1:
            self.txt_pass.config(show="")
        else:
            self.txt_pass.config(show="*")

    def login_logic(self):
        if self.var_email.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
                curr = conn.cursor()
                query = "SELECT * FROM users WHERE email=%s AND password=%s"
                curr.execute(query, (self.var_email.get(), self.var_password.get()))
                row = curr.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome {row[0]}!", parent=self.root)
                    self.open_dashboard() 
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Connection Error: {str(e)}", parent=self.root)

    def open_dashboard(self):
        self.root.destroy() # Close login
        main_root = Tk()
        self.app = Face_Recognition_System(main_root)
        main_root.mainloop()

    
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)    

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()