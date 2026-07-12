import json

employee = {
  "name" : "James",
  "Age" : 25,
  "City" : "New York"
 }

file_path = "C:/Users/Lenovo/OneDrive/Desktop/test.json"

try:
    with open(file_path,"x") as file:
        json.dump(employee,file,indent=4)
        print(f"json File {file_path} was created")
except FileExistsError:
    print("That file already exists!")