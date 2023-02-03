print('A small program to calculate the (3n+1) sequence of a natrual number')

while(True):
    print('Type a number for which you want to calculate the (3n+1) sequence:')
    response = input('> ')
    if response.isdecimal() and (0 < int(response)):
        num = int(response)
        break

print(num, end='', flush=True)
count = 0
while(num!=1):
    if(num%2 == 0):
        num = num//2
    else:
        num = 3*num+1
    print(', ' + str(num), end='', flush=True)
    count += 1
print()
print('It took {} steps to reach 1.'.format(count))