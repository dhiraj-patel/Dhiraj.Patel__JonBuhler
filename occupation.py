import csv,random

f = open("occupations.csv","r").readlines()[1:-1]

occs = csv.reader(f)
dict = {}
for job in occs:
    dict[job[0]] = float(job[1])

def main():
    y = 0
    x = random.randrange(0,100)
    for i in dict:
        i = i + dict[i]
        
        if x <= y:
            return i
print(main())
