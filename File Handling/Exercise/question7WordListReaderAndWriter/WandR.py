def main():
    wordsInput = input("Enter the Numbers of Words you want to enter: ")
    wordsInput = int(wordsInput)
    with open("Exercise\question7WordListReaderAndWriter\WandR.txt",'a') as file:
        for n in range(wordsInput):
            word = input("Start Typing:\n ")
            file.write(word + " ") 
            if n == wordsInput - 1:
                print("You've Reached your limite")
            
            
    LongestWord = ''
    size_of_Word = 0
    with open("Exercise\question7WordListReaderAndWriter\WandR.txt",'r') as file:
        line = file.read()
        arr = line.split()
        size = len(arr)
        for n in arr:
            size_of_Word += len(n)
            avg = len(n) / size_of_Word
            print("The Average Size of ", n, " is : ", format(avg,'.1f'))
            if len(n) > len(LongestWord):
                LongestWord = n
        print("Number of words: ",size)            
        print("Longest word in the file: ",LongestWord)            
                   
if __name__ == "__main__":
    main()
                 