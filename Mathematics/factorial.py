N=int(input())
fact=1
for i in range(1,N+1):
    
    fact=fact*N
    N=N - 1
print(fact)
