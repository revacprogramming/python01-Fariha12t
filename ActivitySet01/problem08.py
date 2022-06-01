# Files

fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
      
   
        count=count+1
        a=line.find('0')
        b=line[a:]
        c=float(b)
        total=total+c
   
print('Average spam confidence:',total/count)
#file name is file1.txt