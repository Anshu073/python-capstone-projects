import json

file_path = "C:/Users/Lenovo/OneDrive/Desktop/test.json"

try:
    with open(file_path,"r") as file:
        content = json.load(file)
        for key,value in content.items():
            print(f"{key} : {value}")
except FileNotFoundError:
    print(f"File {file_path} was not found")
except PermissionError:
    print(f"You doo not have permission to read {file_path} file!")
except Exception:
    print("Something went wrong!")