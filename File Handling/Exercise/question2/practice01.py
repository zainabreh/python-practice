def main():
   try:
        inp = input("Enter file name to open: ")
    
        file = "Exercise\\" + inp
        counter = 0
        lines = []
        with open(file,'r') as fil:
            for r in fil:
                lines.append(r)
                counter += 1
                
                print(f"{counter}: {r}",end=' ')
                
            
            if counter < 5:            
                print(''.join(lines[:4]))
            else:
                print(''.join(lines))
    
   except ValueError:
       print("Value Error")   
       
   except Exception as err:
        print("An Error occured",err)
                
            
main()








    # with open(file, 'r') as fil:
    #     lines = fil.readlines()
    #     line_count = len(lines)