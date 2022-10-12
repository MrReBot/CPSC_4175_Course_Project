import Database
import Student
import os
import json

def main():
    db = Database.Database("database.txt")
    st = Student.Student(db)
    print(f"Loaded {len(db.all_sections())} section(s)")
    print(f"Loaded {len(db.all_courses())} course(s)")
    print(f"Loaded {len(db.all_tags())} Tag(s)")
    print("Database Loaded Sucessfully!\nBegining test cases")
    path = "Test Files"
    for file in os.listdir(path):
        print(f"{path}/{file}: ",end="")
        schedule_template = {
        "Fall": 16,
        "Spring": 16,
        "Summer": 3
        }
        try:
            schedule, classlist = st.generate_schedule(f"{path}/{file}", schedule_template)
            print(f"SUCCESS, {len(schedule)} Semester(s), {len(classlist)} Classe(s)")
            print(f"{schedule}\n")
        except:
            print("FAILED")
    print("Tests cases Finsihed")
        
if __name__ == "__main__":
    main()
