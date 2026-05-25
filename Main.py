"""Application entry point for the Hospital Management System.
Provides the main loop for command-line interaction and ties together Admin, Doctor, and Patient modules.
"""

# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():

    admin = Admin('admin','123','B1 1AB') 
     
    doctors = admin.load_doctors()
    if not doctors:
        doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    
    patients = admin.load_patients()
    if not patients:
        patients = [Patient('Sara','Smith', 20, '07012345678','B1 234', ['fever']), Patient('Mike','Jones', 37,'07555551234','L2 2AB', ['cough']), Patient('Daivd','Smith', 15, '07123456789','C1 ABC', ['headache'])]
    
    discharged_patients = admin.load_discharged_patients()
    grouped_patients = []
    
    while True:
        if admin.login():
            running = True 
            break
        else:
            print('Incorrect username or password.')

    while running:
        
        menu = """
            Choose the operation:
            1- Register/View/Update/Delete doctor
            2- Register/View patients/View grouped patients
            3- Assign doctor to a patient
            4- Discharge patients
            5- View discharged patient
            6- Update admin detais
            7- Save patients data to a file
            8- Reallocate doctor to a patient
            9- Set appointment with a doctor
            10- Management Report
            11- Graph
            12- Quit
        """
        print(menu)

        op = input('Option: ')

        if op == '1':
            # -------- Register/view/update/delete doctor ---------
         #ToDo1
            admin.doctor_management(doctors)
            admin.save_doctors(doctors)  
          
          
        elif op == '2':
            # -------- Register/view/update/delete patients ---------
            admin.patient_management(patients,grouped_patients)
            admin.update_patient_in_file(patients, discharged_patients)  
            

        elif op == '3':
            # ------- Assign doctor to a patient -----------
            admin.assign_doctor_to_patient(patients, doctors)
            admin.update_patient_in_file(patients, discharged_patients)  
           

        elif op == '4':
            # --- discharge patients --------
            #ToDo2
            admin.view(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    patient_index = int(input('Enter the patient ID to discharge: ')) - 1
                    
                    discharged_patients.append(patients.pop(patient_index))
                    
                    admin.update_patient_in_file(patients, discharged_patients)  
                    break

                elif op == 'no' or op == 'n':
                    break

               
                else:
                    print('Please answer by yes or no. ')
        
        elif op == '5':
            # ---- view discharged patients --------
            #ToDo4
            admin.view(discharged_patients)

        elif op == '6':
            # -------- Update admin detais ------------
            admin.update_details()
       
        elif op == '7':
            # ------ Save in a file ----------
            admin.save_doctors(doctors)
            admin.save_patients(patients, discharged_patients)

        elif op == '8':
            # ----- reallocate doctor to a patient --------
            admin.reallocate(patients,doctors)
            admin.update_patient_in_file(patients, discharged_patients)  
            
        elif op == '9':
            # ----- Set appointment with a doctor --------
            admin.set_appointment_management(patients, doctors)
            
        elif op == '10':
            # ------------ management report of everything -----------
            admin.management_report(doctors,patients)    
            
        elif op == '11':
            # ----------- Shows the graph --------
            admin.show_graphs_terminal(doctors,patients)
            
    
        elif op == '12':
            # --------- Quit ----------
            #ToDo5
            print('Exiting the program. Goodbye!')
            break

        else:
            
            print('Invalid option. Try again')


if __name__ == '__main__':
    main()
