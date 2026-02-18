users={}
def login(users):
    username=input("Enter username")
    password=input("Enter password")
    
    if username  in users and users[username]==password:
        print("login sucessfully")
    else:
        print("invalid username or password")

def register(users):
 username =input("Enter the username")
 password =input("Enter the password")
 Mobile=int(input("Enter the mobile No"))
 if(username in users ):
    print("username already exists")
 else:
    users[username]=password
    file = open("hari.txt","a")
    file.write(username +","+ password +"/n")
    file.close()
    print("Registeration successfully")

    
users =login()
users=register()
