import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
#os.remove("data.txt")
