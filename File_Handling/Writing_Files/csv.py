import csv

employees = [["name","age","job"],
             ["Alex",25,"Cook"],
             ["James",26,"Scientist"]]

file_path = "C:/Users/Lenovo/OneDrive/Desktop/test.csv"

with open(file_path,"w",newline="") as file:
    wr = csv.writer(file)
    for row in employees:
        wr.writerow(row)
    print(f"csv file {file_path} was created")
