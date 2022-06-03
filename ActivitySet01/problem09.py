# Lists

filename = "dataset,romeo.txt"
fh = open(filename)
stuff= list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for w in words:
        if w not in stuff:
            stuff.append(w)
stuff.sort()
print(stuff)
 #done