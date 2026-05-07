from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register - Face Recognition System")
        self.root.geometry("1600x900+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background
        img_bg = Image.open(r"d:\New Folder\istockphoto-1964406389-612x612.webp")
        img_bg = img_bg.resize((1600, 900), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(img_bg)
        Label(self.root, image=self.bg).place(x=0, y=0, width=1600, height=900)

        # Register Frame
        frame = Frame(self.root, bg="white", bd=5, relief=RIDGE)
        frame.place(x=550, y=100, width=500, height=550)

        Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg="darkblue", bg="white").place(x=100, y=20)

        # Fields
        Label(frame, text="Full Name", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        Entry(frame, textvariable=self.var_fname, font=("times new roman", 15), bg="lightgrey").place(x=50, y=130, width=400)

        Label(frame, text="Email Address", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=180)
        Entry(frame, textvariable=self.var_email, font=("times new roman", 15), bg="lightgrey").place(x=50, y=210, width=400)

        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=260)
        Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), bg="lightgrey", show="*").place(x=50, y=290, width=400)

        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=340)
        Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), bg="lightgrey", show="*").place(x=50, y=370, width=400)

        # Buttons
        Button(frame, text="Register Now", command=self.register_data, font=("times new roman", 18, "bold"), bg="green", fg="white", cursor="hand2").place(x=50, y=440, width=400)
        
        # Link back to login
        lbl_login = Button(frame, text="Already have an account? Login", command=self.return_login, font=("times new roman", 12), bg="white", fg="blue", bd=0, cursor="hand2")
        lbl_login.place(x=130, y=500)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
                curr = conn.cursor()
                curr.execute("select * from users where email=%s", (self.var_email.get(),))
                if curr.fetchone() != None:
                    messagebox.showerror("Error", "User already exists with this email")
                else:
                    curr.execute("insert into users values(%s,%s,%s)", (self.var_fname.get(), self.var_email.get(), self.var_pass.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully!")
                    self.return_login()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()