fhand=open("binh-ngo-dai-cao.txt")
hist= {}
for line in fhand:
    line = line.rstrip()
    line=line.lower()
    for c in line:
        c = c.rstrip()
        if c not in hist:
            hist[c] = 1
        else:
            hist[c] += 1
print(hist)
