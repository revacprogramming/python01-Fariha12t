# Dictionaries

filename = "dataset/mbox-short.txt"

handle = open(filename)

counts = dict()
for line in handle:
    if line.startswith('From '):
        line = line.split()
        sender = line[1:2]
        for email in sender:
            counts[email] = counts.get(email, 0) + 1


most_count = None
most_sender = None

for key,value in counts.items():
    if most_count is None or value > most_count:
        most_count = value
        most_sender = key

print(most_sender, most_count)