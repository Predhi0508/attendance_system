from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st Image (Left)
        img_top = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\R.jpg") 
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=650, height=700)

        # 2nd Image (Right)
        img_bottom = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\picc.jpg") 
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=45, width=950, height=700)

        # Button to start recognition
        b1_1 = Button(f_lbl2, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)

    # ========================== Attendance Marking (Saves to Excel/CSV) ==========================
    def mark_attendance(self, i, r, n, d):
        # Create file if it doesn't exist
        if not os.path.exists("attendance.csv"):
            with open("attendance.csv", "w") as f:
                f.writelines("ID,Roll,Name,Department,Time,Date,Status")

        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0]) # ID is the first column
            
            # Mark attendance only if the person hasn't been marked yet
            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # ========================== Recognition Logic ==========================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))

                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="face_recognizer")
                    my_cursor = conn.cursor()

                    # Single query to get all data (Uses names from your DESCRIBE command)
                    query = "SELECT name, roll_no, department FROM student WHERE student_id=" + str(id)
                    my_cursor.execute(query)
                    row = my_cursor.fetchone()

                    if row:
                        n, r, d = row 
                        if confidence > 77:
                            cv2.putText(img, f"ID: {id}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Roll: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Dept: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            # Record Attendance
                            self.mark_attendance(str(id), r, n, d)
                        else:
                            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
                    conn.close()
                except Exception as es:
                    print(f"Error fetching data: {str(es)}")

            return img

        # Initialize resources
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Classifier.xml not found. Train data first!")
            return

        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            
            img = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            cv2.imshow("Welcome to Face Recognition", img)

            # Close on 'Enter' (13) or clicking 'X' on window
            if cv2.waitKey(1) == 13 or cv2.getWindowProperty("Welcome to Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()