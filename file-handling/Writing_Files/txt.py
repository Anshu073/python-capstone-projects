# Python Writing Files (.txt, .json, .csv)

txt_data = "My name is Anshh."
# employyes = ["James","Alex","rouk"]
file_path = "C:/Users/Lenovo/OneDrive/Desktop/test.txt"

# Creating New_File Using Mode='w'
with open(file_path,"w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created")

# Creating New File Using Mode='x'
# try:
#     with open(file_path,"x") as file:
#         file.write(txt_data)
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print(f"File {file_path} was already exist!")

# Appending New Txt In Existing File
# with open(file_path,"a") as file:
#     file.write("\n" + txt_data)
#     print("Additional text added successfully...")

# Using With List
# with open(file_path,"w") as file:
#     for employee in employyes:
#         file.write(employee + " ")
#     print(f"File {file_path} was created")