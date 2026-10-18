from cashflow_model.day_count import get_year_fraction

def simple_interest(principal, annual_rate, year_fraction):
    itrst=principal*annual_rate*year_fraction
    return itrst


def compound_interest(principal, annual_rate, year_fraction, frequency):
    itrst=principal*(1+annual_rate/frequency)**(frequency*year_fraction)-principal
    return itrst


def find_last_coupon_date(bond, settlement_date):
    date=bond.get_payment_dates()
    last=bond.issue_date
    for d in date:

        if d<=settlement_date:
            last=d
        else:
            break
    return last
          

def find_next_coupon_date(bond, settlement_date):
    dates = bond.get_payment_dates()
    for d in dates:
        if d > settlement_date:
            return d
    return None

def accrued_interest(bond, settlement_date, convention="30/360"):
    last_coupon = find_last_coupon_date(bond, settlement_date)
    yrfrac = get_year_fraction(last_coupon, settlement_date, convention)
    return yrfrac * bond.face_value * bond.coupon_rate


def clean_price(dirty_price, accrued):
    return dirty_price-accrued