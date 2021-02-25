'''
#dictionary introduction

purse= dict()
purse['candy']= 5
purse['chocolate']=75
purse['icecream']=22
print(purse)
purse['candy']=purse['candy']+51
print(purse)

#dictionary literals

abc = {'hello':27,'heyyy':26,'hola':25}
print(abc)
edf = {}
print(edf)

#function count example
stuff = dict()
line = input("Enter a line: ")
word= line.split()
print(word)
for wor in word:
    stuff[wor] = stuff.get(wor,0)+1
print("Counts",stuff)

#loops in dictionaries

counts = {'jan':10,'feb':20,'mar':30,'apr':40}
for key in counts:
    print(key,counts[key])
    
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items()) #is converted into list and displayed both keys and values

for aa,bb in counts.items(): # for two iterations using dict
    print(aa,bb)
'''
para = dict()
line = input("Enter a text: ")
word =line.split()
for wor in word:
    para[wor]=para.get(wor,0)+1
print("Counts: ",para)
