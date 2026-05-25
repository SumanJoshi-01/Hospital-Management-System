"""Graphical interface for the Hospital Management System using Tkinter.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class LoginWindow:
    """Login window for the Hospital Management System"""
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System - Login")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.authenticated = False
        self.admin = None
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')
        
        # Login Frame
        login_frame = ttk.Frame(root, padding="20")
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        ttk.Label(login_frame, text="Hospital Management System", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(login_frame, text="Username:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.username_entry = ttk.Entry(login_frame, width=25)
        self.username_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(login_frame, text="Password:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_entry = ttk.Entry(login_frame, width=25   )
        self.password_entry.grid(row=2, column=1, pady=5)
        
        login_button = ttk.Button(login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.username_entry.bind('<Return>', lambda e: self.login())
        self.password_entry.bind('<Return>', lambda e: self.login())
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        admin = Admin('admin', '123', '')
        if admin.login(username, password):
            self.authenticated = True
            self.admin = admin
            self.root.destroy()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")
            self.password_entry.delete(0, tk.END)


class HospitalManagementSystem:
    def __init__(self, root, admin):
        self.root = root
        self.admin = admin
        self.root.title("Hospital Management System")
        self.root.geometry("1000x700")
        
        self.doctors = admin.load_doctors()
        if not self.doctors:
            self.doctors = [
                Doctor('John', 'Smith', 'Internal Med.'),
                Doctor('Jone', 'Smith', 'Pediatrics'),
                Doctor('Jone', 'Carlos', 'Cardiology')
            ]
        
        self.patients = admin.load_patients()
        if not self.patients:
            self.patients = [
                Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['fever']),
                Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['cough']),
                Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['headache'])
            ]
        
        self.discharged_patients = admin.load_discharged_patients()
        self.grouped_patients = []
        
        self.create_widgets()
        
    def create_widgets(self):
        nav_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="#2c3e50")
        nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        title_label = tk.Label(nav_frame, text="HMS Menu", font=("Arial", 12, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(fill=tk.X, padx=5, pady=10)
        
        buttons = [
            ("Doctor Management", self.doctor_management),
            ("Patient Management", self.patient_management),
            ("View Doctors", self.view_doctors_list),
            ("Assign Doctor", self.assign_doctor),
            ("Discharge Patient", self.discharge_patient),
            ("View Discharged", self.view_discharged_patients),
            ("Reallocate Doctor", self.reallocate_patient),
            ("Update Admin", self.update_admin_details),
            ("Management Report", self.management_report),
            ("Show Graphs", self.show_graphs),
            ("Save Data", self.save_data),
            ("Quit", self.quit_application),
        ]
        
        for text, command in buttons:
            btn = tk.Button(nav_frame, text=text, command=command, width=18, bg="#34495e", fg="white", 
                           activebackground="#16a085", relief=tk.RAISED, cursor="hand2")
            btn.pack(fill=tk.X, padx=5, pady=2)
        
        self.main_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Welcome to Hospital Management System")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def doctor_management(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Doctor Management", font=("Arial", 14, "bold")).pack(pady=10)
        
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Register Doctor", command=self.register_doctor, width=20, bg="#3498db", fg="white").pack(pady=5)
        tk.Button(btn_frame, text="Update Doctor", command=self.update_doctor, width=20, bg="#3498db", fg="white").pack(pady=5)
        tk.Button(btn_frame, text="Delete Doctor", command=self.delete_doctor, width=20, bg="#3498db", fg="white").pack(pady=5)
    
    def register_doctor(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Register Doctor", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame = tk.Frame(self.main_frame)
        frame.pack(padx=20, pady=10)
        
        tk.Label(frame, text="First Name:").pack(anchor=tk.W, pady=5)
        first_name_entry = tk.Entry(frame, width=30)
        first_name_entry.pack(anchor=tk.W, pady=2)
        
        tk.Label(frame, text="Surname:").pack(anchor=tk.W, pady=5)
        surname_entry = tk.Entry(frame, width=30)
        surname_entry.pack(anchor=tk.W, pady=2)
        
        tk.Label(frame, text="Speciality:").pack(anchor=tk.W, pady=5)
        speciality_entry = tk.Entry(frame, width=30)
        speciality_entry.pack(anchor=tk.W, pady=2)
        
        def add_doctor():
            first_name = first_name_entry.get().strip()
            surname = surname_entry.get().strip()
            speciality = speciality_entry.get().strip()
            
            if not first_name or not surname or not speciality:
                messagebox.showerror("Error", "All fields are required")
                return
            
            for doc in self.doctors:
                if doc.get_first_name() == first_name and doc.get_surname() == surname:
                    messagebox.showerror("Error", "Doctor already exists")
                    return
            
            self.doctors.append(Doctor(first_name, surname, speciality))
            messagebox.showinfo("Success", "Doctor registered successfully")
            self.doctor_management()
        
        tk.Button(frame, text="Register", command=add_doctor, bg="#27ae60", fg="white", width=20).pack(pady=20)

    def view_doctors_list(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="View Doctors", font=("Arial", 12, "bold")).pack(pady=10)
        
        columns = ("ID", "First Name", "Surname", "Speciality", "Patients")
        tree = ttk.Treeview(self.main_frame, columns=columns, height=15, show='headings')
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        for idx, doctor in enumerate(self.doctors, 1):
            tree.insert("", "end", values=(idx, doctor.get_first_name(), doctor.get_surname(), 
                                          doctor.get_speciality(), len(doctor.patients())))
        
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Note: GUI implementation continues; only core portions are placed here for brevity.
