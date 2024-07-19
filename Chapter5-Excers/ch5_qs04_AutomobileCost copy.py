def main():
    loanPayment = float(input("Enter your Monthly Loan Payment"))
    insurance = float(input("Enter your Monthly Insurance"))
    maintenance = float(input("Enter your Monthly Maintenance"))
    gas = float(input("Enter your Monthly gas"))
    tire = float(input("Enter your Monthly Tire"))
    oil = float(input("Enter your Monthly Oil"))
    
    mon_res = monthly_cost(loanPayment,insurance,maintenance,gas,tire,oil)
    print("Your Monthly cost is: ",mon_res)
    yearly_cost(mon_res)
    
def monthly_cost(loanPayment,insurance,maintenance,gas,tire,Oil):
    return loanPayment+insurance+maintenance+gas+tire+Oil

def yearly_cost(res):
    result = res * 12
    
    print("Your yearly cost is: ", result)
    
main()