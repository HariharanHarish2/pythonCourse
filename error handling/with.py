with open("data.txt", "r") as f:
    print(f.read())
    #without close()
with open("data.txt", "a") as f:
    f.write("\nUsing with statement")
