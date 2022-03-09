number = 1234

n1=number%10
number//=10

n2=number%10
number//=10

n3=number%10
number//=10

n4=number%10
number//=10

print(n1*(n1%2+1)+n2*(n2%2+1)+n3*(n3%2+1)+n4*(n4%2+1))