varA = 1
varB = 2

#"string involved" if either varA or varB are strings
#"bigger" if varA is larger than varB
#"equal" if varA is equal to varB
#"smaller" if varA is smaller than varB

#example
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

#q1
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

#q3
num = 10
while num > 3:
    num -= 1
    print(num) 

#q4
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

#q5
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

