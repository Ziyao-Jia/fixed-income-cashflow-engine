from datetime import date

def add_months(d: date, months: int) -> date:  ## for some awkward cases(Month-ends and leap years)
    total = d.month - 1 + months
    year = d.year + total // 12
    month = total % 12 + 1
    day = d.day
    while day > 28:
        try:
            return date(year, month, day)
        except ValueError:
            day -= 1
    return date(year, month, day)

class Bond:
    name:str
    face_value:float
    coupon_rate:float
    payment_frequency:int
    issue_date:date
    maturity_date:date


    def __init__(self, name, face_value, coupon_rate, payment_frequency,
                 issue_date, maturity_date):
        self.name=name
        self.face_value=face_value
        self.coupon_rate=coupon_rate
        self.payment_frequency=payment_frequency
        self.issue_date=issue_date
        self.maturity_date=maturity_date


    def get_coupon_amount(self)->float:
      amount:float
      amount=self.face_value*self.coupon_rate/self.payment_frequency
      return amount

    def get_payment_dates(self):
        Dates=[]
        steps=12//self.payment_frequency
        dd=add_months(self.issue_date,steps)
        while dd<=self.maturity_date:
            Dates.append(dd)
            dd=add_months(dd,steps)
        return Dates
    def __str__(self):
        return(f"the bound name is {self.name}")
   


class Loan:
    name:str
    original_balance:float
    annual_rate:float
    monthly_payment:float
    start_date:date
    term_months:int
    def __init__(self,name,original_balance,annual_rate,monthly_payment,start_date,term_months):
        self.name = name
        self.original_balance = original_balance
        self.annual_rate = annual_rate
        self.monthly_payment = monthly_payment
        self.start_date = start_date
        self.term_months = term_months
    