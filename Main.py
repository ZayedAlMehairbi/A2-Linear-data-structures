import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Patient:
    def __init__(self, patientId, name, medicalCondition):
        self.patientId = patientId
        self.name = name
        self.medicalCondition = medicalCondition

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, prescription):
        self.stack.append(prescription)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

class Hospital:
    def __init__(self):
        self.patientRecords = {}
        self.consultationQueue = Queue()
        self.prescriptionStack = Stack()
        self.appointments = {}
        self.notes = {}

    def addPatientRecord(self, patient):
        self.patientRecords[patient.patientId] = patient

    def updatePatientRecord(self, patientId, newCondition):
        if patientId in self.patientRecords:
            self.patientRecords[patientId].medicalCondition = newCondition

    def removePatient(self, patientID):
        for patient in self.consultationQueue.queue:
            if patient.patientId == patientID:
                self.consultationQueue.queue.remove(patient)
                return True
        return False

    def scheduleAppointment(self, patientId, doctor, datetime):
        self.appointments[patientId] = (doctor, datetime)

    def prescribeMedication(self, patientId, prescription, amount, date):
        self.prescriptionStack.push((patientId, prescription, amount, date))

    def writeNotes(self, patientId, note):
        if patientId in self.notes:
            self.notes[patientId].append(note)
        else:
            self.notes[patientId] = [note]

