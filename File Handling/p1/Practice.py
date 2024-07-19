def main():
    
    # Creating a file
    
    # zainab = open('./File-Handling/zainab.txt','w')
    
    # Writing on the file
    
    # zainab.write("Zainab is a good girl and she is always working hard to make her parents proud and less their burden and she believe that that day is not far when she will share her father burden with herself inshaAllah\n")
    # zainab.write("Rehman is zainab's father, she love her father more than anyone but can't tell to anyone nor she want anyone to know that,she want her  love for her father to be proven by her action not by her words\n")
    # zainab.write("Durrani")

    # closing file
    
    # zainab.close()
    
    
    # Opening file for reading purpose
    
    # zainab = open('./File-Handling/zainab.txt','r')
    
    # Reading whole file
    
    # reading = zainab.read()
    
    # Reading only one line at a time
    
    # reading = zainab.readline()
    
    
    # closing file
    
    # zainab.close()
    
    
    # Dispalying the content of the file in terminal
    # print(reading)
    
    
    
    
    # friend = open("friend.txt",'w')
    
    # f1 = input("Friend 01: ")
    # f2 = input("Friend 02: ")
    # f3 = input("Friend 03: ")
    # f4 = input("Friend 04: ")
    
    
    # friend.write(f1+"\n")
    # friend.write(f2+"\n")
    # friend.write(f3+"\n")
    # friend.write(f4+"\n")

    
    # friend = open("friend.txt",'r')
    
    # lin1 = friend.readline()
    # lin2 = friend.readline()
    # lin3 = friend.readline()
    # lin4 = friend.readline()
    # lin5 = friend.readline()
    # lin6 = friend.readline()
    # lin7 = friend.readline()
    
    # print("....................")
    
    # lin1 = lin1.rstrip("\n")
    # lin2 = lin2.strip("\n")
    # lin3 = lin3.rstrip("\n")
    # lin4 = lin4.rstrip("\n")
    # lin5 = lin1.rstrip("\n")
    # lin6 = lin2.strip("\n")
    # lin7 = lin3.rstrip("\n")
    
    # friend.close()
    
    # print(lin1)
    # print(lin2)
    # print(lin3)
    # print(lin4)
    # print(lin5)
    # print(lin6)
    # print(lin7)
    
    
    
    friend = open("File Handling/p1/friend.txt",'a')
    
    f5 = input("Friend 06: ")
    f6 = input("Friend 07: ")
    f7 = input("Friend 08: ")
    
    
    friend.write(f5+"\n")
    friend.write(f6+"\n")
    friend.write(f7+"\n")
    
    
    
    
    friend = open("File Handling/p1/friend.txt",'r')
    
    read = friend.read()
    
    # lin1 = friend.readline()
    # lin2 = friend.readline()
    # lin3 = friend.readline()
    # lin4 = friend.readline()
    # lin5 = friend.readline()
    # lin6 = friend.readline()
    # lin7 = friend.readline()
    
    # print("....................")
    
    # lin1 = lin1.rstrip("\n")
    # lin2 = lin2.strip("\n")
    # lin3 = lin3.rstrip("\n")
    # lin4 = lin4.rstrip("\n")
    # lin5 = lin5.rstrip("\n")
    # lin6 = lin6.strip("\n")
    # lin7 = lin7.rstrip("\n")
    
    friend.close()
    
    # print(lin1)
    # print(lin2)
    # print(lin3)
    # print(lin4)
    # print(lin5)
    # print(lin6)
    # print(lin7)
    
    print(read)
    
    
    
    
main()