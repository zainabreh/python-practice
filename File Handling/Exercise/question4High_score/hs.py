import re
def main():
    
    file = open("Exercise\question4High_score\hs.txt",'r')
    x = 0 #total
    max = 0 #maximum
    
    for n in file:
        print(n)
        match = re.search(r"(\d+\d+)",n)
        
        if match:
            no = match.group(1)
            score = int(no)
            
            if score > max:
                max = score
            
            x += score
        else:
            print("Number Not Found")
    file.close()
    
    print("Maximum Number is: ",max)
    print("Total of the Numbers is: ",x)
    
main()