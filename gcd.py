def compute_hcf(n1,n2):
    if(n1>n2):
       small=n2
    else:
        small=n1
    for i in range(1,small+1):
        if(n1%i==0)and(n2%i==0):
            hcf=i
    return hcf        
 
nu1=int(input())
nu2=int(input())
print("the lcm is",compute_hcf(nu1,nu2))
