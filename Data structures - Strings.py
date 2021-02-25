'''
#strings and len function
s = 'foobar'
print(s[0])
print(s[5])
#print(s[7])

print(len(s))

#string looping

string='perfectplanb'
for i in string:
    print(i)

string='perfectplanb'
for i in range(0,len(string)):
    print(string[i])

word = 'ohnananana'
count=0
for i in word:
    if i == 'n':
        count=count+1

print(count)

#string slicing

s='helloworld'
first_five_char= s[:6]
print(first_five_char)

third_to_fifth_char= s[2:6]
print(third_to_fifth_char)

characters = s[::-1]
print(characters)

#string library functions

string='perfectplanb'
print(string.isupper())
print(string.islower())

string2='PERFECTPLANB'
print(string2.isupper())
print(string2.islower())
print(string2.lower())

#string whitespace

s= '        hello there               '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

#parsing and extracting

data = 'sayali phatak9628@gmail.com'
atpos = data.find('9')
print(atpos)
stpos = data.find(' ',atpos)
print(stpos)
host = data[atpos+1:stpos]
print(host)
'''
#string assignment
str = 'Perfect-Plan-B:0.7541 '
atpos=str.find(':')
print(atpos)
stpos=str.find(' ')
print(stpos)
host = str[atpos+1:stpos]
print(host)

y = float(.7541)
print(y)
