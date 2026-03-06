x=int(input("Enter a number greater than 9"))

counter=0
print(x, end="")
while x >9:
    sum=0
    temp=x

    while x>0:
        sum=sum + x%10
        x = x // 10

    print(f" -> {sum}", end="")

    counter=counter+1
    x = sum
print()
print("Final value :" , sum)
print("Total steps:", counter)



x=int(input("Enter a number between 10 and 100 inclusive:"))
while x<10 or x>100:
     x=int(input("Invalid input.Enter a number between 10 and 100 inclusive:"))

i=1
fizcount=0
buzcount=0
fbcount=0
while i<= x:
     if i%7==0:
         print(i,"is skipped")
     elif i%15 ==0:
         print("FizzBuzz")
         fbcount+=1

     elif i%3 ==0:
         print("Fizz")
         fizcount+=1

     elif i%5 ==0:
         print("Buzz")
         buzcount+=1
     else :
         print(i)
     i +=1


print("--Summary--")
print("Fizz count : ", fizcount)
print("Buzz count : ", buzcount)
print("FizBuzz count : ", fbcount)

n = int(input("Please enter a number between 3 and 9: "))
if 3 <= n <= 9:

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
else:
    print("Invalid input!")