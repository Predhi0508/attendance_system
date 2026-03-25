from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================= Variables =================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_radio1 = StringVar()


    
        # Background image
        try:
            bg_img = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\bgg.webp")
            bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(bg_img)
            bg_lbl = Label(self.root, image=self.bg_img)
            bg_lbl.place(x=0, y=0, width=1530, height=790)
        except Exception as e:
            print(f"Error loading background image: {e}")

        # Top frame for images
        self.top_frame = Frame(self.root, bg="black")
        self.top_frame.place(x=0, y=0, width=1530, height=180)

        # Header Images
        img = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\student.webp")
        img = img.resize((510, 180), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.top_frame, image=self.photoimg).place(x=0, y=0, width=510, height=180)

        img1 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\download.webp")
        img1 = img1.resize((510, 180), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.top_frame, image=self.photoimg1).place(x=510, y=0, width=510, height=180)
        
        img2 = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\Saved Pictures\student 2.webp")
        img2 = img2.resize((510, 180), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.top_frame, image=self.photoimg2).place(x=1020, y=0, width=510, height=180)

        # Title
        title_lbl = Label(self.root, text="STUDENT DETAILS", font=("Helvetica", 28, "bold"), bg="#3017bd", fg="white")
        title_lbl.place(x=0, y=180, width=1530, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=10, y=240, width=1510, height=530)
       
        # Left Label Frame (Information Entry)
        left_frame = LabelFrame(main_frame, text="Student Information", font=("Helvetica", 12, "bold"), bg="white", bd=2, relief=RIDGE)
        left_frame.place(x=10, y=10, width=735, height=510)

        img_left= Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\si.jpg")
        img_left = img_left.resize((720, 160), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=160)

        # Course Information
        course_frame = LabelFrame(left_frame, text="Current Course Information", font=("Helvetica", 11, "bold"), bg="white", bd=2, relief=RIDGE)
        course_frame.place(x=5, y=165, width=720, height=110)

        Label(course_frame, text="Department", font=("Helvetica", 11, "bold"), bg="white").grid(row=0, column=0, padx=10, sticky=W)
        self.combo_dep = ttk.Combobox(course_frame,textvariable=self.var_dep,font=("Helvetica", 11, "bold"), width=17, state="readonly")
        self.combo_dep["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        self.combo_dep.current(0)
        self.combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Label(course_frame, text="Course", font=("Helvetica", 11, "bold"), bg="white").grid(row=0, column=2, padx=10, sticky=W)
        self.combo_course = ttk.Combobox(course_frame,textvariable=self.var_course, font=("Helvetica", 11, "bold"), width=17, state="readonly")
        self.combo_course["values"] = ("Select Course","M.Sc", "B.Sc", "BCA", "MCA", "B.Tech")
        self.combo_course.current(0)
        self.combo_course.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        Label(course_frame, text="Year", font=("Helvetica", 11, "bold"), bg="white").grid(row=1, column=0, padx=10, sticky=W)
        self.combo_year = ttk.Combobox(course_frame,textvariable=self.var_year, font=("Helvetica", 11, "bold"), width=17, state="readonly")
        self.combo_year["values"] = ("Select Year", "2023-24", "2024-25", "2025-26", "2026-27")
        self.combo_year.current(0)
        self.combo_year.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        Label(course_frame, text="Semester", font=("Helvetica", 11, "bold"), bg="white").grid(row=1, column=2, padx=10, sticky=W)
        self.combo_semester = ttk.Combobox(course_frame,textvariable=self.var_semester ,font=("Helvetica", 11, "bold"), width=17, state="readonly")
        self.combo_semester["values"] = ("Select Semester", "Semester-1", "Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        self.combo_semester.current(0)
        self.combo_semester.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student Information Entry
        cs_frame = LabelFrame(left_frame, text="Class Student Information", font=("Helvetica", 11, "bold"), bg="white", bd=2, relief=RIDGE)
        cs_frame.place(x=5, y=280, width=720, height=215)

        Label(cs_frame, text="Student ID:", font=("Helvetica", 11, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=2, sticky=W)
        ttk.Entry(cs_frame, width=15,textvariable=self.var_std_id,font=("Helvetica", 11, "bold")).grid(row=0, column=1, padx=2, pady=2, sticky=W)

        Label(cs_frame, text="Student Name:", font=("Helvetica", 11, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=2, sticky=W)
        ttk.Entry(cs_frame, width=15,textvariable=self.var_std_name,font=("Helvetica", 11, "bold")).grid(row=0, column=3, padx=2, pady=2, sticky=W)

        Label(cs_frame, text="Roll No:", font=("Helvetica", 11, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=2, sticky=W)
        ttk.Entry(cs_frame, width=15,textvariable=self.var_roll ,font=("Helvetica", 11, "bold")).grid(row=1, column=1, padx=2, pady=2, sticky=W)

        Label(cs_frame, text="Gender:", font=("Helvetica", 11, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=2, sticky=W)
        self.combo_gender = ttk.Combobox(cs_frame,textvariable=self.var_gender,font=("Helvetica", 11, "bold"), width=13, state="readonly")
        self.combo_gender["values"] = ("Male", "Female", "Other")
        self.combo_gender.current(0)
        self.combo_gender.grid(row=1, column=3, padx=2, pady=2, sticky=W)

        Label(cs_frame, text="Email:", font=("Helvetica", 11, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=2, sticky=W)
        ttk.Entry(cs_frame, width=15,textvariable=self.var_email ,font=("Helvetica", 11, "bold")).grid(row=2, column=1, padx=2, pady=2, sticky=W)

        Label(cs_frame, text="Phone No:", font=("Helvetica", 11, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=2, sticky=W)
        ttk.Entry(cs_frame, width=15,textvariable=self.var_phone,font=("Helvetica", 11, "bold")).grid(row=2, column=3, padx=2, pady=2, sticky=W)

        radiobtn1 = ttk.Radiobutton(cs_frame, text="Take Photo Sample", variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        radiobtn2 = ttk.Radiobutton(cs_frame, text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Button Frame
        btn_frame = Frame(cs_frame, bd=1, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=155, width=715, height=35)

        Button(btn_frame, text="Save", command=self.add_data, font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=13).grid(row=0, column=0)
        # Update Button
        Button(btn_frame, text="Update", command=self.update_data, font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=13).grid(row=0, column=1)

        # Delete Button (Added command=self.delete_data)
        Button(btn_frame, text="Delete", command=self.delete_data, font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=13).grid(row=0, column=2)

        # Reset Button (Added command=self.reset_data)
        Button(btn_frame, text="Reset", command=self.reset_data, font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=13).grid(row=0, column=3)

        # Take photo Button (Link this to your dataset generation function later)
        Button(btn_frame, text="Take photo", command=self.generate_dataset, font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=13).grid(row=0, column=4)

        # Update photo Button
        Button(btn_frame, text="Update photo", font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=13).grid(row=0, column=5)

        # Right Label Frame (Records)
        right_frame = LabelFrame(main_frame, text="Student Records", font=("Helvetica", 12, "bold"), bg="white", fg="black", bd=2, relief=RIDGE)
        right_frame.place(x=755, y=10, width=735, height=490)

        img_right = Image.open(r"c:\Users\Pridhi\OneDrive\Pictures\memories\New Folder\ssss.webp")
        img_right = img_right.resize((710, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(right_frame, image=self.photoimg_right, bd=2, relief=RIDGE).place(x=5, y=5, width=710, height=130)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Helvetica", 11, "bold"))
        search_frame.place(x=5, y=135, width=710, height=100)
        Label(search_frame, text="Search By:", font=("Helvetica", 10, "bold"), bg="blue", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.search_var = StringVar()
        self.search_combo = ttk.Combobox(search_frame, textvariable=self.search_var, font=("Helvetica", 10, "bold"), width=12, state="readonly")
        self.search_combo["values"] = ("Select", "Roll No", "Student ID", "Phone No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        self.search_txt_var = StringVar()
        Entry(search_frame, textvariable=self.search_txt_var, font=("Helvetica", 10, "bold"), width=15, bd=2, relief=RIDGE).grid(row=0, column=2, padx=10, pady=5, sticky=W)
        #Search Button (Added command=self.search_data)
        Button(search_frame, text="Search", command=self.search_data, font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=10).grid(row=0, column=3, padx=4)
        #Show All Button (Added command=self.fetch_data)
        Button(search_frame, text="Show All", command=self.fetch_data, font=("Helvetica", 10, "bold"), bg="#3017bd", fg="white", width=10).grid(row=0, column=4, padx=4)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=265)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "roll", "gender", "email", "phone", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, show="headings") 
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

       # Define Headings (What the user sees at the top)
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("photo", text="Photo Status")

        # Define Column Widths & Alignment 
        self.student_table.column("dep", width=100, anchor=CENTER)
        self.student_table.column("course", width=100, anchor=CENTER)
        self.student_table.column("year", width=80, anchor=CENTER)
        self.student_table.column("sem", width=100, anchor=CENTER)
        self.student_table.column("id", width=100, anchor=CENTER)
        self.student_table.column("name", width=120, anchor=CENTER)
        self.student_table.column("roll", width=80, anchor=CENTER) 
        self.student_table.column("gender", width=80, anchor=CENTER)
        self.student_table.column("email", width=150, anchor=CENTER)
        self.student_table.column("phone", width=120, anchor=CENTER)
        self.student_table.column("photo", width=100, anchor=CENTER)

       
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

      # ================= Function Declaration =================

    def fetch_data(self):
        """Fetches data from MySQL and displays it in the table"""
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()    
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Fetch failed: {str(es)}", parent=self.root)

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
                my_cursor = conn.cursor()
                
                # Column order matches your Workbench: department, course, year, semester, student_id, name, roll_no, gender, email, phone_no, photo
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_email.get(),  # Matches 'email' column
                    self.var_phone.get(),  # Matches 'phone_no' column
                    self.var_radio1.get()
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        """Fills the input boxes when a row is clicked"""
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus) 
        data = content["values"]
        
        self.var_dep.set(data[0])    
        self.var_course.set(data[1])  
        self.var_year.set(data[2])  
        self.var_semester.set(data[3]) 
        self.var_std_id.set(data[4])  
        self.var_std_name.set(data[5]) 
        self.var_roll.set(data[6])  
        self.var_gender.set(data[7])  
        # Mapping Email and Phone correctly from the table
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_radio1.set(data[10])

    def update_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to update!", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update student details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
                    my_cursor = conn.cursor()
                    
                    # 1. Corrected multi-line SQL Query (matches your Workbench column names)
                    query = """update student set 
                                department=%s, 
                                course=%s, 
                                year=%s, 
                                semester=%s, 
                                name=%s, 
                                roll_no=%s, 
                                gender=%s, 
                                email=%s, 
                                phone_no=%s 
                                where student_id=%s"""

                    # 2. Values tuple must match the order of %s in the query above
                    values = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_std_id.get() # <--- This was missing in your screenshot
                    )

                    my_cursor.execute(query, values)
                    conn.commit()
                    self.fetch_data() # Refreshes the table automatically
                    conn.close()
                    messagebox.showinfo("Success", "Student details updated successfully!", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Update failed: {str(es)}", parent=self.root)
    # ================= Reset Function =================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    # ================= Delete Function =================

    def delete_data(self):
        """Removes the selected student record from MySQL"""
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required to delete!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student record?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
                    my_cursor = conn.cursor()
                    
                    # Using the correct primary key column name 'student_id'
                    sql = "DELETE FROM student WHERE student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    
                    conn.commit()
                    self.fetch_data()   # Refreshes the table
                    self.reset_data()   # Clears the form
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully deleted student record", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Delete failed: {str(es)}", parent=self.root)


    # ================= Search Function =================
    def search_data(self):
        if self.search_var.get() == "Select" or self.search_txt_var.get() == "":
            messagebox.showerror("Error", "Please select an option and enter search text", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
                my_cursor = conn.cursor()
                
                # Mapping UI Search Combo names to DB Column names
                search_column = ""
                if self.search_var.get() == "Roll No":
                    search_column = "roll_no"
                elif self.search_var.get() == "Student ID":
                    search_column = "student_id"
                elif self.search_var.get() == "Phone No":
                    search_column = "phone_no"

                query = "SELECT * FROM student WHERE " + search_column + " LIKE '%" + str(self.search_txt_var.get()) + "%'"
                my_cursor.execute(query)
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showinfo("No Results", "No matching student found", parent=self.root)
                
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Search failed: {str(es)}", parent=self.root)

    # ======================== Generate Dataset Function ========================
    def generate_dataset(self):
        if self.var_dep.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="predhi@12345", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where Student_id=%s", (self.var_std_id.get(),))
                my_cursor.fetchone()
                conn.close()

                # Load the face detection XML file
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)     #scaling factor
                    for (x, y, w, h) in faces:
                        # Return the cropped face
                        return img[y:y+h, x:x+w]
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0
                
                while True:
                    ret, my_frame = cap.read()
                    cropped = face_cropped(my_frame)
                    
                    if cropped is not None:
                        img_id += 1
                        face = cv2.resize(cropped, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        
                        if not os.path.exists("data"):
                            os.makedirs("data")
                            
                        file_name_path = f"data/user.{self.var_std_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    # Stop if 'Enter' (13) is pressed or 100 images are taken
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed successfully!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

   

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()  
    
    
   
