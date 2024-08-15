import sys


def calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years):
    total_savings = current_wealth
    for year in range(1, years + 1):
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)

        print(f"Year {year}: Total savings: ${total_savings:,.2f}")
    return 0


def main():
    program = input("Which program do you want to run? (returns or freedom): ")
    try:
        current_wealth = float(input("What is the current wealth: "))
        rate_of_return = float(input("What is the rate of return (%): "))
        monthly_savings = float(input("What is the monthly savings: "))
        years = int(input("How many years do you want? "))
    except ValueError:
        print("That's not a number!")
        sys.exit()
    if program == "returns":
        print("\n")
        calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years)
    else:
        print("That's not a valid program!")


if __name__ == "__main__":
    main()