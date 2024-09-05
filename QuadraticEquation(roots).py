#input= a=1 b=-3 c=2
#output = roots:(2.0,1.0)



#For calculating roots

#formula = d=(b**2)-4*a*c
#          root1=(-b+(d**(0.5)))/2*a



a=int(input("Give a:"))
b=int(input("Give b:"))
c=int(input("Give c:"))

d=(b**2)-4*a*c
root1=(-b+(d**(0.5)))/2*a
root2=(-b-(d**(1/2)))/2*a

print(f"Roots:({root1},{root2})")