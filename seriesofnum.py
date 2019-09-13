N=int(input('You are given a number ‘n’'))

sum=0
for i in range(0,N + 1):
    sum=sum + N
    N=N -1
print('Print the nth number of series.',sum)
