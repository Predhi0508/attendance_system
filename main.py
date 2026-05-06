from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Import your other files
from student import Student
from train import Train 
from face_recognition import Face_Recognition
from Attendance import Attendance
from help import helpdesk
from chatbot import ChatBot

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # --- BACKGROUND IMAGE ---
        bg_img = Image.open(r"d:\New Folder\istockphoto-1964406389-612x612.webp")
        bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root, image=self.bg_img)
        bg_lbl.place(x=0, y=0, width=1530, height=790)

        # --- TOP HEADER IMAGES ---
        img1 = Image.open(r"d:\New Folder\facial-recognition-attendance-system.jpg")
        img1 = img1.resize((510, 180), Image.Resampling.LANCZOS)
        self.p1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.p1).place(x=0, y=0, width=510, height=180)

        img2 = Image.open(r"d:\New Folder\170864455-d1ca33f4-5424-44f3-b359-297fc560c0b0.png")
        img2 = img2.resize((510, 180), Image.Resampling.LANCZOS)
        self.p2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.p2).place(x=510, y=0, width=510, height=180)
        
        img3 = Image.open(r"d:\New Folder\istockphoto-1139859279-612x612.webp")
        img3 = img3.resize((510, 180), Image.Resampling.LANCZOS)
        self.p3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.p3).place(x=1020, y=0, width=510, height=180)

        # --- TITLE BAR ---
        title_lbl = Label(self.root, text="SMART FACE RECOGNITION ATTENDANCE SYSTEM", font=("Helvetica", 28, "bold"), bg="#0b1c3d", fg="white")
        title_lbl.place(x=0, y=180, width=1530, height=50)

        # --- BUTTONS ROW 1 ---
        # Student Details
        img_s = Image.open(r"d:\New Folder\ssss.webp").resize((220, 220), Image.Resampling.LANCZOS)
        self.ps = ImageTk.PhotoImage(img_s)
        Button(self.root, image=self.ps, command=self.student_details, cursor="hand2").place(x=100, y=250, width=220, height=220)
        Button(self.root, text="Student Details", command=self.student_details, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=100, y=470, width=220, height=40)
        
        # Face Recognition
        img_f = Image.open(r"d:\New Folder\train.jpg").resize((220, 220), Image.Resampling.LANCZOS)
        self.pf = ImageTk.PhotoImage(img_f)
        Button(self.root, image=self.pf, command=self.face_rec, cursor="hand2").place(x=400, y=250, width=220, height=220)
        Button(self.root, text="Face Recognition", command=self.face_rec, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=400, y=470, width=220, height=40)

        # Attendance
        img_a = Image.open(r"d:\New Folder\scsc.png").resize((220, 220), Image.Resampling.LANCZOS)
        self.pa = ImageTk.PhotoImage(img_a)
        Button(self.root, image=self.pa, command=self.attendance_details, cursor="hand2").place(x=730, y=250, width=220, height=220)
        Button(self.root, text="Attendance", command=self.attendance_details, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=730, y=470, width=220, height=40)

        # Chatbot
        img_c = Image.open(r"d:\New Folder\chatbot.webp").resize((220, 220), Image.Resampling.LANCZOS)
        self.pc = ImageTk.PhotoImage(img_c)
        Button(self.root, image=self.pc, command=self.chatbot_open, cursor="hand2").place(x=1040, y=250, width=220, height=220)
        Button(self.root, text="Chatbot", command=self.chatbot_open, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=1040, y=470, width=220, height=40)

        # --- BUTTONS ROW 2 ---
        # Train Data
        img_t = Image.open(r"d:\New Folder\mind.avif").resize((220, 220), Image.Resampling.LANCZOS)
        self.pt = ImageTk.PhotoImage(img_t)
        Button(self.root, image=self.pt, command=self.train_data_page, cursor="hand2").place(x=100, y=520, width=220, height=220) 
        Button(self.root, text="Train Data", command=self.train_data_page, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=100, y=740, width=220, height=40)

        # Photos Folder
        img_ph = Image.open(r"d:\New Folder\si.jpg").resize((220, 220), Image.Resampling.LANCZOS)
        self.pph = ImageTk.PhotoImage(img_ph)
        Button(self.root, image=self.pph, command=self.open_photos, cursor="hand2").place(x=400, y=520, width=220, height=220)
        Button(self.root, text="Photos", command=self.open_photos, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=400, y=740, width=220, height=40)

        # Help
        img_h = Image.open(r"d:\New Folder\hp.webp").resize((220, 220), Image.Resampling.LANCZOS)
        self.ph = ImageTk.PhotoImage(img_h)
        Button(self.root, image=self.ph, command=self.help_page, cursor="hand2").place(x=730, y=520, width=220, height=220)
        Button(self.root, text="Help Desk", command=self.help_page, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=730, y=740, width=220, height=40)

        # Exit
        img_e = Image.open(r"d:\New Folder\ee.jpg").resize((220, 220), Image.Resampling.LANCZOS)
        self.pe = ImageTk.PhotoImage(img_e)
        Button(self.root, image=self.pe, command=self.exit_system, cursor="hand2").place(x=1040, y=520, width=220, height=220)
        Button(self.root, text="Exit", command=self.exit_system, font=("times", 15, "bold"), bg="darkblue", fg="white").place(x=1040, y=740, width=220, height=40)

    # --- BUTTON FUNCTIONS ---
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def train_data_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def chatbot_open(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)

    def help_page(self):
        self.new_window = Toplevel(self.root)
        self.app = helpdesk(self.new_window)

    def open_photos(self):
        os.startfile("data")

    def exit_system(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()