import Database


def main():
    db = Database.Database("database.txt")
    print(f"Loaded {len(db.all_sections())} section(s)")
    print(f"Loaded {len(db.all_courses())} course(s)")
    print("Database Loaded Sucessfully!")
    
if __name__ == "__main__":
    main()