import cmath
a=int(input())
b=int(input())
c=int(input())
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("The solution are {0} and {1}".format(sol1,sol2))
