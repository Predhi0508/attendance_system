from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Training")

        # Title 
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Images (Ensure paths are correct)
        img_top = Image.open(r"d:\New Folder\facial-recognition-attendance-system.jpg").resize((1530, 180), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=45, width=1530, height=180)

        # Train Button
        b1_1 = Button(self.root, text="CLICK HERE TO TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="darkred", fg="white")
        b1_1.place(x=0, y=225, width=1530, height=60)

        # Bottom Image 
        img_bottom = Image.open(r"d:\New Folder\train.jpg").resize((1530, 500), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=0, y=285, width=1530, height=500)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir) or len(os.listdir(data_dir)) == 0:
            messagebox.showerror("Error", "No training data found in 'data' folder! Please add students and take photos first.")
            return
            
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            if not image.endswith((".jpg", ".png", ".jpeg")):
                continue
                
            img = Image.open(image).convert('L') # Gray scale
            imageNp = np.array(img, 'uint8')
            
            try:
                # Extract ID: user.1.5.jpg -> ID is the middle part (1)
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training in Progress...", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Skipping bad file: {image} Error: {e}")
                continue
        
        # Train and Save
        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Complete! You can now use Face Recognition.")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()