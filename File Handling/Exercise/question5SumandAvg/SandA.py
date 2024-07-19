def main():
    x = 0
    count = 0
    try:
        with open("p2\sales.txt",'r') as file:
            for n in file:
                x += float(n)
                count += 1
            avg = x / count
            print("Total of Numbers is: ",format(x,'.2f'))
            print("Average of Numbers is: ",format(avg,'.2f'))
    except ValueError:
        print("Value Error")
        
    except IOError:
        print("Input Error")
        
    except TypeError:
        print("Some type Error")
if __name__ == '__main__':
    main()