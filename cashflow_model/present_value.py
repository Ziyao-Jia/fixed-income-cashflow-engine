

from cashflow_model.day_count import get_year_fraction
from cashflow_model.cashflow_engine import project_bond_cashflows


def discount(amount, rate, years):
    PV=amount/(1+rate)**years
    return PV

def calculate_npv(cashflows, discount_rate, as_of_date, convention="ACT/365"):
    total=0.0
    for v in cashflows:
        if v.date<=as_of_date:
            continue
        yfraction=get_year_fraction(as_of_date,v.date,convention)
        total+=discount(v.amount,discount_rate,yfraction)
    return total 

def calculate_ytm(bond, market_price, as_of_date, convention="ACT/365"):
   low,high=0.0001,0.30
   cashflow=project_bond_cashflows(bond)
   for i in range(100):
       mid=(low+high)/2
       npv=calculate_npv(cashflow,mid,as_of_date,convention)
       if abs(npv-market_price)<0.01:
          return mid
       elif npv>market_price:
          low=mid
       else:
          high=mid
   return mid

def calculate_duration(cashflows, ytm, as_of_date, convention="ACT/365"):
    
    weightedtime=0.0
    for pp in cashflows:
        if pp.date<=as_of_date:
            continue
        yearfrac=get_year_fraction(as_of_date,pp.date,convention)
        weightedtime+=discount(pp.amount,ytm,yearfrac)*yearfrac
    tpv=calculate_npv(cashflows,ytm,as_of_date,convention)
    return weightedtime/tpv

    

def calculate_modified_duration(macaulay_duration, ytm, frequency):
    return macaulay_duration/(1+ytm/frequency)


def price_curve(cashflows, rates, as_of_date, convention="ACT/365"):
    return [calculate_npv(cashflows, r, as_of_date, convention) for r in rates]
