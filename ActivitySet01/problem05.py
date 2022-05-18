# Functions

def computepay(h, r):
    if h>40 :
        #regular salary
        reg=40*r
        #overtime salary
        ovr=(h-40)*r*1.5
        pay=reg+ovr   
    else :
        pay=h*r
    return pay

hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))

p = computepay(hrs, rate)
print("Pay", p)
