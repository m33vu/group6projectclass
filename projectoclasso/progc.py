#Assignment: Classes
#Marcus Valdez
#Student ID number: 000890235

#Doctor class
class Doctor:
    def __init__(self, id, name, specialization, working_time,  qualification, room_Number):
        self.__id = id
        self.__name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_Number = room_Number

    #Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification

    def get_room_Number(self):
        return self.room_Number
    
    #Setters
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_specialization(self, specialization):
        self.specialization = specialization
    
    def set_working_time(self, working_time):
        self.working_time = working_time

    def set_qualification(self, qualification):
        self.qualification = qualification
    
    def set_room_Number(self, room_Number):
        self.room_Number = room_Number
    
    global doctorlist
    doctorlist = []

    #Methods
    def doctor_menu(self):
        global doctorchoice
        doctorchoice = int(input("Doctors Menu:\n1- Display Doctors List\n2- Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n\t")) 
    
    def FormatDrInfo(self):
        my_file = open("doctors.txt", "r")
        for each_line in my_file:
            print(each_line)

    def enterDrInfo(self):
        doctorid = int(input("Enter the doctor ID: \n\t"))
        doctorname = input("Enter the doctor's name \n\t")
        doctorspecialization = input("Enter the doctor's specialization \n\t")
        doctorworkingtime = input("Enter the doctor's working time \n\t")
        doctorqualification = input("Enter the doctor's qualification \n\t")
        doctorroomnumber = int(input("Enter the doctor's room number \n\t"))
        # if i need later doctorinfo = Doctor(doctorid, doctorname, doctorspecialization, doctorworkingtime, doctorqualification, doctorroomnumber)
        new_doctor = open("doctors.txt", "a")
        new_doctor.write("\n")
        new_doctor.write(str(doctorid))
        new_doctor.write("_")
        new_doctor.write(doctorname)
        new_doctor.write("_")
        new_doctor.write(doctorspecialization)
        new_doctor.write("_")
        new_doctor.write(doctorworkingtime)
        new_doctor.write("_")
        new_doctor.write(doctorqualification)
        new_doctor.write("_")
        new_doctor.write(str(doctorroomnumber))
        new_doctor.close()


    def readDoctorsFile(self):
        my_file = open("doctors.txt", "r")
        for line in my_file:
            line_strip = line.strip()
            line_split = line_strip.split()
            doctorlist.append(line_split)
        my_file.close()

    def searchDoctorById(self):
        my_file = open("doctors.txt", "r")
        global id_search
        id_search = input("Enter the doctor Id:\n\t")
        for line in doctorlist:
            if id_search == "66":
                if line[0].startswith(id_search):
                    print(doctorlist[6])
            elif id_search == "21":
                if line[0].startswith(id_search):
                    print(doctorlist[1])
            elif id_search == "32":
                if line[0].startswith(id_search):
                    print(doctorlist[2])
            elif id_search == "17":
                if line[0].startswith(id_search):
                    print(doctorlist[3])
            elif id_search == "33":
                if line[0].startswith(id_search):
                    print(doctorlist[4])
            elif id_search == "123":
                if line[0].startswith(id_search):
                    print(doctorlist[5])
            else: 
                print("Can't find the doctor with the same ID on the system")
                break

    def searchDoctorByName(self):
        doctornames = [doctor1.get_name(), doctor2.get_name(), doctor3.get_name(), doctor4.get_name(), doctor5.get_name(), doctor6.get_name()]
        name_search = input("Enter the doctor's name:\n\t")
        if name_search in doctornames:
            if name_search == doctor1.get_name():
                print(doctorlist[1])
            elif name_search == doctor2.get_name():
                print(doctorlist[2])
            elif name_search == doctor3.get_name():
                print(doctorlist[3])
            elif name_search == doctor4.get_name():
                print(doctorlist[4])
            elif name_search == doctor5.get_name():
                print(doctorlist[5])
            elif name_search == doctor6.get_name():
                print(doctorlist[6])
        else:
            print("Can't find the doctor with the same name on the system")

    def displayDoctorInfo(self):
        print(doctorlist)

    global delete_line
    def delete_line(filename, line_number):
        with open(filename) as file:
            lines = file.readlines()
        if (line_number <= len(lines)):
            del lines[line_number - 1]
            with open(filename, "w") as file:
                for line in lines:
                    file.write(line)

    def editDoctorInfo(self):
        new_doctor = int(input("Please enter the id of the doctor that you want to edit their information: \n\t"))
        new_name = str(input("Enter new name: \n\t"))
        new_specialization = str(input("Enter the new specialization: \n\t"))
        new_workingtime = str(input("Enter the new working time: \n\t"))
        new_qualification = str(input("Enter the new qualification: \n\t"))
        new_roomnumber = int(input("Enter the new room number: \n\t"))
        edit_doctor = open("doctors.txt", "a")
        edit_doctor.write("\n")
        edit_doctor.write(str(new_doctor))
        edit_doctor.write("_")
        edit_doctor.write(new_name)
        edit_doctor.write("_")
        edit_doctor.write(new_specialization)
        edit_doctor.write("_")
        edit_doctor.write(new_workingtime)
        edit_doctor.write("_")
        edit_doctor.write(new_qualification)
        edit_doctor.write("_")
        edit_doctor.write(str(new_roomnumber))
        edit_doctor.close()
        if new_doctor == 66:
            delete_line("doctors.txt", 7)
        elif new_doctor == 21:
            delete_line("doctors.txt", 2)
        elif new_doctor == 32:
            delete_line("doctors.txt", 3)
        elif new_doctor == 17:
            delete_line("doctors.txt", 4)
        elif new_doctor == 33:
            delete_line("doctors.txt", 5)
        elif new_doctor == 123:
            delete_line("doctors.txt", 6)
        

    def displayDoctorsList(self):
        my_file = open("doctors.txt", "r")
        for each_line in my_file:
            print(each_line)

    def test(self):
        print(doctor0.get_id(),"\t",doctor0.get_name(),"\t","\t",doctor0.get_specialization(),"\t",doctor0.get_working_time(),"\t",doctor0.get_qualification(),"\t", doctor0.get_room_Number())
        print(doctor1.get_id(),"\t", doctor1.get_name(),"\t",doctor1.get_specialization(),"\t","\t",doctor1.get_working_time(),"\t",doctor1.get_qualification(),"\t",doctor1.get_room_Number())
        print(doctor2.get_id(),"\t",doctor2.get_name(),"\t",doctor2.get_specialization(),"\t",doctor2.get_working_time(),"\t",doctor2.get_qualification(),"\t", doctor2.get_room_Number())
        print(doctor3.get_id(),"\t", doctor3.get_name(),"\t",doctor3.get_specialization(),"\t",doctor3.get_working_time(),"\t", doctor3.get_qualification(),"\t","\t", doctor3.get_room_Number())
        print(doctor4.get_id(),"\t",doctor4.get_name(),"\t",doctor4.get_specialization(),"\t","\t",doctor4.get_working_time(),"\t",doctor4.get_qualification(),"\t",doctor4.get_room_Number())
        print(doctor5.get_id(),"\t",doctor5.get_name(),"\t",doctor5.get_specialization(),"\t",doctor5.get_working_time(),"\t",doctor5.get_qualification(),"\t","\t",doctor5.get_room_Number())
        print(doctor6.get_id(),"\t",doctor6.get_name(),"\t",doctor6.get_specialization(),"\t","\t",doctor6.get_working_time(),"\t",doctor6.get_qualification(),"\t","\t",doctor6.get_room_Number())

    def writeListOfDoctorsToFile(self):
        pass

    def addDrToFile(self):
        pass

