import Database
import Student

def main():
    db = Database.Database("database.txt")
    #st = Student.Student(db, )
    print(f"Loaded {len(db.all_sections())} section(s)")
    print(f"Loaded {len(db.all_courses())} course(s)")
    print(f"Loaded {len(db.all_tags())} Tag(s)")
    print("Database Loaded Sucessfully!")
    
if __name__ == "__main__":
    main()