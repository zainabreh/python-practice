import re
def main():
    videos = int(input("Enter the Number of short videos of a project"))
    
    video_file = open("File Handling/Task 01/video.txt",'w')
    
    for c in range(1,videos + 1):
        time = float(input("Enter the Time(sec) for short #" + str(c) + " video: " + '\n'))
        
        video_file.write("Time for #" + str(c) + " short video is: " + str(time) + "\n")
        
    video_file.close()
    
    
    video_file_read = open("File Handling/Task 01/video.txt",'r')
    x = 0
    for n in video_file_read:
        match = re.search(r"(\d+\.\d+)",n)
        
        if match:
            strin = match.group(1)
            amount = float(strin)
            x += amount
            print(n)
            
        else:
            print("Could not find time value in file")
        
    video_file_read.close()
    
    print("Total time of the whole project is: " + str(x))
    
    
main()        