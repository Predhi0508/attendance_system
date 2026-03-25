from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background image
        bg_img = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\bgg.webp")
        bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image=self.bg_img)
        bg_lbl.place(x=0, y=0, width=1530, height=790)

         #top frame
        self.top_frame = Frame(self.root, bg="black")
        self.top_frame.place(x=0, y=0, width=1530, height=180)

           #first image
        img=Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\student.webp")
        img=img.resize((510,180), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=180)

          #Second Image
        img1=Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\download.webp")
        img1=img1.resize((510,180), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=180)
        
        #Third Image
        img2=Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\student 2.webp")
        img2=img2.resize((510,180), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=510,height=180)

        title_lbl = Label(
            self.root,
            text="STUDENT DETAILS",
            font=("Helvetica", 28, "bold"),
            bg="#3017bd",
            fg="white"
        )
        title_lbl.place(x=0, y=180, width=1530, height=50)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=240, width=1510, height=500)


        # left label Frame
        left_frame = LabelFrame(main_frame, text="Student Information", font=("Helvetica", 12, "bold"))
        left_frame.place(x=0, y=0, width=750, height=500)

    #   Main Frame
       main_frame = Frame(self.root, bd=2, bg="white")
       main_frame.place(x=10, y=240, width=1510, height=500)

      # Right Label Frame
      right_frame = LabelFrame(
      main_frame,
      text="Student Records",
      font=("Helvetica", 12, "bold"),
      bg="white",
      fg="black",
      bd=2,
     relief=RIDGE
      )
    
    right_frame.place(x=760, y=0, width=750, height=500)
       #Right label Frame
    




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()  

