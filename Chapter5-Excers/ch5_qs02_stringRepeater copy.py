def main():
    str = input("Enter String")
    num = int(input("Enter Number,you want to repeat the string"))
    res = repeat(str,num)
    print("your Resulted output is:",res,"")
    
def repeat(str,n):
    return str * n

main()
