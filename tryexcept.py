try:
    print(10/0)

except ZeroDivisionError:
    print("its zerodivision")
else:
    print("invalid number")