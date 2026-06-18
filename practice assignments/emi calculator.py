def calculate_emi(principal, annual_rate, years):
    rate = annual_rate / (12 * 100)
    months = years * 12

    emi = (principal * rate * (1 + rate) ** months) / \
          ((1 + rate) ** months - 1)

    return emi

loan = float(input("Enter Loan Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Tenure (Years): "))

emi = calculate_emi(loan, rate, years)

print("Monthly EMI =", round(emi, 2))
