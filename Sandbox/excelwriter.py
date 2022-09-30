# import xlsxwriter module
import xlsxwriter as xlsx

# importing date class from datetime module
from datetime import date
import openpyxl as xl
from os.path import exists
import shutil
 
class ExcelWriter:

    def copy_File(self, newfilename, templateFileName):

        shutil.copy(templateFileName, newfilename)

    def savetofile(self, classDictionary, classList, newFileName, templateFileName):
        ew=ExcelWriter()
        todays_date = date.today()
        # Workbook() takes one, non-optional, argument
        # which is the filename that we want to create.
        if(exists(templateFileName) == True):
            filename1 =newFileName
            check = exists(filename1)
            if(check== False):
                ew.copy_File(filename1,templateFileName)
            wb2 = xl.load_workbook(filename1)
            ws2 =wb2.active
    
            startingCellNumber = -6
            nextLine = False
            currentYear = ''
            for semester in classDictionary:
                # Use the worksheet object to write
                # data via the write() method.
                season = semester.split(" ")
                #If the semester is fall for the first time it prints the data on the first free line
                #if it is fall of next year they print this on the next year line
                if(season[0] == "Fall"):
                    semesterCell = ["A","B"]
                    newSemesterCell = [1,2]
                    if(season[1] != currentYear):
                        currentYear = season[1]
    #                    nextLine = False
                        startingCellNumber = startingCellNumber+9
                    ws2[semesterCell[0] + str(startingCellNumber)].value = semester
                    creditCellNumber = startingCellNumber +8
                elif(season[0] == "Spring"):
                    semesterCell = ["C","D"]
                    ws2[semesterCell[0] + str(startingCellNumber)].value = semester
     #               nextLine = True
                    creditCellNumber = startingCellNumber +8
                elif(season[0] == "Summer"):
                    semesterCell =["E","F"]
                    ws2[semesterCell[0] + str(startingCellNumber)].value = semester
     #               nextLine = True
                    creditCellNumber = startingCellNumber +3
                cellNum = startingCellNumber+1
                for number, classnam in enumerate(classDictionary[semester]):
                    partofclass = number%2
                    if(partofclass == 0):
                        ws2[semesterCell[0] + str(cellNum)] = classnam
                    elif(partofclass == 1):
                        ws2[semesterCell[1] + str(cellNum)] = int(classnam)
                        cellNum = cellNum +1
                    
                #if(semester == "Fall" + str(todays_date.year)):
                #    worksheet.write('A1',str(classdictionary[semester]))
               #     classnum=0
               #
            cellNum = 3
            for number, classinfo in enumerate(classList):
                partofclassinfo = number%3
                   
                if(partofclassinfo == 0):
                    ws2['H'+str(cellNum)]= classinfo
                if(partofclassinfo == 1):
                    ws2['I'+str(cellNum)] = int(classinfo)
                if(partofclassinfo==2):
                    ws2['J'+str(cellNum)] = classinfo
                    cellNum = cellNum + 1
                        
                      
                       
            wb2.save(filename1)
            errorcheck = False
        else:
            errorcheck = True
        return errorcheck
    
    

def main():
    ew=ExcelWriter()
    classdict= {'Fall 2022' : ['CPSC1201',"3", 'HIST2112','3'],
                           'Spring 2023' : ['CPSC1203', "3",'CPSC1204','4'],
                           'Summer 2023' : ['MATH1131',"4"],
                           'Fall 2023' : ['A General Elective', '3'],
                           'Fall 2024' : ['CPSC3125','3']
            }
    classlist= ['CPSC1201',"3","",'HIST2112','3',"",'CPSC1203', "3","",'CPSC1204','4',"",'MATH1131',"4","CLASS NUM", 'A General Elective', '3',""]
    errorcheck = ew.savetofile(classdict,classlist,"Path to graduate_Test.xlsx","Path To Graduation.xlsx" )
    if(errorcheck == True):
        print("Error, excel sheet does not exist")
    else:
        print("Excel sheet saved")

if __name__ == "__main__":
    main()

