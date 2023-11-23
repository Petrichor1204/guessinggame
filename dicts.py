#dictionaries in python


ages = dict()
ages['grace']=3
ages['betty']=5
ages['jessica']=2
print(ages)
names = ['harley', 'grace', 'betty', 'cynthia']
for name in names:
    if name not in ages:
        ages[name]=1
    else:
        ages[name] = ages[name] + 1 
print(ages)         
for name in names:
    ages[name]=ages.get(name, 0) + 1
print(ages)    

#counting words in a text
counts=dict()
print('Enter a line of text:')
line = input('')
words=line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word]=counts.get(word, 0) + 1
print('Counts:', counts)    
for key in ages:
    print(key, ages[key])
print(list(ages.values()))    
print(list(ages.keys()))

name=input('enter file:')
handle= open(name)

conts=dict()
for line in handle:
    words=line.split()
    for word in words:
        conts[word]=conts.get(word, 0)+1
print(words)
print(conts)       

bigcont =None 
bigword = None
for word,cont in conts.items():
    if bigcont is None or cont>bigcont:
        bigword = word
        bigcont = cont 
print(bigword, bigcont)              