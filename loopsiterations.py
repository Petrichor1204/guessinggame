n=10
while n>0:
    print (n)
    n=n-1
print('blastoff')
print(n)

#breaking the loop
while True:
    line=input('>')
    if line=='done':
        break
    print(line)
print('Done')    

#using continue
while True:
    line=input('>')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print('Done')    
#iterations
numbers = [1,2,3,4,5]
for i in numbers:
    print(i)
print('go')    
#in strings
friends = ['Ned','Ham','Joey']
for friend in friends:
    print('Merry Christmas,',friend)
print('yass!')    

lsf = 7
print('before:', lsf)
for the_num in [8,15,35,76,5,67,2,13,4]:
    if the_num>lsf:
        lsf=the_num
    print(lsf, the_num)
print('after:',lsf)        

count=0
sum=0
print('before:', count, sum)
for value in [23,34,45,56,78,90]:
    count=count + 1
    sum = sum + value
    print(count, sum)
print('after:',count, sum, count/sum)    

#search using a Boolean variable
found= False
print('before:', found)
for value in [2,4,5,6,7,8]:
    if value==6:
        found=True
    print(found,value)
print('after:',found)        

#finding smallest value
sv = None
print('before')
for value in [5,34,24,15,64,14,53,67,3,1,2]:
    if sv is None:
        sv = value
    elif value<sv:
        sv=value
    print(sv, value)
print('after:', sv)            