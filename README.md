# Fixed-Income Cashflow Engine
This repo is a fixed-income-cashflow I have built from scratch. It builds future interest and principal cashflows from the terms of a bond or an amortizing loan, then calculates net present value, yield to maturity, and duration(Macauley and modified). It also runs scalable interest-rate shock scenarios and plots how price changes with yield. All of the calculations and modellings utilise no existing libraries. 



<img width="478" height="530" alt="image" src="https://github.com/user-attachments/assets/d21b9af7-e3de-48bd-a5ad-af54f218765c" />  
<img width="816" height="408" alt="image" src="https://github.com/user-attachments/assets/435219af-17ac-4138-a21a-b889a5f430e1" />


## Functions and utilities

- [x] Bond and Loan instrument definitions
- [x] Four day-count conventions (ACT/360, ACT/365, 30/360, ACT/ACT)
- [x] Cashflow projection (coupons + principal / loan amortization)
- [x] Accrued interest and clean price
- [x] NPV, YTM (bisection), Macaulay / modified duration
- [x] Scenario analysis and duration-based PnL approximation
- [x] Price-yield curve

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
