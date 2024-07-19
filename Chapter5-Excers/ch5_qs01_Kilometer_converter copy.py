def main():
    converter()

def converter():
    inp = float(input("Enter Distance in Kilometer"))

    Miles = inp * 0.6214

    print("Conversion of Kilometer into Miles\n Kilometer \t to \t Miles \n",inp,"\t\t",format(Miles,'.1f'))

main()

