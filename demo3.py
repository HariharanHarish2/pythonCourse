


def register():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")

        if username == "":
            print("Invalid Username")
            continue

        if len(password) < 5:
            print("Password must be at least 5 characters")
            continue

        if "@" not in email or "." not in email:
            print("Invalid Email")
            continue

        if not mobile.isdigit() or len(mobile) != 10:
            print("Invalid Mobile Number")
            continue

        with open("user.txt", "a") as file:
            file.write(username + "," + password + "," + email + "," + mobile + "\n")

        print("Registration Successful\n")
        break


def login():
    try:
        with open("user.txt", "r") as file:
            users = file.readlines()
    except FileNotFoundError:
        print("No user found. Please Register First.\n")
        register()
        login()
        return

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    for user in users:
        u, p, e, m = user.strip().split(",")
        if username == u and password == p:
            print("Login Successful\n")
            shopping_cart()
            return

    print("Invalid Login\n")


def shopping_cart():
    prices = []

    while True:
        price = float(input("Enter Product Price: "))
        prices.append(price)

        choice = input("Add More Items? (yes/no): ").lower()
        if choice == "no":
            break

    discount = float(input("Enter Discount Percentage: "))
    final = add(prices, discount)

    print("Final Amount:", final)


def add(prices, discount_percent):
    total = sum(prices)
    discount = total * (discount_percent / 100)
    final_amount = total - discount
    return final_amount


login()
