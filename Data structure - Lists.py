'''
#lists introduction
li=["apples","oranges","mangoes",12,95]
print(li)
li[1]="peach"
print(li)
li[4]=55
print(li)

string='apple'
string[0]='A'
print(string)

#len range
li=["apple","orange","banana",12]
for l in li:
    print(l)

for s in range(len(li)):
    print(li[s])

#lists continued ...
#list slicing
t=[15,18,2,16,91,16,88]
print(t[1:5])
print(t[:2])
print(t[4:])
print(t[:])

#building list from scratch
stuff=list()
stuff.append('book')
stuff.append(12)
print(stuff)

#using in for searching
li=[5,16,82,46,75,18,46,33]
9 in li

#change order of list
li =['Sayali','Vilas','Phatak']
#print(li)
li.sort()
print(li)
print(li[2])

#sum & avg of numbers
#without using lists
total=0
count=0
while True:
    nm = input("Enter a number: ")
    if nm == 'done':
        break
    val = float(nm)
    total = total + val
    count = count + 1
    avg = total/count
print("Average: ",avg)
    
#using list
stuff = list()
while True:
    nm = input("Enter a number: ")
    if nm =='done':
        break
    val=float(nm)
    stuff.append(val)
    avg = sum(stuff)/len(stuff)
print("Average: ",avg)

#split function
string = "Sayali Vilas Phatak"
stuff= string.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for words in stuff:
    print(words)

stuff = 'A lot                   of        space'
etc = stuff.split()
print(etc)

stuff2 = 'first;second;third'
e = stuff2.split()
print(e)
print(len(e))
et = stuff2.split(';')
print(et)
print(len(et))


line = 'From sayaliphatak9628@gmail.com 97 98 99'
stuff = line.split()
print(stuff)
email = stuff[1]
domain = email.split('@')
print(domain)
print(domain[1])
'''

han = open("file.txt")
for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds)<3 or wds[0]!='From':
        continue
    print(wds[5])

















 







