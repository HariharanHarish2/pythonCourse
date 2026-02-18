salary =int(input("Enter the salary:"))
Age = int(input("Enter the Age:"))
if(salary>=20000 or Age<=25):
    loan_amount=int(input("Loan:"))
if(loan_amount<=50000):
    print("its  eligible")
if(loan_amount>50000):
    print("Maximum loan amount is 50000")
else:
    print("loan not appicable")