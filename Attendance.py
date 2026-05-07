from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

# Global variable to store attendance data list
mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        # ================= Variables =================
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

        # Left Label Frame (Information Entry)
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=660)

        # Labels and Entry Fields
        # Attendance ID
        Label(Left_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Name
        Label(Left_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Roll
        Label(Left_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Department
        Label(Left_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold")).grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Time
        Label(Left_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Date
        Label(Left_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(Left_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold")).grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Status
        Label(Left_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.atten_status = ttk.Combobox(Left_frame, width=18, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Buttons Frame
        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=350, width=705, height=35)

        Button(btn_frame, text="Import csv", command=self.importCsv, width=15, font=("times new roman", 11, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export csv", command=self.exportCsv, width=15, font=("times new roman", 11, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Update", command=self.update_data, width=15, font=("times new roman", 11, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 11, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # Right Label Frame (Table View)
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
        self.AttendanceReportTable.heading("attendance", text="Status")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

    # ========================== LOGIC FUNCTIONS ==========================

    def fetchData(self, rows):
        """Refreshes the Treeview table with data from the rows list"""
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        """Loads a CSV file into the table"""
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if fln == "":
            return
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        """Saves current table data to a CSV file (Excel format)"""
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            if fln == "":
                return
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Exported successfully to " + os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        """Fills the form boxes when you click on a row in the table"""
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        if len(rows) == 0:
            return
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def update_data(self):
        """Adds or Updates the manually entered data into the table list"""
        if self.var_atten_id.get() == "" or self.var_atten_name.get() == "":
            messagebox.showerror("Error", "Please fill essential details!", parent=self.root)
        else:
            global mydata
            # Collect current form data
            new_row = [
                self.var_atten_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            ]
            mydata.append(new_row)
            self.fetchData(mydata)
            messagebox.showinfo("Success", "Record added to the local list. Remember to Export to save permanently.", parent=self.root)

    def reset_data(self):
        """Clears all input fields"""
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()