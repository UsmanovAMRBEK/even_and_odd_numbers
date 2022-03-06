from itertools import count


var_int=1287
count_odd_digits=var_int//1000%2+var_int//100%2+var_int//10%2+var_int%2
print(count_odd_digits)