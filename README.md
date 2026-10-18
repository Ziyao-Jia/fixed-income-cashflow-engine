# Fixed-Income Cashflow Engine
This repo is a fixed-income-cashflow I have built from scratch. It builds future interest and principal cashflows from the terms of a bond or an amortizing loan, then calculates net present value, yield to maturity, and duration(Macauley and modified). It also runs scalable interest-rate shock scenarios and plots how price changes with yield. All of the calculations and modellings utilise no existing libraries. 

<img width="601" height="302" alt="image" src="https://github.com/user-attachments/assets/b54a5b80-c24b-4bc1-94b3-97836c38c645" /> <img width="407" height="593" alt="image" src="https://github.com/user-attachments/assets/e11e36e0-8aae-40fa-92ed-9424a7f0609f" />


## Functions and utilities

- [ ] Bond and Loan instrument definitions
- [ ] Four day-count conventions (ACT/360, ACT/365, 30/360, ACT/ACT)
- [ ] Cashflow projection (coupons + principal / loan amortization)
- [ ] Accrued interest and clean price
- [ ] NPV, YTM (bisection), Macaulay / modified duration
- [ ] Scenario analysis and duration-based PnL approximation
- [ ] Price-yield curve

## Get Started

### Enviroment requirements

- Python 3.10+
- matplotlib（newest version)

### Install&run

```bash
# Clone this repo
git clone https://github.com/Ziyao-Jia/fixed-income-cashflow-engine.git
cd fixed-income-cashflow-engine

# Optional (creating virtual enviroment)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Have fun!
python main.py
