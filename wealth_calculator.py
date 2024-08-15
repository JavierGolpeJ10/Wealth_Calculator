def calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years):
    total_savings = current_wealth
    for year in range(1, years + 1):
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)
        print(f"Year {year}: Total savings: {total_savings:.2f}")
    return 0

