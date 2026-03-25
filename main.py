from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
import os

class Face_Recgnition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background image
        bg_img = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\istockphoto-1964406389-612x612.webp")
        bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image=self.bg_img)
        bg_lbl.place(x=0, y=0, width=1530, height=790)

         #top frame
        self.top_frame = Frame(self.root, bg="black")
        self.top_frame.place(x=0, y=0, width=1530, height=180)

           #first image
        img=Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\facial-recognition-attendance-system.jpg")
        img=img.resize((510,180), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=180)

          #Second Image
        img1=Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\170864455-d1ca33f4-5424-44f3-b359-297fc560c0b0.png")
        img1=img1.resize((510,180), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=180)
        
        #Third Image
        img2=Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\1_FW2rw68RCH1DyT6soXgNNQ.jpg")
        img2=img2.resize((510,180), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=510,height=180)


        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Helvetica", 28, "bold"),
            bg="#0b1c3d",
            fg="white"
        )
        title_lbl.place(x=0, y=180, width=1530, height=50)

        #Student Button
        img4 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\premium_photo-1683887034473-74e486cdb7a1.avif")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root, image=self.photo4, command=self.student_details, cursor="hand2", activebackground="white")
        b1.place(x=100, y=250, width=220, height=220)
        
        b1_lbl = Button(self.root, text="Student Details", command=self.student_details, cursor="hand2", 
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b1_lbl.place(x=100, y=470, width=220, height=40)
        
         #Face Detector Button

        img5 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\istockphoto-1139859279-612x612.webp")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo5 = ImageTk.PhotoImage(img5)

        b2 = Button(self.root, image=self.photo5, command=self.face_data, cursor="hand2", activebackground="white")
        b2.place(x=400, y=250, width=220, height=220)
        
        b2_lbl = Button(self.root, text="Face Detector", command=self.face_data, cursor="hand2", 
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b2_lbl.place(x=400, y=470, width=220, height=40)

         #Attendance Button
        img6 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\istockphoto-1268517553-612x612.webp")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo6 = ImageTk.PhotoImage(img6)

        b3 = Button(self.root, image=self.photo6, command=self.attendance_data, cursor="hand2", activebackground="white")
        b3.place(x=730, y=250, width=220, height=220)
        
        b3_lbl = Button(self.root, text="Attendance", command=self.attendance_data, cursor="hand2", 
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b3_lbl.place(x=730, y=470, width=220, height=40)
       #Chatbot Button
        img7 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\chatbot.webp")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo7 = ImageTk.PhotoImage(img7)

        b4 = Button(self.root, image=self.photo7, command=self.chatbot_data, cursor="hand2", activebackground="white")
        b4.place(x=1040, y=250, width=220, height=220)
        
        b4_lbl = Button(self.root, text="Chatbot", command=self.chatbot_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b4_lbl.place(x=1040, y=470, width=220, height=40)

        #Train Data
        img8 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\train data.webp")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo8 = ImageTk.PhotoImage(img8)


        b4 = Button(self.root, image=self.photo8, command=self.train_data, cursor="hand2", activebackground="white")
        b4.place(x=100, y=520, width=220, height=220) 

        b4_lbl = Button(self.root, text="Train Data", command=self.train_data, cursor="hand2", 
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b4_lbl.place(x=100, y=740, width=220, height=40)

        
        #photos
        img9 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\photos.png")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo9 = ImageTk.PhotoImage(img9)

        b5 = Button(self.root, image=self.photo9, command=self.open_img, cursor="hand2", activebackground="white")
        b5.place(x=400, y=520, width=220, height=220)
        b5_lbl = Button(self.root, text="Photos", command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b5_lbl.place(x=400, y=740, width=220, height=40)

        #Developers 
        img10 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\dev.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo10 = ImageTk.PhotoImage(img10)

        b6 = Button(self.root, image=self.photo10, command=self.developers_data, cursor="hand2", activebackground="white")
        b6.place(x=730, y=520, width=220, height=220)

        b6_lbl = Button(self.root, text="Developers", command=self.developers_data, cursor="hand2",
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b6_lbl.place(x=730, y=740, width=220, height=40)

        #Exit Button
        img11 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\ee.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo11 = ImageTk.PhotoImage(img11)

        b7 = Button(self.root, image=self.photo11, command=self.exit_data, cursor="hand2", activebackground="white")
        b7.place(x=1040, y=520, width=220, height=220)

        b7_lbl = Button(self.root, text="Exit", command=self.exit_data, cursor="hand2",
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white", activebackground="white")
        b7_lbl.place(x=1040, y=740, width=220, height=40)




    def student_details(self):
        messagebox.showinfo("Button Clicked", "Student Details Section opened!")

    def face_data(self):
        messagebox.showinfo("Button Clicked", "Face Detector Section opened!")

    def attendance_data(self):
        messagebox.showinfo("Button Clicked", "Attendance Section opened!") 

    def chatbot_data(self):
        messagebox.showinfo("Button Clicked", "Chatbot Section opened!") 

    def train_data(self):
        messagebox.showinfo("Button Clicked", "Train Data Section opened!")    
    def photos_data(self):
        messagebox.showinfo("Button Clicked", "Photos Section opened!")
    def developers_data(self):
        messagebox.showinfo("Button Clicked", "Developers Section opened!")
    def exit_data(self):
        self.root.quit()
# This finds the 'data' folder inside the current directory of the script
    def open_img(self):
        path= os.path.join(os.getcwd(), "data")
        if os.path.exists(path):
            os.startfile(path)
        else:
            from tkinter import messagebox
            messagebox.showerror("Error", "The 'data' folder does not exist in the project directory.")
    #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recgnition_System(root)
    root.mainloop()  



        

