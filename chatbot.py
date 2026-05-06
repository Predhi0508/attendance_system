from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance System Help Desk")
        self.root.geometry("800x600+350+100")
        self.root.bind('<Return>', self.send_message)

        # Main Frame
        main_frame = Frame(self.root, bd=4, bg="powder blue", relief=RIDGE)
        main_frame.pack(fill=BOTH, expand=True)

        # Title
        lbl_menu = Label(main_frame, text="CHAT ME - HELP DESK", font=("arial", 20, "bold"), bg="white", fg="green")
        lbl_menu.pack(side=TOP, fill=X)

        # Chat Window (Text Area)
        # Added bg="white" and fg="black" to ensure visibility
        self.text_chat = Text(main_frame, font=("arial", 12, "bold"), bd=3, relief=RIDGE, bg="white", fg="black")
        self.text_chat.pack(padx=10, pady=10, fill=BOTH, expand=True) # Set fill and expand to TRUE

        # Scrollbar
        scrollbar = Scrollbar(self.text_chat)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text_chat.config(yscrollcommand=scrollbar.set)

        # Bottom Frame for Input
        input_frame = Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        input_frame.pack(side=BOTTOM, fill=X)

        lbl_type = Label(input_frame, text="Type Something:", font=("arial", 12, "bold"), bg="white", fg="blue")
        lbl_type.grid(row=0, column=0, padx=10, pady=10)

        self.entry_var = StringVar()
        self.entry = ttk.Entry(input_frame, textvariable=self.entry_var, width=45, font=("arial", 13, "bold"))
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        self.entry.focus() # Automatically put cursor in input box

        self.send_btn = Button(input_frame, text="Send >>", command=self.send_message, font=("arial", 12, "bold"), width=10, bg="green", fg="white")
        self.send_btn.grid(row=0, column=2, padx=10, pady=10)

        self.clear_btn = Button(input_frame, text="Clear", command=self.clear_chat, font=("arial", 12, "bold"), width=8, bg="red", fg="white")
        self.clear_btn.grid(row=0, column=3, padx=10, pady=10)

        # Initial Bot Welcome Message
        self.text_chat.insert(END, "Bot: Hello! I am your Attendance Assistant. How can I help you today?\n")

    # ========================== Chat Logic ==========================
    def send_message(self, event=None):
        msg = self.entry_var.get().strip()
        user_input = msg.lower()
        
        if msg == "":
            return

        # Show user message in window
        self.text_chat.insert(END, "\nYou: " + msg + "\n")
        self.entry_var.set("") # Clear input box

        # Bot Responses logic
        if "hi" in user_input or "hello" in user_input:
            self.text_chat.insert(END, "Bot: Hi there! How can I assist you?\n")
        
        elif "how to train" in user_input:
            self.text_chat.insert(END, "Bot: Go to 'Train Data' on the dashboard and click 'TRAIN DATA'.\n")

        elif "face" in user_input or "camera" in user_input:
            self.text_chat.insert(END, "Bot: Use 'Face Detector' to open the camera and mark attendance.\n")

        elif "excel" in user_input or "attendance" in user_input:
            self.text_chat.insert(END, "Bot: Attendance records are saved in 'attendance.csv'.\n")

        elif "developer" in user_input:
            self.text_chat.insert(END, "Bot: This system was developed by Predhi.\n")

        elif "bye" in user_input:
            self.text_chat.insert(END, "Bot: Goodbye! Have a great day!\n")
        
        else:
            self.text_chat.insert(END, "Bot: I'm not sure about that. Try asking about 'Training' or 'Attendance'.\n")
        
        self.text_chat.see(END) # Auto-scroll to the bottom

    def clear_chat(self):
        self.text_chat.delete('1.0', END)
        self.text_chat.insert(END, "Bot: History cleared. How can I help you?\n")

if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()