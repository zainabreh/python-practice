def main():
    
    months = ['Jan','Feb','Mar',"Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    amount = []
    total = 0
    
    for i in months:
        rain_amount = input("Enter Rainfall Amount for "+ i + " : ")
        amount.append(rain_amount)
        
    for i in amount:
        total += int(i)
        
    print("Total Rainfall in a year: ", total)
    print("Average Rainfall in a year: ", format(total/len(amount),'.2f'))
    
    max_Number = max(amount)
    max_Rainfall = amount.index(max_Number)
    max_Rainfall_Month = months[max_Rainfall]
    
    print("Maximum Rainfall in Month: ", max_Rainfall_Month)
    
    
    min_Number = min(amount)
    min_Rainfall = amount.index(min_Number)
    min_Rainfall_Month = months[min_Rainfall]
    
    print("Minimum Rainfall in Month: ", min_Rainfall_Month)
    
main()    
    