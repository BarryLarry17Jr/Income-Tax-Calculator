#!/usr/bin/env python

pay = int(input("Hourly wage?"))
hours_worked = int(input("Hours worked per day?"))
days_worked = int(input("Days worked per week?"))

daily_income = int(pay) * int(hours_worked)
weekly_income = pay * int(hours_worked) * int(days_worked)
yearly_income = weekly_income * 52


print("___________________________________________________________________________")
print
print("Daily Income:$" + str(daily_income))
print("Weekly Income:$" + str(weekly_income))
print("Yearly Income:$" + str(yearly_income))


if 0 <= int(yearly_income) <= 18200:
    print("You're poor lol.")
    print("You don't have an income tax cause you earn less than $182,01.")

if 18201 <= int(yearly_income) <= 37000:
    a = (19/100) * int(yearly_income - 18200)
    print("Your income tax threshold is $18,201 to $37,000.")
    print("You are taxed at a rate of 19c for each $1 over $18,200.")
    print("Your income tax is $" + str(int(a)) + ".")


if 37001 <= int(yearly_income) <= 90000:
    b = (32.5 / 100) * int(yearly_income - 37000) + 3572
    print("Your income tax threshold is $37,001 to $90,000.")
    print("You are taxed at a rate of 32.5c for each $1 over $37,000 plus $3,572.")
    print("Your income tax is $" + str(int(b)) + ".")


if 90001 <= int(yearly_income) <= 180000:
    c = (37 / 100) * int(yearly_income - 90000) + 20797
    print("Your income tax threshold is $90,001 to $180,000.")
    print("You are taxed at a rate of 37c for each $1 over $90,000 plus $20,797.")
    print("Your income tax is $" + str(int(c)) + ".")


if 180001 <= int(yearly_income) <= 100000000:
    d = (45/100) * int(yearly_income - 180000) + 54097
    print("Your income tax threshold is $180,001 and over.")
    print("You are taxed at a rate of 45c for every $1 over $180,000 plus $54,097.")
    print("Your income tax is $" + str(int(d)) + ".")

if 1 <= int(yearly_income) <= 100000000:
    print("___________________________________________________________________________")


if 100000001 <= int(yearly_income):
    print("Your a greedy mother fucker. Piss off i'm not telling u shit.")
    print("___________________________________________________________________________")
