hanoi(n,start,temp,final):
    magic(n-1,start --> temp) #moves n-1 discs from start to finish
    move(N start --> final)
    magic(n-1, temp --> final)

def hanoi(n,start,temp,final):#f(n)
    if n>0:
        hanoi(n-1,start,final,temp)#f(n-1)
        final=final+[start[-1]]#or: final=final+[start[len(start)-1]]
        hanoi(n-1,temp,start,final)#f(n-1)
