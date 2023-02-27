import math

# function to calculate monthly loan payments
def calculate_loan_payment(principal, interest_rate, num_months):
    monthly_rate = interest_rate / 1200
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-num_months))
    return round(payment, 2)

# function to calculate investment returns
def calculate_investment_returns(principal, interest_rate, num_months):
    final_amount = principal * (1 + interest_rate / 100) ** (num_months / 12)
    return round(final_amount - principal, 2)

# function to calculate interest rate
def calculate_interest_rate(principal, num_months, monthly_payment):
    monthly_rate = 0.01
    while True:
        if monthly_rate >= 1:
            return None
        balance = principal
        for i in range(num_months):
            interest = balance * monthly_rate
            balance += interest - monthly_payment
            if balance <= 0:
                break
        if balance <= 0:
            break
        monthly_rate += 0.0001
    return round(monthly_rate * 1200, 2)

# function to save results in output file
def save_results(result, output_file):
    with open(output_file, "a") as f:
        f.write(str(result) + "\n")

# get user input
print("Welcome to the Financial Calculator!")
print("What do you want to calculate? (Enter 1, 2 or 3)")
print("1. Monthly loan payments")
print("2. Investment returns")
print("3. Interest rate")
choice = int(input("Enter your choice: "))

if choice == 1:
    principal = float(input("Enter the loan principal amount: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    num_months = int(input("Enter the number of months for the loan: "))
    monthly_payment = calculate_loan_payment(principal, interest_rate, num_months)
    print(f"The monthly payment is ${monthly_payment}")
    save_results(monthly_payment, "output.txt")

elif choice == 2:
    principal = float(input("Enter the investment amount: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    num_months = int(input("Enter the number of months for the investment: "))
    investment_returns = calculate_investment_returns(principal, interest_rate, num_months)
    print(f"The investment returns are ${investment_returns}")
    save_results(investment_returns, "output.txt")

elif choice == 3:
    principal = float(input("Enter the loan principal amount: "))
    num_months = int(input("Enter the number of months for the loan: "))
    monthly_payment = float(input("Enter the monthly payment: "))
    interest_rate = calculate_interest_rate(principal, num_months, monthly_payment)
    if interest_rate is None:
        print("Unable to calculate interest rate")
    else:
        print(f"The interest rate is {interest_rate}%")
        save_results(interest_rate, "output.txt")

else:
    print("Invalid choice. Please try again.")
