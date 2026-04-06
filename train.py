from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Training")

        # Title (y=0)
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top 3 Images (Starting at y=45 so title is visible)
        # First image
        img = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\facial-recognition-attendance-system.jpg")
        img = img.resize((510, 180), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=510, height=180)

        # Second Image
        img1 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\170864455-d1ca33f4-5424-44f3-b359-297fc560c0b0.png")
        img1 = img1.resize((510, 180), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=510, y=45, width=510, height=180)

        # Third Image
        img2 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\1_FW2rw68RCH1DyT6soXgNNQ.jpg")
        img2 = img2.resize((510, 180), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1020, y=45, width=510, height=180)

        # Train Button (Placed in the middle gap)
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=225, width=1530, height=60)

        # Bottom Image (Moved up slightly to look better)
        img_bottom = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\training data.webp")
        img_bottom = img_bottom.resize((1530, 500), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
        f_lbl_bottom.place(x=0, y=285, width=1530, height=500)

    def train_classifier(self):
        data_dir = ("data")
        # Ensure the data folder exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "No 'data' folder found!")
            return
            
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []

        for image in path:
            if not image.endswith((".jpg", ".png", ".jpeg")):
                continue
                
            img = Image.open(image).convert('L') # Convert to gray scale
            imageNp = np.array(img, 'uint8')
            
            # Extract ID from filename (e.g., user.1.1.jpg -> ID 1)
            try:
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)==13
            except:
                continue
        
        if not faces:
            messagebox.showerror("Error", "No training data found in 'data' folder!")
            return

        ids = np.array(ids)

        # ================== Train the classifier and save ==================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data Set Completed Successfully!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()