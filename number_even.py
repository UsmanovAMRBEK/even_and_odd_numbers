# var_int=4256
# count_even_digits=(var_int//1000+1)%2+(var_int//100+1)%2+(var_int//10+1)%2+(var_int+1)%2
# print(count_even_digits)

var_int=4256
count_odd_digits=var_int//1000%2+var_int//100%2+var_int//10%2+var_int%2
print(4-count_odd_digits)
