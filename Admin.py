"""Admin module

Administrative operations and utilities for the Hospital Management System.
Provides login, doctor/patient management, appointment handling, and reporting.
"""

from Doctor import Doctor
from Patient import Patient

class Admin:
    """A class that deals with the Admin operations"""
    
    
    def __init__(self, username, password, address = ''):

        self.__username = username
        self.__password = password
        self.__address =  address
        
        
    def view(self,a_list):

        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')
                     

    def login(self, username=None, password=None) :
 
        if username is None or password is None:
            print("-----Login-----")
            username = input('Enter the username: ')
            password = input('Enter the password: ')
            
        if username == self.__username and password == self.__password:
            return True
        else:
            return False

    def get_username(self):      
        return self.__username
    
    def get_password(self):      
        return self.__password
    
    def get_address(self):       
        return self.__address
    
    def set_username(self, new_username):      
        self.__username = new_username
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def set_address(self, new_address):
        self.__address = new_address

    def find_index(self,index,doctors):
               
        if index in range(0,len(doctors)): 
            return True

        else:
            return False
            

    def update_details(self):

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            username = input('Enter the new username: ')
            self.__username = username
            print(f'Username updated to {self.__username}.')

        elif op == 2:
            password = input('Enter the new password: ')

            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            address = input('Enter the new address: ')
            self.__address = address
            print(f'Address updated to {self.__address}.')

        else:
            #ToDo16
            print('Invalid operation choosen.')
            
            

    def management_report(self, doctors, patients):
        """
        This function is used to generate a report of the system's management
        
        """
        print('Management Report')
        print('==================================================')
        print(f'Number of doctors: {len(doctors)}')
        print('--------------------------------------------------')
        for doctor in doctors:
            print(f'Doctor: {doctor.full_name()}')
            print(f'Speciality: {doctor.get_speciality()}')
            print(f'Number of Patients: {len(doctor.patients())}')
            print('--------------------------------------------------')
        print('==================================================')
        print('Appointment Report')
        print('==================================================')
        for doctor in doctors:
            print(f'Doctor: {doctor.full_name()}')
            appointments_by_month = self.appointments_per_month(doctor)
            for month, appointments in appointments_by_month.items():
                if appointments:
                    print(f'{month}:')
                    for count, patient in enumerate(appointments, start=1):
                        print(f'  {count}. {patient}')
            print('--------------------------------------------------')
        print('==================================================')
        print('Patient Report')
        print('==================================================')
        illness_count = self.count_patients_by_illness(patients)
        for illness, count in illness_count.items():
            print(f'Illness: {illness}, Number of Patients: {count}')
        print('==================================================')


    def set_appointment(self, doctor, patient, month):
        """
        Set an appointment for a patient with a doctor in a specific month.
        
        """
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        if 1 <= month <= 12:
            month_name = months[month - 1]
            appointment = f"{patient.full_name()} - {month_name}"
            doctor.add_appointment(appointment)
            print(f"Appointment set for {patient.full_name()} with Dr. {doctor.full_name()} in {month_name}")
        else:
            print("Invalid month. Please enter a number between 1 and 12.")

    def set_appointment_management(self, patients, doctors):
        """
        Allow the admin to set an appointment for a patient with any doctor
        
        """
        print("-----Set Appointment-----")

        print("-----Select Patient-----")
        print('ID |          Full Name           |      Doctor\'s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) - 1

            if patient_index not in range(len(patients)):
                print('The ID entered was not found.')
                return

        except ValueError:
            print('The ID entered is incorrect')
            return

        patient = patients[patient_index]

        print("\n-----Select Doctor-----")
        print('ID |          Full Name           |  Speciality')
        self.view(doctors)

        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) - 1

            if doctor_index not in range(len(doctors)):
                print('The doctor ID entered was not found.')
                return

        except ValueError:
            print('The doctor ID entered is incorrect')
            return

        doctor = doctors[doctor_index]

        print(f"\nSetting appointment for {patient.full_name()} with Dr. {doctor.full_name()}")
        print(f"Speciality: {doctor.get_speciality()}")

        print("\nAvailable months:")
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        for idx, month in enumerate(months, 1):
            print(f"{idx} - {month}")

        month_input = input("Please enter the month number (1-12): ")

        try:
            month = int(month_input)
            if 1 <= month <= 12:
                self.set_appointment(doctor, patient, month)
            else:
                print("Invalid month number. Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# ---------------------------------------------------------------------------
#    ------------------------ Doctor code ------------------------------
# ---------------------------------------------------------------------------
     
     
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        
        """
        #ToDo2
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')
        return first_name, surname, speciality
    
 
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
       
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('Choose an option: ')

        # ----------register----------
        if op == '1':
            print("-----Register-----")

            print('Enter the doctor\'s details:')
            #ToDo4
            first_name, surname, speciality = self.get_doctor_details()

            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True
                    break 
            #ToDo6
            if name_exists == False:
                doctors.append(Doctor(first_name, surname, speciality))
            print('Doctor registered.')

        # ----------View-------------
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

        # ----------Update--------------
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                except ValueError: 
                    print('The ID entered is incorrect')

            # ------------menu----------
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) 

            #ToDo8
            if op == 1:
                new_first_name = input('Enter the new first name: ')
                doctors[index].set_first_name(new_first_name)
                print('First name updated.')

            elif op == 2:
                new_surname = input('Enter the new surname: ')
                doctors[index].set_surname(new_surname)
                print('Surname updated.')

            elif op == 3:
                new_speciality = input('Enter the new speciality: ')
                doctors[index].set_speciality(new_speciality)
                print('Speciality updated.')

            else:
                print('Invalid operation choosen. Check your spelling!')
               
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            #ToDo9
            doctor_index = int(doctor_index) -1

            if doctor_index in range(len(doctors)):
                
                del doctors[doctor_index]
                print('Doctor deleted.')

            else:
                print('The id entered was not found.')

        else:
            print('Invalid operation choosen. Check your spelling!')
       
       
    def view_docotrs(self,doctors):
       
        print("-----View Doctors-----")
        print('ID |          Full Name           | Speciality   ')
        self.view(doctors)
        
        
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        
        """
        print("-----Assign-----")

*** End Patch