def main():    
    time_cal()

def time_cal():
    for c in range(10):
        t = int(input("Enter the time of falling object"))
        d = 1/2 * (9.8) * (t * t)
        print("Distance for ", t , " is ", d)
        
main()
        