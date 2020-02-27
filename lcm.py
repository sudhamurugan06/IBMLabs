def compute_lcm(n1,n2):
    if(n1>n2):
       big=n1
    else:
        big=n2
    while True:
        if(big%n1==0)and (big%n2==0):
          lcm=big
          break
        big+=1
    return lcm    
  
noo1=int(input())
noo2=int(input())
print("the lcm is",compute_lcm(noo1,noo2))
