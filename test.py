for i in range(5):
    print (i)
    if i > 2:
        print('bigger than 2')
    print('done with i', i)
print('all done')        

x=4 
if x < 2:
    print("smaller")
else:
    print("bigger")

x=3
if x>2:
    print("smaller")
elif x<10:
    print("bigger")
else:
    print("biggest")
    
astr = "hello Bob"
try:
    instr=int(astr)
except:
    instr=3
print(instr)
astr = "17"
try:
    instr=int(astr)
except:
    instr =3
print(instr)

astr = input("ENTER A NUMBER:")
try:
    instr=int(astr)
except:
    instr = -1
if instr>=0:
    print("good job")
else:
    print("not a number stupid ass")

#Calculating pay for employee
pph= 4
hrs= (input("how many hours have you worked today?:"))
total_pay =pph* hrs
try:
    total_pay=int(hrs)*pph
except:
    hrs=-1
if int(hrs)>0:
    print("Your total pay is", "$", total_pay)
else:
    print("ERROR! Please Enter A Valid Number")   
     
print("DONE")
tiny = max("hello world")
print(tiny)

def seventeen_darling():
    print("You know without you I'm so lonely")
    print("When you're not here 911 calling")

print(total_pay)
seventeen_darling()

def greet(lang):
    if lang == 'es':
        print('hola')
    elif lang== 'fr':
        print('bonjour')
    else:
        print('hello')       
greet('sjan')
greet('fr')
greet('es')         
def greet():
    return "hello"
print(greet(), 'DALLY')
    
n = 5
while n>0:
    print(n) 
    n=n-1
print("BLASTOFF")       
print(n)
n=0
while n>0:
    print("rinse")
    print('lather')
print('dry')    
while True:
    line = input(">")
    if line == "done":
        break 
    print(line)
print('FINISH')    

while True:
    line = input(">")
    if line[0]=="#":
        continue
    if line =='done':
        break
    print(line)
print('DONE')    
for i in [5, 4, 3, 2, 1]:
    print (i)
print('Blastoff')    
friends = ['joey', 'chandler', 'monica', 'rachel', 'phoebe', 'ross']
for friend in friends:
    print('Merry Christmas', friend)
smallest=None
print('before',smallest)
for value in [12, 4, 6, 78, 43, 67, 2]:
    if smallest is None:
        smallest = value
    elif value<smallest:
        smallest=value
    print(smallest, value)
print("after", smallest)  
greeting = "hello"+ " " + "there"
print(greeting)
stuff = ("hello world")
ppp= type(stuff)
print(ppp)
greet = "hello world"
trt=greet.upper()
print(trt)


