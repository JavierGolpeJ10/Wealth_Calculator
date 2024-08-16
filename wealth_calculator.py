import sys


def calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years):
    total_savings = current_wealth
    for year in range(1, years + 1):
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)

        print(f"Year {year}: Total savings: ${total_savings:,.2f}")
    return 0


def calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth):
    total_savings = current_wealth
    years_to_freedom = 0
    while True:
        years_to_freedom += 1
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)
        if total_savings > target_wealth:
            print(f"You will reach financial freedom in {years_to_freedom} years!")
            return 0


def calculate_future_income():
    money_right_now = float(input("How much money do you have now? : "))
    checks = float(input("how much do you earn every month? : "))
    months_passed = int(input("how many months ahead do you want to see? : "))

    future_income = checks * months_passed
    total_income = money_right_now + future_income
    print(f"You will have ${total_income} income in {months_passed} months.")


def calculate_financing_purchase():
    purchase_amount = float(input("What is the cost of purchase? : "))
    checks_per_month = float(input("How much money do you earn per month? : "))
    payments = float(input("How much do you want to pay each month? : "))

    high_payment = checks_per_month * 0.5
    user_percentage = (payments/checks_per_month) * 100
    minimum_payment = checks_per_month * 0.2

    def calculate_months(payment, amount):
        return (amount // payment) + (1 if amount % payment > 0 else 0)

    months_high = calculate_months(high_payment, purchase_amount)
    months_standard = calculate_months(payments, purchase_amount)
    months_minimum = calculate_months(minimum_payment, purchase_amount)

    print(f"It will take you {months_high} months or {months_high/12:.2f} years to pay off debt with payments of "
          f"${high_payment:,.2f}, 50% of your monthly income.")
    print(f"It will take you {months_standard} months or {months_standard/12:.2f} years to pay off debt with payments "
          f"of ${payments:,.2f}, {user_percentage:.0f}% of your monthly income.")
    print(f"It will take you {months_minimum} months or {months_minimum/12:.2f} years to pay off debt with payments of "
          f"${minimum_payment:,.2f}, 20% of your monthly income.")


def main():
    program = input("Which program do you want to run? (returns/freedom/future/finance): ")
    if program == "future":
        calculate_future_income()
        return 0
    if program == "finance":
        calculate_financing_purchase()
        return 0
    try:
        current_wealth = float(input("What is the current wealth: "))
        rate_of_return = float(input("What is the rate of return (%): "))
        monthly_savings = float(input("What is the monthly savings: "))
    except ValueError:
        print("That's not a number!")
        sys.exit()
    if program == "returns":
        years = int(input("How many years do you want? "))
        calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years)
    else:
        try:
            target_wealth = float(input("What is the amount you need to be financially free? : "))
        except ValueError:
            print("That's not a number!")
            sys.exit()
        calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth)


if __name__ == "__main__":
    main()
