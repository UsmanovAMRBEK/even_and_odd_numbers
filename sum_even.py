number = 2225

n1=number%10
number//=10

n2=number%10
number//=10

n3=number%10
number//=10

n4=number%10
number//=10
print(n1*((n1+1)%2)+n2*((n2+1)%2)+n3*((n3+1)%2)+n4*((n4+1)%2))