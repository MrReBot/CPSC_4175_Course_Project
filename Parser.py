import os


def parse_file(filename:str) -> list:
    """Get a files extension and attempt to parse it into a class list"""
    ext =  filename[filename.rfind(".")+1:] # Get the file extension
    if not os.path.exists(filename):
        print("ERROR: File Doesn't exist!")
        return
    if ext == "txt":
        return parse_txt(filename)
    else:
        print(f"'{ext}' isn't a supported file extension")
        
        
            
def parse_txt(filename: str) -> list:
    """Parser for text files"""
    course_list = []
    with open(filename,"r") as f:
        for line in f.read().splitlines():
            if not line.startswith("#"):
                course_list.append(line.strip())
        return course_list