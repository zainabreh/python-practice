import circle
import Rectangle


def main():
    QUITE = "q"

    while True:
        print("\n\t\tMENU\n\n")

        print("\t1) Area of a circle\n")
        print("\t2) Circumferance of a circle\n")
        print("\t3) Area of Rectangle\n")
        print("\t4) Perimeter of Rectangle\n")
        print("\t5) Press q for Quite\n\n")

        choice = input("Enter Your Choice").lower()

        if choice == QUITE:
            print("Quitting Program")
            break
        try:
            choice = int(choice)
            
            if choice in range(1,5):

                if choice == 1:
                    print("\tArea of Circle\n")
                    radius = float(input("Enter Radius of a Circle"))
                    print("Area of a Circle is", circle.circle_Area(radius))
                elif choice == 2:
                    print("\tCircumferance of a circle\n")
                    radius = float(input("Enter Circumferance of a Circle"))
                    print("Area of a Circle is", circle.circle_Circum(radius))
                elif choice == 3:
                    print("\tArea of Rectangle\n")
                    width = float(input("Enter width of Rectangle"))
                    height = float(input("Enter height of Rectangle"))
                    print("Area of a Circle is", Rectangle.rect_Area(width, height))
                elif choice == 4:
                    print("\tPerimeter of Rectangle\n")
                    width = float(input("Enter width of Rectangle"))
                    height = float(input("Enter height of Rectangle"))
                    print("Area of a Circle is", Rectangle.rect_perim(width, height))
            else:
                print("Error: Invalid selection. Please choose between 1 and 4.")
                    
        except ValueError:
            print("Error: Invalid input. Please enter a number (1-4) or 'q' to quit.")
   
main()