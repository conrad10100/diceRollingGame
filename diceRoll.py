import random
count = 0
maxmoney = 100
value = 0
count2 = 0
money = 0
money = input("How much money do you have :")
money2 = int(money)
while money2>0:
    rollOne = random.randint(1, 6)
    rollTwo = random.randint(1, 6)
    value = rollOne + rollTwo
    count = count + 1
    if maxmoney < money2:
        maxmoney = money2
        count2 = count-1
    if value ==7:
        money2 = money2 +4
    else:
        money2 = money2-1
    #print (count ,"", money2) #Remove pound in front of print to see how your money changes
print("You have no more money after" , count, "rolls")
print("You should have quit after",count2,"rolls when you had $",maxmoney)
