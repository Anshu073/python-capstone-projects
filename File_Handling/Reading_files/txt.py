file_path = "C:/Users/Lenovo/OneDrive/Desktop/test.txt"

try:
    with open(file_path,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File {file_path} was not found")
except PermissionError:
    print(f"You do not have permission to read {file_path} file!")
except Exception:
    print("Something went wrong!")
