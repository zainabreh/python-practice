def main():
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: "))
    
    res = max(n1,n2)
    
    print("Maximum number is: ",res)
    
def max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
main()