doctor0 = Doctor("Id", "Name", "Speciality", "Timing", "Qualification", "Room Number")
doctor1 = Doctor(21, "Dr. Cody", "ENT", "5AM-11AM", "MBBS,MD", "17")
doctor2 = Doctor(32, "Dr. Vikram", "Physician", "10PM-3AM", "MBBS,MD", "45")
doctor3 = Doctor(17, "Dr. Amy", "Surgeon", "8PM-2AM", "BDM", "8")
doctor4 = Doctor(17, "Dr.David", "Artho", "10AM-4PM", "MBBS,MS", "40")
doctor5 = Doctor(123, "Dr.Ross", "Headaches", "8PM-10AM", "MST", "102")
doctor6 = Doctor(66, "Dr. Mike", "Heart", "9AM-5PM", "MS", "2")

#Facility class
class Facility:
    def __init__(self, Facility_name):
        self.Facility_name = Facility_name
        
#getters
    def get_Facility_name(self):
        return self.Facility_name

#setters
    def set_Facility_name(self, Facility_name):
        self.Facility_name = Facility_name

    global facilitylist
    facilitylist = []
#Methods


    def facility_menu(self):
        global facility_choice
        facility_choice = int(input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\t"))

    def readFacilityfile(self):
        facilityfile = open("facilities.txt", "r")
        for line in facilityfile:
            line_strip = line.strip()
            line_split = line_strip.split()
            facilitylist.append(line_split)
        facilityfile.close()

    def displayFacilities(self):
        my_file = open("facilities.txt", "r")
        for each_line in my_file:
            print(each_line)

    def addFacility(self):
        facilityname = (input("Enter the name of the facility: \n\t"))
        new_Facility = open("facilities.txt", "a")
        new_Facility.write("\n")
        new_Facility.write(facilityname)
        new_Facility.close()

#Laboratory class
class Laboratory:
    def __init__(self, Lab_name, cost):
        self.Lab_name = Lab_name
        self.cost = cost
        
    global laboratorylist
    laboratorylist = []

#Setters
    def get_Lab_name(self):
        return self.__Lab_name

    def get_cost(self):
        return self.__cost  
    

#Getters
    def set_Lab_name(self, Lab_name):
        self.__Lab_name = Lab_name

    def set_cost(self, cost):
        self.__cost = cost

#Methods
    def laboratories_menu(self):
        global labchoice
        labchoice = int(input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\t"))

    def displayLabsList(self):
        my_file = open("laboratories.txt", "r")
        for each_line in my_file:
            print(each_line)
    
    def readLabsFile(self):
        my_file = open("laboratories.txt", "r")
        for line in my_file:
            line_strip = line.strip()
            line_split = line_strip.split()
            laboratorylist.append(line_split)
        my_file.close()

    def addLaboratory(self):
        labname = input("Enter Laboratory facility:: \n\t")
        labcost = input("Enter Laboratory cost: \n\t")
        new_lab = open("laboratories.txt", "a")
        new_lab.write("\n")
        new_lab.write(labname)
        new_lab.write("_")
        new_lab.write(labcost)
        new_lab.close()

         
laboratory1 = Laboratory("Facility_1", 800)
laboratory2 = Laboratory("Facility_2", 1200)
laboratory3 = Laboratory("Facility_3", 500)
laboratory4 = Laboratory("Facility_4", 50)
    
#Patient class
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

#Getters
    def get_pid(self):
        return self.__pid
    
    def get_name(self):
        return self.__name
    
    def get_disease(self):
        return self.__disease 

    def get_gender(self):
        return self.__gender  

    def get_age(self):
        return self.__age

#Setters
    def set_pid(self, pid):
        self.__pid = pid

    def set_cost(self, name):
        self.__name = name

    def set_Lab_name(self, disease):
        self.__disease = disease

    def set_gender(self, gender):
        self.__gender = gender
    
    def set_age(self, age):
        self.__age = age

    global patientlist
    patientlist = []
#Methods
    def patientmenu(self):
        global patientchoice
        patientchoice = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\t"))

    def readPatientFile(self):
        my_file = open("patients.txt", "r")
        for line in my_file:
            line_strip = line.strip()
            line_split = line_strip.split()
            patientlist.append(line_split)
        my_file.close()

    def displayPatientsList(self):
        my_file = open("patients.txt", "r")
        for each_line in my_file:
            print(each_line)

    def searchPatientById(self):
        my_file = open("patients.txt", "r")
        global p_id_search
        p_id_search = input("Enter the Patient Id:\n\t")
        for line in patientlist:
            if p_id_search == "12":
                if line[0].startswith(p_id_search):
                    print(patientlist[1])
            elif p_id_search == "13":
                if line[0].startswith(p_id_search):
                    print(patientlist[2])
            elif p_id_search == "14":
                if line[0].startswith(p_id_search):
                    print(patientlist[3])
            elif p_id_search == "15":
                if line[0].startswith(p_id_search):
                    print(patientlist[4])
            else: 
                print("Can't find the Patient with the same id on the system")
                break

    def enterPatientInfo(self):
        patientid = int(input("Enter Patient id: \n\t"))
        patientname = input("Enter Patient name \n\t")
        patientdisease = input("Enter Patient disease \n\t")
        patientgender = input("Enter Patient gender: \n\t")
        patientage = int(input("Enter Patient age: \n\t"))
        new_patient = open("patients.txt", "a")
        new_patient.write("\n")
        new_patient.write(str(patientid))
        new_patient.write("_")
        new_patient.write(patientname)
        new_patient.write("_")
        new_patient.write(patientdisease)
        new_patient.write("_")
        new_patient.write(patientgender)
        new_patient.write("_")
        new_patient.write(str(patientage))
        new_patient.close()

    global delete_line2
    def delete_line2(filename, line_number):
        with open(filename) as file:
            lines = file.readlines()
        if (line_number <= len(lines)):
            del lines[line_number - 1]
            with open(filename, "w") as file:
                for line in lines:
                    file.write(line)
    
    def editPatientInfo(self):
        newpatient = int(input("Please enter the id of the Patient that you want to edit their information: \n\t"))
        newname = str(input("Enter new name: \n\t"))
        newdisease = str(input("Enter new disease: \n\t"))
        newgender = str(input("Enter new gender: \n\t"))
        newage = int(input("Enter new age: \n\t"))
        edit_patient = open("patients.txt", "a")
        edit_patient.write("\n")
        edit_patient.write(str(newpatient))
        edit_patient.write("_")
        edit_patient.write(newname)
        edit_patient.write("_")
        edit_patient.write(newdisease)
        edit_patient.write("_")
        edit_patient.write(newgender)
        edit_patient.write("_")
        edit_patient.write(str(newage))
        edit_patient.close()
        if newpatient == 12:
            delete_line2("patients.txt", 2)
        elif newpatient == 13:
            delete_line2("patients.txt", 3)
        elif newpatient == 14:
            delete_line2("patients.txt", 4)
        elif newpatient == 15:
            delete_line2("patients.txt", 5)

patient1 = Patient(12, "Pankaj", "Cancer", "Male", 30)
patient2 = Patient(13, "Sumit", "Cold", "Male", 23)
patient3 = Patient(14, "Alok", "Maleriya", "Male", 45)
patient4 = Patient(15, "Ravi", "Diabetes", "Male", 25)


#Management class
class Management:
    def StartMessage(self):
        print("Welcome to Alberta Hospital (AH) Management system \n")
    def DisplayMenu(self):
        global optionchoice
        optionchoice = int(input("Select from the following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n\t"))

mainmenu = Management()
mainmenu.StartMessage()
while True:
    mainmenu.DisplayMenu()
    if optionchoice == 0:
        break
    elif optionchoice not in range(0,5):
        break
    
    while True:
        if optionchoice == 1:
            doctormenu = Doctor(1,1,1,1,1,1)
            doctormenu.doctor_menu()
            if doctorchoice == 1:
                doctormenu.readDoctorsFile()
                doctormenu.displayDoctorsList()
                print("\n")
                print("Back to previous menu \n")
            elif doctorchoice == 2:
                doctormenu.readDoctorsFile()
                doctormenu.searchDoctorById()
                print("\n")
                print("Back to previous menu \n")
            elif doctorchoice == 3:
                doctormenu.readDoctorsFile()
                doctormenu.searchDoctorByName()
                print("\n")
                print("Back to previous menu \n")
            elif doctorchoice == 4:
                doctormenu.enterDrInfo()
                doctormenu.readDoctorsFile()
                print("\n")
                print("Back to previous menu \n")
            elif doctorchoice == 5:
                doctormenu.editDoctorInfo()
                print("\n")
                print("Back to previous menu \n")
            elif doctorchoice == 6:
                mainmenu.StartMessage()
                mainmenu.DisplayMenu()
            else:
                break
        elif optionchoice == 2:
            facilitymenu = Facility(1)
            facilitymenu.facility_menu()
            if facility_choice == 1:
                facilitymenu.readFacilityfile()
                facilitymenu.displayFacilities()
                print("\n")
                print("Back to previous menu \n")
            elif facility_choice == 2:
                facilitymenu.addFacility()
                print("\n")
                print("Back to previous menu \n")
            elif facility_choice == 3:
                mainmenu.StartMessage()
                mainmenu.DisplayMenu()
            else:
                break
        elif optionchoice == 3:
            laboratorymenu = Laboratory(1,1)
            laboratorymenu.laboratories_menu()
            if labchoice == 1:
                laboratorymenu.readLabsFile()
                laboratorymenu.displayLabsList()
                print("\n")
                print("Back to previous menu \n")
            elif labchoice == 2:
                laboratorymenu.addLaboratory()
                print("\n")
                print("Back to previous menu \n")
            elif labchoice == 3:
                mainmenu.StartMessage()
                mainmenu.DisplayMenu()
            else:
                break
        elif optionchoice == 4:
            patient_menu = Patient(1,1,1,1,1)
            patient_menu.patientmenu()
            if patientchoice == 1:
                patient_menu.readPatientFile()
                patient_menu.displayPatientsList()
                print("\n")
                print("Back to previous menu \n")
            elif patientchoice == 2:
                patient_menu.readPatientFile()
                patient_menu.searchPatientById()
                print("\n")
                print("Back to previous menu \n")
            elif patientchoice == 3:
                patient_menu.readPatientFile()
                patient_menu.enterPatientInfo()
                print("\n")
                print("Back to previous menu \n")
            elif patientchoice == 4:
                patient_menu.editPatientInfo()
                print("\n")
                print("Back to previous menu \n")
            elif patientchoice == 5:
                mainmenu.StartMessage()
                mainmenu.DisplayMenu()