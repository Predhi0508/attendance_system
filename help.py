from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class helpdesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Help Desk")

        # Title
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        img_bg = Image.open(r"d:\New Folder\gg.webp")
        img_bg = img_bg.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        
        bg_lbl = Label(self.root, image=self.photoimg_bg)
        bg_lbl.place(x=0, y=45, width=1530, height=720)

        # ================== ADD THIS PART BELOW ==================
        # This creates the frame that was missing in your code
        main_frame = Frame(bg_lbl, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=515, y=150, width=500, height=350) 
        # =========================================================

        # Now you can put labels inside 'main_frame'
        dev_name = Label(main_frame, text="Email: mattupredhi1809@gmail.com", font=("times new roman", 18, "bold"), bg="white", fg="black")
        dev_name.place(x=0, y=50, width=500)

        help_msg = Label(main_frame, text="Support available 24/7", font=("times new roman", 14, "italic"), bg="white", fg="blue")
        help_msg.place(x=0, y=200, width=500)


if __name__ == "__main__":
    root = Tk()
    obj = helpdesk(root)
    root.mainloop()