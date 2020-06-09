def Series(x, y): 
   
    str_x = str(x) 
   
    sums = x 
    sum_str = str(x) 
   
    for i in range(1, y): 
         
        sum_str = sum_str + str_x 
           
        sums = sums + int(sum_str) 
  
    return sums 
  
x = 2
y = 4
total = Series(x, y) 
print(total) 