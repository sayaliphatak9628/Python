'''
#introduction to files

#f=open("demofile.txt","x")
f=open("demofile.txt","w")
f.write("Hello World")
f.close()
print(f.read())

f=open("demofile.txt","a")
f.write("\nHey there!")
f.close()

f=open("demofile.txt","r")
print(f.read())

xfile=open("demofile.txt")
for i in xfile:
    print(i)

#counting lines in file

f= open("demofile.txt")
count=0
for i in f:
   # print(i)
    count=count+1
print("Line count: ",count)

#read whole file
f=open("demofile.txt")
st=f.read()
print(len(st))
print(st[:4])
if "Hey" in st:
    print("Yessssss")

#searching in a file
f=open("demofile.txt")
#print(f.read())
for line in f:
    #print(line)
   # print(line.rstrip())
    if not line.startswith("Hey"):
        continue
    print(line)

#taking file name from user

fname=input("Enter file name: ")
try:
    fhand=open(fname)
except:
    print("File cannot be opened")
    quit()
#fhand=open(fname)

count=0
for line in fhand:
    if line.startswith("Hey"):
        count=count+1
print("Count",count)

#files assignment
#f=open("demo.txt","x")
f=open("demo.txt","w")
f.write("From xyz.vhy@perfectplanb.net Sat Jan 5 09:14:16 2008.Return-Path: Received: from murder (perfectplanb.net [141.211.14.90]) by mail.perfectplanb.net with LMTPA;Sat, 05 Jan 2008 09:14:16 -0500")
f.close()

fname=open("demo.txt")
for line in fname:
    lines=line.rstrip()
    print(line.upper())
'''
