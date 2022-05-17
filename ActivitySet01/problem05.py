# Functions


def computepay(h, r):
    if h>40 :
        #regular
        reg=h*r
        #overtime45
        
        ovr=(h-40)*(r*0.5)
        pay=reg+ovr   
    else :
        pay=h*r
    return pay

hrs = float(input("Enter Hours:"))
rate=float(input("Enter rate:"))

p = computepay(hrs, rate)
print("Pay", p)
