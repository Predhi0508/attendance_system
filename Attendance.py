from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

# Global variable to store attendance data
mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Title
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=700)

        # Left Label Frame (Data Entry)
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=660)

        # Fields (ID, Roll, Name, Dept, Time, Date, Status)
        # ID
        attendanceId_label = Label(Left_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceId_entry = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name
        nameLabel = Label(Left_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        nameLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        nameEntry = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        nameEntry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Roll
        rollLabel = Label(Left_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white")
        rollLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        rollEntry = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold"))
        rollEntry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        depLabel = Label(Left_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        depLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        depEntry = ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        depEntry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Buttons Frame
        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        submit_btn = Button(btn_frame, text="Submit", command=self.fetchData, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        submit_btn.grid(row=0, column=4)

        # Right Label Frame (Table Display)
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Table", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=660)

        # Table Section
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=600)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

    # ========================== Functions ==========================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data has been exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
    
if __name__ == "__main__":
      root = Tk()
      obj = Attendance(root)
      root.mainloop()
    