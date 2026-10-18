from datetime import date
from cashflow_model.instruments import Bond
from cashflow_model.cashflow_engine import (
    project_bond_cashflows, project_amortizing_loan, total_interest
)
from cashflow_model.present_value import (
    calculate_npv, calculate_ytm, calculate_duration, calculate_modified_duration, price_curve
)
from cashflow_model.scenario import STANDARD_SCENARIOS, run_all_scenarios

def main():
    as_of = date(2024, 1, 1)
    bond = Bond("US Treasury 5Y", 1000.0, 0.05, 2, as_of, date(2029, 1, 1))
    cfs = project_bond_cashflows(bond)
    base_rate = 0.04

    npv = calculate_npv(cfs, base_rate, as_of)
    ytm = calculate_ytm(bond, npv, as_of)
    dur = calculate_duration(cfs, ytm, as_of)
    mod_dur = calculate_modified_duration(dur, ytm, 1)

    print("=" * 50)
    print(f"{bond.name}")
    print(f"NPV:           ${npv:,.2f}")
    print(f"YTM:           {ytm:.2%}")
    print(f"Duration:      {dur:.2f} years")
    print(f"Mod Duration:  {mod_dur:.2f}")
    print("=" * 50)

    print("\nCashflow Schedule:")
    print(f"{'Date':<12} {'Amount':>10} {'Type'}")
    for cf in cfs:
        print(f"{cf.date}  {cf.amount:>10.2f}  {cf.cashflow_type}")

    print("\nScenario Analysis:")
    results = run_all_scenarios(cfs, base_rate, STANDARD_SCENARIOS, as_of)
    print(f"{'Scenario':<15} {'NPV':>12} {'$ Change':>10} {'% Change':>10}")
    for r in results:
        print(f"{r['name']:<15} ${r['npv']:>10,.2f} {r['dollar_change']:>+10.2f} {r['pct_change']:>+9.2f}%")

    print("\n" + "=" * 50)
    print("Loan Amortization (first 6 months)")
    loan_cfs = project_amortizing_loan(10_000.0, 0.05, 188.71, 60)
    print(f"{'Month':<8} {'Interest':>10} {'Principal':>10}")
    for i in range(6):
        interest = loan_cfs[i*2].amount
        principal = loan_cfs[i*2+1].amount
        print(f"{i+1:<8} {interest:>10.2f} {principal:>10.2f}")
    print(f"Total interest: ${total_interest(loan_cfs):,.2f}")

    # Optional: price-yield curve with matplotlib
    try:
        import matplotlib.pyplot as plt
        rates = [r / 1000 for r in range(5, 121, 5)]
        prices = price_curve(cfs, rates, as_of)
        plt.figure(figsize=(8, 4))
        plt.plot([r * 100 for r in rates], prices)
        plt.xlabel("Yield (%)")
        plt.ylabel("Price")
        plt.title(f"Price vs Yield — {bond.name}")
        plt.grid(True)
        plt.show()
    except ImportError:
        print("\n(matplotlib not installed, skipping chart)")

if __name__ == "__main__":
    main()