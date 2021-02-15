from sys import argv

script, amount = argv

cash = amount.split('.')

try:
    money = int(cash[1])
    bills = int(cash[0])
except:
    print("Please enter a number in the format of '0.00' with no negative numbers")
    exit()
else:
    if money < 0 or bills < 0 or len(cash[1]) > 2:
        print("Please enter a number in the format of '0.00' with no negative numbers")
        exit()

def billsfunc(money):
    one = 0
    five = 0
    ten = 0
    twenty = 0
    fifty = 0
    hundred = 0

    while money >= 100:
        if money - 100 >= 0:
            money -= 100
            hundred += 1
    while money >= 50:
        if money - 50 >= 0:
            money -= 50
            fifty += 1
    while money >= 20:
        if money - 20 >= 0:
            money -= 20
            twenty += 1
    while money >= 10:
        if money - 10 >= 0:
            money -= 10
            ten += 1
    while money >= 5:
        if money - 5 >= 0:
            money -= 5
            five += 1
    while money >= 1:
        if money - 1 >= 0:
            money -= 1
            one += 1

    print("You need",end = "")
    if hundred == 1:
        print(f" {hundred} hundred dollar bill",end = ", ")
    elif hundred > 0:
        print(f" {hundred} hundred dollar bills",end = ", ")

    if fifty == 1:
        print(f" {fifty} fifty dollar bill",end = ", ")
    elif fifty > 0:
        print(f" {fifty} fifty dollar bills",end = ", ")
    if twenty == 1:
        print(f" {twenty} twenty dollar bill",end = ", ")
    elif twenty > 0:
        print(f" {twenty} twenty dollar bills",end = ", ")
    if ten == 1:
        print(f" {ten} ten dollar bill",end = ", ")
    elif ten > 0:
        print(f" {ten} ten dollar bills",end = ", ")
    if five == 1:
        print(f" {five} five dollar bill",end = ", ")
    elif five > 0:
        print(f" {five} five dollar bills",end = ", ")
    if one == 1:
        print(f" {one} dollar bill",end = ", ")
    elif one > 0:
        print(f" {one} dollar bills",end = ", ")

def coins(money):
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    while money >= 25:
        if money - 25 >= 0:
            money -= 25
            quarter += 1
    while money >= 10:
        if money - 10 >= 0:
            money -= 10
            dime += 1
    while money >= 5:
        if money - 5 >= 0:
            money -= 5
            nickel += 1
    while money >= 1:
        if money - 1 >= 0:
            money -= 1
            penny += 1

    if quarter == 1:
        print(f" {quarter} quarter",end = ", ")
    else:
        print(f" {quarter} quarters",end = ", ")

    if dime == 1:
        print(f" {dime} dime",end = ", ")
    else:
        print(f" {dime} dimes",end = ", ")

    if nickel == 1:
        print(f" {nickel} nickel",end = ", and")
    else:
        print(f" {nickel} nickels",end = ", and")

    if penny == 1:
        print(f" {penny} penny")
    else:
        print(f" {penny} pennies")

billsfunc(bills)
coins(money)
