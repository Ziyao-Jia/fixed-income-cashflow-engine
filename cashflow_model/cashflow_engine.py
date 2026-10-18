
class Cashflow:
    
    def __init__(self, date, amount, cashflow_type):
       self.date=date
       self.amount=amount
       self.cashflow_type=cashflow_type


def project_bond_cashflows(bond):
    cashflows=[]
    payday=bond.get_payment_dates()
    for d in payday:
        cashflows.append(Cashflow(d,bond.get_coupon_amount(),"COUPON"))
    cashflows.append(Cashflow(bond.maturity_date,bond.face_value,"PRINCIPAL"))
    return cashflows

def project_amortizing_loan(balance, annual_rate, monthly_payment, num_months):
    
    cashflows=[]
    remaining=balance
    principal=int
   
    for d in range(1,num_months+1):
        if remaining<=0:
            break
        interest=remaining*annual_rate/12    
        principal=min(monthly_payment-interest,remaining)
        
        cashflows.append(Cashflow(d,interest,"INTEREST"))
        cashflows.append(Cashflow(d,principal,"PRINCIPAL"))
        remaining-=principal
    return cashflows
def total_cashflows(cashflows):
    ## This is fucking cash baby  ~~~
    return sum(cashbaby.amount for cashbaby in cashflows)
    
    


def total_interest(cashflows):
    return sum(cashbabe.amount for cashbabe in cashflows if cashbabe.cashflow_type=="COUPON" or cashbabe.cashflow_type=="INTEREST")
    
