x =int(input("Enter a large integer of seconds to invert"))
hours =x // 3600
minutes= (x%3600) // 60
seconds = x%60
print(x,"seconds are", hours ,"hours,", minutes ,"minutes, and " ,seconds ,"seconds .")