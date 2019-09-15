N,M=(map(int,input().split()))
square=N*M
if(square%N==0 and square%M==0):
    if(N==M):
        print("yes")
    else:
        print("no")
