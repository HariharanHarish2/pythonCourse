def add(prices, discount_percent):
    total = sum(prices)
    discount = total * (discount_percent / 100)
    final_amount = total - discount
    return final_amount


def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")
    mobile = input("Enter Mobile: ")

    if username == "":
        print("Invalid Username")
        return

    if len(password) < 5:
        print("Password must be at least 5 characters")
        return

    if "@" not in email or "." not in email:
        print("Invalid Email")
        return

    if not mobile.isdigit() or len(mobile) != 10:
        print("Invalid Mobile Number")
        return

    with open("user.txt", "a") as file:
        file.write(username + "," + password + "," + email + "," + mobile + "\n")

    print("Registration Successful")


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        with open("user.txt", "r") as file:
            users = file.readlines()
    except FileNotFoundError:
        print("No users registered")
        return

    for user in users:
        u, p, e, m = user.strip().split(",")
        if username == u and password == p:
            print("Login Successful")
            shopping_cart()
            return

    print("Invalid Login")


def shopping_cart():
    prices = []

    while True:
        price = float(input("Enter Product Price: "))
        prices.append(price)

        choice = input("Add More Items? (yes/no): ")
        if choice.lower() == "no":
            break

    discount = float(input("Enter Discount Percentage: "))
    final = add(prices, discount)

    print("Final Amount:", final)


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")
