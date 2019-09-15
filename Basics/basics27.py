n,m=(map(int,input().split()))
list1=list(map(int,input().split()))
rep=list1.count(m)
if(rep>1):
    print(rep)

elif(m not in list1):
    print('-1')
else:
    print('0')