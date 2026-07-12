import os

path = "2D_collections/Num_pad.py"

if os.path.exists(path):
    print(f"{path} Exists...")

    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a Directory")
else:
    print(f"{path} not Exist!")