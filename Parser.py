import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import re
import  Database

def parse_file(filename:str, db) -> list:
    """Get a files extension and attempt to parse it into a class list"""
    ext =  filename[filename.rfind(".")+1:] # Get the file extension
    if not os.path.exists(filename):
        print("ERROR: File Doesn't exist!")
        return
    if ext == "txt":
        return parse_txt(filename, db)
    elif ext == "pdf":
        return parse_pdf(filename, db)
    else:
        print(f"'{ext}' isn't a supported file extension")



def parse_txt(filename: str, db) -> list:
    """Parser for text files"""
    course_list = []
    with open(filename,"r") as f:
        for line in f.read().splitlines():
            if not line.startswith("#"):
                course_list.append(line.strip())
        return course_list

def parse_pdf(filename: str, db) -> list:
    """Parser for DegreeWorks PDF Files"""
    pdf = PdfFileReader(filename)
    course_list = []
    prune_list = ["GEOL 1121", "GEOL 2225", "ENVS 1205", "ASTR 1105", "CHEM 1211","CHEM 1212", "ATSC 1112", "CPSC 5115"]
    for page_num in range(pdf.numPages):
        pageObj = pdf.getPage(page_num)
        txt = pageObj.extract_text().splitlines()
        for line_num, line in enumerate(txt):
            if "SCIENCE COURSES WITH LAB Still Needed" in line:
                count = int(re.findall("[0-9]+", line)[0]) #Get the number of labs that are required
                for i in range(count):
                     course_list.append("SCIE-LABB")
            #elif "Senior Software Engineering Project" in line:
            #    course_list.append("CPSC 4176")
            elif "Class in" in line:
                course = re.findall("[a-zA-Z]+ [0-9]{4}",line)
                try:
                    course_list.append(course[0])
                except IndexError:
                    pass
            elif "Electives" in line: # Need this for elective processing
                elective = db.get_elective(line.split(" Electives ")[0])
                credits = txt[line_num+1].strip().split(" ")[0]
                course_list.append(f"ELECT,{elective},{credits}")
    for course in prune_list:
        if course in course_list:
            course_list.remove(course)
    return course_list

if __name__ == "__main__":
    db = Database.Database("database.txt")
    print(parse_pdf("Test Files/Input1.pdf",db))
