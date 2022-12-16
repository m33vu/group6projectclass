# Student Name: Gordon Lam
# Student ID: 000892800
# Assignment: 4 - Classes (Individual)
# Section responsible in the group project: facility class


class facility:
    #Constructor
    def __init__(self,FacilityName):
        self.FacilityName = FacilityName

    #Method
    def addFacility(self):
        pass

    def displayFacilities(self):
        FacilitiesFile=open("facilities.txt","r")
        fList = FacilitiesFile.read()
        print(fList)
        FacilitiesFile.close()
    
    def writeListOffacilitiesToFile(self):
        New_facility=facility(input("Enter new facility: "))
        appendFile=open('facilities.txt','a')
        appendFile.write("\n")
        appendFile.write(str(New_facility.FacilityName))
        appendFile.close()


######## Lines below are used to test the methods
option = int(input("\nFacilities Menu:\n 1 - Display Facilities list\n 2 - Add Facility\n 3 - Back to the Main Menu\n"))
while option !=0:
    if option == 1:
        facility.displayFacilities(facility.displayFacilities)
        option = int(input("Facilities Menu:\n 1 - Display Facilities list\n 2 - Add Facility\n 3 - Back to the Main Menu\n"))
    elif option == 2:
        facility.writeListOffacilitiesToFile(facility.writeListOffacilitiesToFile)
        option = int(input("Facilities Menu:\n 1 - Display Facilities list\n 2 - Add Facility\n 3 - Back to the Main Menu\n"))
    elif option == 0:
        break
