# Function to load users from file into dictionary
def load_users():
    users = {}   # Data structure (dictionary)

    try:
        file = open("users.txt", "r")
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password
        file.close()
    except FileNotFoundError:
        pass

    return users


# Function to register new user
def register(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("Username already exists")
    else:
        users[username] = password

        file = open("users.txt", "a")
        file.write(username + "," + password + "\n")
        file.close()

        print("Registration successful")


# Function to login user
def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("Invalid username or password")


# Main Program (Loop + if else)
users = load_users()

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register(users)
    elif choice == "2":
        login(users)
    elif choice == "3":
        print("Program ended")
        break
    else:
        print("Invalid choice")
