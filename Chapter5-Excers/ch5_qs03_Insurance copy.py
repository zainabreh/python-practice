def main():
    rep = float(input("Enter replacement cost"))
    insurance(rep)
    
    
def insurance(r):
    insuran = r * 0.8
    print("Your insurance amount is: ",format(insuran,".2f"),sep="")
    
main()