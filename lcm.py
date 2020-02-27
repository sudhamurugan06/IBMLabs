def compute_lcm(n1,n2):
    if(n1>n2):
       big=n1
    else:
        big=n2
    while True:
        if(big%n1==0)and (big%n2==0):
          lcm=big
          break
        big+=n1
    return lcm    
  
n1=int(input())
n2=int(input())
print("the lcm is",compute_lcm(n1,n2))
