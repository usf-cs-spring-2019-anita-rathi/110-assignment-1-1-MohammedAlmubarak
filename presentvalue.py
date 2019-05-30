F=float(input("enter future value: "))
r=float(input("enter annual interest rate: "))
r=r/100
n=int(input("enter number of years: "))

P=F/(1+r)**n

print("what you need to deposit today: ", P)