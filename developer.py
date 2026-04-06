from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Developer Info")

        # Title at the top
        title_lbl = Label(self.root, text="DEVELOPER DETAILS", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image (Tech Circuit)
        # Update this path to where your background image is stored
        img_bg = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\dev.webp") 
        img_bg = img_bg.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        
        bg_lbl = Label(self.root, image=self.photoimg_bg)
        bg_lbl.place(x=0, y=45, width=1530, height=720)

        # ================== Main Center Frame ==================
        # Width=500, Height=600. Centered at x=515
        main_frame = Frame(bg_lbl, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=515, y=50, width=500, height=600)

        # 1. Developer Photo
        img_dev = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\girl.webp") 
        img_dev = img_dev.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_dev = ImageTk.PhotoImage(img_dev)
        
        f_lbl_dev = Label(main_frame, image=self.photoimg_dev, bg="white")
        f_lbl_dev.place(x=150, y=20, width=200, height=200)

        # 2. Developer Name & Role
        dev_name = Label(main_frame, text="Hello, My Name is Predhi", font=("times new roman", 20, "bold"), bg="white", fg="black")
        dev_name.place(x=0, y=230, width=500)

        dev_role = Label(main_frame, text="I am a Full Stack Developer", font=("times new roman", 16, "bold"), bg="white", fg="black")
        dev_role.place(x=0, y=270, width=500)

        # 3. Contact Details
        email_lbl = Label(main_frame, text="Email: mattupredhi1809@gmail.com", font=("times new roman", 14), bg="white", fg="black")
        email_lbl.place(x=0, y=340, width=500)

        # LinkedIn (Blue and Underlined)
        linkedin_lbl = Label(main_frame, text="www.linkedin.com/in/predhi-mattu-86780026b", font=("times new roman", 14, "underline"), bg="white", fg="blue", cursor="hand2")
        linkedin_lbl.place(x=0, y=380, width=500)

        # GitHub
        github_lbl = Label(main_frame, text="https://github.com/Predhi0508", font=("times new roman", 14), bg="white", fg="black")
        github_lbl.place(x=0, y=430, width=500)

        # Optional bottom text or branding
        footer_lbl = Label(main_frame, text="© 2024 Face Recognition Project", font=("times new roman", 10, "italic"), bg="white", fg="grey")
        footer_lbl.place(x=0, y=560, width=500)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()