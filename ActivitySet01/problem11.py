# Tuples

filename = "dataset/mbox-short.txt"
handle = open(filename)
d1 = dict()
for line in handle:
    if line.startswith("From "): 
        lst = line.split()
        num = lst[5]
        time = num.split(":")
        d1[time[0]] = d1.get(time[0],0) + 1
ftime = sorted(d1.items())
for (k,v) in ftime:
    print(k,v)