# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter rate:")
r=float(rate)
if h>40 :
    reg=40*r
    ovr=(h-40)*r*1.5
    pay=reg+ovr
    print("Pay:",pay)
else :
        pay=h*r
        print("Pay:",pay)
        
        
