

from cashflow_model.present_value import calculate_npv


class Scenario:
    

    def __init__(self, name, rate_shift, description=""):
        self.name=name
        self.rate_shift=rate_shift
        self.description=description


#Six Standard Shocks
STANDARD_SCENARIOS = [
    Scenario("Rates +0.5%", 0.005),
    Scenario("Rates +1%", 0.01),
    Scenario("Rates +2%", 0.02),
    Scenario("Rates -0.5%", -0.005),
    Scenario("Rates -1%", -0.01),
    Scenario("Rates -2%", -0.02),
]



def run_scenario(cashflows, base_rate, scenario, as_of_date, convention="ACT/365"):
    rate=base_rate+scenario.rate_shift
    return calculate_npv(cashflows,rate,as_of_date,convention)

def run_all_scenarios(cashflows, base_rate, scenarios, as_of_date, convention="ACT/365"):
    base_npv=calculate_npv(cashflows,base_rate,as_of_date,convention)
    result=[]
    for cnario in scenarios:
        npv=run_scenario(cashflows, base_rate,cnario, as_of_date, convention)
        result.append({
            'name':cnario.name,
            'npv':npv,
            'dollar_change':npv-base_npv,
            'pct_change':(npv-base_npv)/base_npv*100,
        })
    return result


def estimate_pnl_from_duration(modified_duration, rate_change, portfolio_value):
    return -modified_duration * rate_change * portfolio_value
    