class LoginUI:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.bg_color = "#D3D3D3"
        self.text_color = "#000000"
        self.button_color = "#D3D3D3"

        self.usernameLabel = tk.Label(master, text="Username:", bg=self.bg_color, fg=self.text_color)
        self.usernameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.usernameEntry = tk.Entry(master)
        self.usernameEntry.grid(row=0, column=1, padx=5, pady=5)

        self.passwordLabel = tk.Label(master, text="Password:", bg=self.bg_color, fg=self.text_color)
        self.passwordLabel.grid(row=1, column=0, padx=5, pady=5)
        self.passwordEntry = tk.Entry(master, show="*")
        self.passwordEntry.grid(row=1, column=1, padx=5, pady=5)

        self.loginButton = tk.Button(master, text="Login", command=self.login, bg=self.button_color, fg=self.text_color)
        self.loginButton.grid(row=2, columnspan=2, padx=5, pady=5)

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if username == "admin" and password == "123":
            self.master.destroy()
            root = tk.Tk()
            app = HospitalUI(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

class HospitalUI:
    def __init__(self, master):
        self.master = master
        master.title("Hospital Management System")

        self.bg_color = "#D3D3D3"
        self.text_color = "#000000"
        self.button_color = "#D3D3D3"

        self.hospital = Hospital()

        self.main_frame = tk.Frame(master, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.patient_frame = tk.LabelFrame(self.main_frame, text="Patient Information", bg=self.bg_color)
        self.patient_frame.pack(padx=20, pady=10, fill=tk.BOTH)

        self.patientIdLabel = tk.Label(self.patient_frame, text="Patient ID:", bg=self.bg_color, fg=self.text_color)
        self.patientIdLabel.grid(row=0, column=0, padx=5, pady=5)
        self.patientIdEntry = tk.Entry(self.patient_frame)
        self.patientIdEntry.grid(row=0, column=1, padx=5, pady=5)

        self.patientNameLabel = tk.Label(self.patient_frame, text="Patient Name:", bg=self.bg_color, fg=self.text_color)
        self.patientNameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.patientNameEntry = tk.Entry(self.patient_frame)
        self.patientNameEntry.grid(row=1, column=1, padx=5, pady=5)

        self.conditionLabel = tk.Label(self.patient_frame, text="Medical Condition:", bg=self.bg_color, fg=self.text_color)
        self.conditionLabel.grid(row=2, column=0, padx=5, pady=5)
        self.conditionEntry = tk.Entry(self.patient_frame)
        self.conditionEntry.grid(row=2, column=1, padx=5, pady=5)

        self.addButton = tk.Button(self.patient_frame, text="Add Patient", command=self.addPatient, bg=self.button_color, fg=self.text_color)
        self.addButton.grid(row=3, columnspan=2, padx=5, pady=5)


        self.queue_frame = tk.LabelFrame(self.main_frame, text="Consultation Queue", bg=self.bg_color)
        self.queue_frame.pack(padx=20, pady=10, fill=tk.BOTH)

        self.queueListbox = tk.Listbox(self.queue_frame, width=50, height=15)
        self.queueListbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        self.queueScrollbar = tk.Scrollbar(self.queue_frame, orient=tk.VERTICAL, command=self.queueListbox.yview)
        self.queueScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.queueListbox.config(yscrollcommand=self.queueScrollbar.set)

        self.updateButton = tk.Button(self.patient_frame, text="Update Patient", command=self.updatePatientRecord, bg=self.button_color, fg=self.text_color)
        self.updateButton.grid(row=4, columnspan=2, padx=5, pady=5)

        self.removeButton = tk.Button(self.patient_frame, text="Remove Patient", command=self.removePatient, bg=self.button_color, fg=self.text_color)
        self.removeButton.grid(row=5, columnspan=2, padx=5, pady=5)

        self.prescription_frame = tk.LabelFrame(self.main_frame, text="Prescription", bg=self.bg_color)
        self.prescription_frame.pack(padx=20, pady=10, fill=tk.BOTH)

        self.prescriptionLabel = tk.Label(self.prescription_frame, text="Prescription:", bg=self.bg_color, fg=self.text_color)
        self.prescriptionLabel.grid(row=0, column=0, padx=5, pady=5)
        self.prescriptionEntry = tk.Entry(self.prescription_frame, width=40)
        self.prescriptionEntry.grid(row=0, column=1, padx=5, pady=5)

        self.amountLabel = tk.Label(self.prescription_frame, text="Amount (g):", bg=self.bg_color, fg=self.text_color)
        self.amountLabel.grid(row=1, column=0, padx=5, pady=5)
        self.amountVar = tk.StringVar()
        self.amountCombo = ttk.Combobox(self.prescription_frame, textvariable=self.amountVar)
        self.amountCombo['values'] = [str(i) for i in range(10, 501)]
        self.amountCombo.current(0)
        self.amountCombo.grid(row=1, column=1, padx=5, pady=5)

        self.prescribeButton = tk.Button(self.prescription_frame, text="Prescribe", command=self.prescribeMedication, bg=self.button_color, fg=self.text_color)
        self.prescribeButton.grid(row=2, columnspan=2, padx=5, pady=5)

        self.appointment_frame = tk.LabelFrame(self.main_frame, text="Doctor Appointment", bg=self.bg_color)
        self.appointment_frame.pack(padx=20, pady=10, fill=tk.BOTH)

        self.appointmentLabel = tk.Label(self.appointment_frame, text="Doctor:", bg=self.bg_color, fg=self.text_color)
        self.appointmentLabel.grid(row=0, column=0, padx=5, pady=5)
        self.doctorEntry = tk.Entry(self.appointment_frame)
        self.doctorEntry.grid(row=0, column=1, padx=5, pady=5)

        self.dateTimeLabel = tk.Label(self.appointment_frame, text="Date and Time:", bg=self.bg_color, fg=self.text_color)
        self.dateTimeLabel.grid(row=1, column=0, padx=5, pady=5)
        self.dateTimeEntry = tk.Entry(self.appointment_frame)
        self.dateTimeEntry.grid(row=1, column=1, padx=5, pady=5)

        self.scheduleButton = tk.Button(self.appointment_frame, text="Schedule", command=self.scheduleAppointment, bg=self.button_color, fg=self.text_color)
        self.scheduleButton.grid(row=2, columnspan=2, padx=5, pady=5)

        self.summary_frame = tk.LabelFrame(self.main_frame, text="Summary", bg=self.bg_color)
        self.summary_frame.pack(padx=20, pady=10, fill=tk.BOTH)

        self.summaryText = tk.Label(self.summary_frame, text="", bg=self.bg_color, fg=self.text_color, justify=tk.LEFT)
        self.summaryText.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        self.logoutButton = tk.Button(master, text="Logout", command=self.logout, bg=self.button_color, fg=self.text_color)
        self.logoutButton.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.updateQueue()

        self.queueListbox.bind("<<ListboxSelect>>", self.showPatientSummary)

    def addPatient(self):
        patientId = self.patientIdEntry.get()
        name = self.patientNameEntry.get()
        condition = self.conditionEntry.get()

        if patientId and name and condition:
            patient = Patient(patientId, name, condition)
            self.hospital.addPatientRecord(patient)
            self.hospital.consultationQueue.enqueue(patient)
            self.updateQueue()
            self.updateNoteSummary()
            messagebox.showinfo("Success", "Patient added successfully.")
            self.patientIdEntry.delete(0, tk.END)
            self.patientNameEntry.delete(0, tk.END)
            self.conditionEntry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def updatePatientRecord(self):
        patient_id = self.patientIdEntry.get()
        new_condition = self.conditionEntry.get()
        if patient_id and new_condition:
            if self.hospital.updatePatientRecord(patient_id, new_condition):
                messagebox.showinfo("Success","Patient record updated successfully.")
                self.updateNoteSummary()
            else:
                messagebox.showerror("Error","Patient not found.")
        else:
            messagebox.showerror("Error","Please fill in all fields.")

    def removePatient(self):
        patient_id = self.patientIdEntry.get()
        if patient_id:
            if self.hospital.removePatient(patient_id):
                messagebox.showinfo("Success","Patient was removed from"
                                              "queue successfully.")
                self.updateQueue()
                self.updateNoteSummary()
            else:
                messagebox.showerror("Error","Patient not found.")
        else:
            messagebox.showerror("Error","Please enter the patient ID:")


    def prescribeMedication(self):
        patient_index = self.queueListbox.curselection()
        if patient_index:
            selected_patient = self.queueListbox.get(patient_index)
            patientId = selected_patient.split()[0]
            prescription = self.prescriptionEntry.get()
            amount = int(self.amountVar.get())
            date = datetime.now().strftime("%Y-%m-%d")

            if patientId and prescription:
                self.hospital.prescribeMedication(patientId, prescription, amount, date)
                messagebox.showinfo("Success", "Prescription issued successfully.")
                self.prescriptionEntry.delete(0, tk.END)
                self.updateNoteSummary()
            else:
                messagebox.showerror("Error", "Please enter prescription details.")
        else:
            messagebox.showerror("Error", "Please select a patient from the queue.")

    def scheduleAppointment(self):
        patient_index = self.queueListbox.curselection()
        if patient_index:
            selected_patient = self.queueListbox.get(patient_index)
            patientId = selected_patient.split()[0]
            doctor = self.doctorEntry.get()
            datetime_str = self.dateTimeEntry.get()

            if patientId and doctor and datetime_str:
                self.hospital.scheduleAppointment(patientId, doctor, datetime_str)
                messagebox.showinfo("Success", "Appointment scheduled successfully.")
                self.doctorEntry.delete(0, tk.END)
                self.dateTimeEntry.delete(0, tk.END)
                self.updateNoteSummary()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Please select a patient from the queue.")

    def updateQueue(self):
        self.queueListbox.delete(0, tk.END)
        for patient in self.hospital.consultationQueue.queue:
            self.queueListbox.insert(tk.END, f"{patient.patientId} - {patient.name} - {patient.medicalCondition}")

    def updateNoteSummary(self):
        self.summaryText.config(text="")
        summary = ""
        for patient in self.hospital.consultationQueue.queue:
            patient_id = patient.patientId
            if patient_id in self.hospital.notes:
                notes = "\n".join(self.hospital.notes[patient_id])
                summary += f"Patient ID: {patient_id}\n{notes}\n\n"
            else:
                summary += f"Patient ID: {patient_id}\nNo notes\n\n"

            prescription = None
            for item in self.hospital.prescriptionStack.stack:
                if item[0] == patient_id:
                    prescription = item
                    break

            if prescription:
                summary += f"Patient ID: {patient_id}\nPatient Name: {patient.name}\nMedical Condition: {patient.medicalCondition}\nPrescription: {prescription[1]} - Amount: {prescription[2]}g - Date: {prescription[3]}\n\n"

            if patient_id in self.hospital.appointments:
                doctor, datetime_str = self.hospital.appointments[patient_id]
                summary += f"Doctor Appointment: {doctor} - {datetime_str}\n\n"

        self.summaryText.config(text=summary)

    def showPatientSummary(self, event):
        selected_index = self.queueListbox.curselection()
        if selected_index:
            selected_patient = self.queueListbox.get(selected_index)
            patientId = selected_patient.split()[0]
            patient = self.hospital.patientRecords.get(patientId)
            if patient:
                summary = f"Patient ID: {patient.patientId}\n" \
                          f"Patient Name: {patient.name}\n" \
                          f"Medical Condition: {patient.medicalCondition}\n\n"

                if patientId in self.hospital.notes:
                    notes = "\n".join(self.hospital.notes[patientId])
                    summary += f"Notes:\n{notes}\n\n"

                prescription = None
                for item in self.hospital.prescriptionStack.stack:
                    if item[0] == patientId:
                        prescription = item
                        break

                if prescription:
                    summary += f"Prescription:\nPrescribed Medication: {prescription[1]}\nAmount: {prescription[2]}g\nDate: {prescription[3]}\n\n"

                if patientId in self.hospital.appointments:
                    doctor, datetime_str = self.hospital.appointments[patientId]
                    summary += f"Doctor Appointment:\nDoctor: {doctor}\nDate and Time: {datetime_str}\n"

                self.summaryText.config(text=summary)
            else:
                self.summaryText.config(text="Selected patient not found.")
        else:
            self.summaryText.config(text="No patient selected.")

    def logout(self):
        self.master.destroy()
        root = tk.Tk()
        app = LoginUI(root)
        root.mainloop()

root = tk.Tk()
app = LoginUI(root)
root.mainloop()
