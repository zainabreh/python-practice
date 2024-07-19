def main():
    sqrt_Feet_Wall = float(input("Enter Square Feetof wall spaced to be Painted"))
    price_per_Gallon = float(input("Enter the price of pant per gallon"))
    
    gallon = no_gallon_Req(sqrt_Feet_Wall)
    hour = hrs_lab(sqrt_Feet_Wall)
    cost = cost_paint(gallon,price_per_Gallon)
    charges = lab_charges(hour)
    total = total_cost_paint(cost,charges)
    display(gallon,hour,cost,charges,total)
    
    
def no_gallon_Req(wall):
    return wall / 112

def hrs_lab(wall):
    return (wall / 112) * 8

def cost_paint(gal,priceGal):
    return gal * priceGal

def lab_charges(hrs):
    return hrs * 35

def total_cost_paint(cost,charge):
    return cost + charge

def display(gallon,hour,cost,charges,total):
    print("\tData\n")
    print("The Number Gallon Required are:",gallon,"\n")
    print("The Hour of Laboured Required is:",hour,"\n")
    print("The cost of the paint per Gallon is:",cost,"\n")
    print("The Labour Charges:",charges,"\n")
    print("The Total Payment of the Entire Job is:",total,"\n")
    
main()