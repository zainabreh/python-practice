def main():
    actual_value_property = float(input("Enter the actual value of the property"))
    
    assesment_value = assesment(actual_value_property)
    print("Your Assesment value for your property: ",assesment_value)
    property_tax = tax(assesment_value)
    print("Your Tax for your property: ",format(property_tax,'.2f'),sep='')
    
def assesment(val):
    return val * 0.6
def tax(val):
    return val * 72

main()