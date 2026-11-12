listofnames = ["Zeziel", "Aurelia", "Vicinia", "Palindrome", "Hillybilly", "Bartholemew","Daviscous", "Edith", "Morticine", "Carol"]

for amountofpasses in range(len(listofnames)):
    for currentposition in range(len(listofnames) - 1 - amountofpasses):
    # - 1 as python starts from 0, so i need len to be 7 for this rather than my 8 names. else if i reach len[8] then it will be like 'hmm where index 9'
    # - amount of passes because each completed pass places the largest remaining name into its final position at the end of the list, therefore no need to check again
    # i and j confuse me, yuck
        
        if listofnames[currentposition] > listofnames[currentposition + 1]: # if my current name position is bigger than the one next to it...swappyyy
            listofnames[currentposition], listofnames[currentposition + 1] = listofnames[currentposition + 1], listofnames[currentposition] 
            # i dont need a temp variable!!!!!!!!! fuck yeah

    print("pass", amountofpasses + 1, ":", ", ".join(listofnames)) # show each pass

print("final:", ", ".join(listofnames)) # prettyyy <3 end result!