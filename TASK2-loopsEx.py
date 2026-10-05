# for i in range(1,4,1):
#     print("Hello World")

# for i in range(2,17,3):
#     print(i)

# for i in range(3,0,-1):
#     print(i)

# for i in range(100,0,-10):
#     print(i)


#sum of first n natural numbers
# n=4
# sum=0
# for i in range(1,4,1):
#     sum=sum+i
# print("sum =",sum)


#find the avg of first n natural numbers using loop
# n=4
# sum=0
# for i in range(1,n,1):
#     sum=sum+i
#     avg=sum/n
# print("Avg of first n Natural Numbers =",avg)


# sum=0
# for i in range(1,4,1):
#     sum=sum+10
# print("sum =",sum)

# n=2
# for i in range(1,11,1):
#     print(n*i)
# print(f"2*1={n*i} 2*2={n*i} 2*3={n*i} 2*4={n*i} 2*5")

#Loops with conditions
# n=100
# for i in range(1,n+1,1):
#     if (i%2==0):
#         print(i)

# s=15
# n=11
# for i in range(s,n-1,-1):
#     if(i%2!=0):
#         print(i)


# s=5
# n=10
# for i in range(s,n+1,1):
#     if(i%5==0):
#         print(i)


#count the even numbers in the range of 1 to 5
# count=0
# for i in range (1,6,1):
#     if (i%2==0):
#      count=count+1
# print("count =",count)


#for Loop Pratice questions.
#avg of numbers 1 to n
# n=int(input("Enter the number :"))
# sum=0
# for i in range (1,n+1,1):
#     sum=sum+i
# avg=sum/n
# print("Average of 1 to n Numbers :",avg)


 #sum of squares of numbers from 1 to n
# n=int(input("Enter the number :"))
# sum=0
# for i in range (1,n+1,1):
#     sum=sum+i**2
# print("Square of the given Number :",sum)


#sum of cubes of numbers 1 to N
# n=int(input("Enter the number :"))
# sum=0
# for i in range (1,n+1,1):
#     sum=sum+i**3
# print("Square of the given Number :",sum)


#power of a number without using the ** operator
# base=int(input("Enter the Base Number :"))
# power=int(input("Enter the power Number:"))
# result=1
# for i in range(1,power+1,1):
#     result=result*base
# print("result =",result)


#First N terms of the fibonacci series
# n=int(input("Enter the N :"))
# a=0
# b=1
# for i in range(1,n,1):
#     print(a)
#     c=a+b
#     a=b
#     b=c


#display the first n terms in series1,1/2,1/3,1/4,1/5
# n=int(input("Enter the Number :"))
# for i in range(1,n+1,1):
#     if i==1:
#       print(1)
#     else:
#        print("1/" + str(i))


#display the first n terms in series 1,11,111,1111,11111
# n=int(input("Enter the Number :"))
# num=0
# for i in range(1,n+1,1):
#     num=num*10+1
#     print(num)


#display numbers in series 1,3,9,27
# n=int(input("Enter the Number :"))
# num=1
# print(num)
# for i in range(1,n+1,1):
#     num=num*3
#     print(num)


#WHILE LOOP
#find the largest from the given number
# n=452
# lar=0
# while(n!=0):
#     ld=n%10
#     if (ld>lar):
#         lar=ld
#     n=n//10
# print(lar)


#find the smallest digit from given number
# n=4523
# small=9
# while(n!=0):
#     ld=n%10
#     if (ld<small):
#         small=ld
#     n=n//10
# print(small)


# i=2
# while(i<=14):
#     print(i)
#     i=i+4


# n=4324
# ld=n%10
# print(ld)
# n=n//10
# print(n)


#reverse the number
# n=2345567
# while(n!=0):
#     ld=n%10
#     print(ld)
#     n=n//10


#count digits in given number
# n=432556
# count=0
# while(n!=0):
#     count=count+1
#     n=n//10
# print(count)

#sum of the given number
# n=432556
# sum=0
# while(n!=0):
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print("sum of the given number = ",sum)





# n = 324416

# while n > 0:
#     temp = n
#     max = 0

#     while temp > 0:
#         ld = temp % 10
#         if ld > max:
#             max = ld
#         temp //= 10


#     print(max, end="")

#     temp = n
#     rem = 0
    
#     while temp > 0:
#         ld = temp % 10
#         if ld != max:
#             rem = rem * 10 + ld
#         temp //= 10

#     n = rem


# sum=0
# for j in range(20,151):
#     count=0
#     for i in range(1,j+1,1):
#         if j%i==0:
#             count=count+1
#     if count==2:
#         sum=sum+i
# print(sum) 



# sum_perfect=0
# count=0
# for j in range(1,1001,1):
#     sum_factors=0
#     for i in range(1,j,1):
#         if j%i==0:
#             sum_factors=sum_factors+i
#     if sum_factors==j:
#         sum_perfect=sum_perfect+j
#         count=count+1
# average=sum_perfect//count
# print(average)


# for i in range(1900,2027,1):
#     if (i%400==0 or i%4==0 and i%100!=0):
#         print(i)


# for i in range(100,501,1):
#     original=i
#     reverse=0
#     while i>0:
#         ld=i%10
#         reverse=reverse*10+ld
#         i=i//10
#     if original==reverse:
#         print(original)


# for i in range(120,851,1):
#     n=i
#     sum_digits=0
#     while n>0:
#         ld=n%10
#         sum_digits=sum_digits+ld
#         n=n//10
#     if sum_digits==10:
#         print(i)


# for j in range(1,51,1):
#     for i in range(j+1,51,1):
#         if i+j==30:
#             print(i,j)



# for j in range(10,301,1):
#     count=0
#     for i in range(1,j+1,1):
#         if j%i==0:
#             count=count+1
#     if count==3:
#         print(i)


# for j in range(20,51,1):
#     for i in range(1,j+1,1):
#         count=0
#         for k in range(1,i+1,1):
#             if i%k==0:
#                 count=count+1
#         if j%i==0 and count==2:
#             print(i)


# for i in range(100,1000,1):
#     n=i
#     sum=0
#     while i>0:
#         ld=i%10
#         sum=sum+ld**3
#         i=i//10
#     if sum==n:
#         print(n)



# max_count=0
# max_num=0
# for j in range(1,101,1):
#     count=0
#     for i in range(1,j+1,1):
#         if j%i==0:
#             count=count+1
#     if count>max_count:
#         max_count=count
#         max_num=j
# print(max_num)
# print(max_count)




# for i in range(1,11,1):
#     print(i)
#     if (i==5):
#         break
# i=20
# while i <= 30:
#     print(i)
#     if (i==24):
#         break

# for i in range(6,21,1):
#     if(i%5==0):
#         print(i)
#         break

# for i in range(28,10,-1):
#     if(i%3==0):
#         print(i)
#         break

# for i in range(3,11,1):
#     print(i)
#     if i ==5:
#         break


# c=0
# for i in range(15,21,1):
#     print(i)

# n=63251
# while n!=0:
#     ld=n%10
#     if(ld%2==0):
#         print(ld)
#         n=n//10


# n=63251
# while n!=0:
#     ld=n%10
#     if(ld<=3):
#         print(ld)
#         break
#         n=n//10


# for i in range(1,11,1):
    
#     if i==5:
#         continue
#     print(i)

# ul=2025
# for i in range(2020,2027,1):
    
#     if i==ul:
#         continue
#     print(i)
# i=1
# while (i<=5):
#     if(i==3):
#         i=i+1
#         continue
#     print(i)
#     i=i+1    


# for i in range(1,11,1):
#     if(i%2==0):
#         continue
#     print(i)

# n=63841
# while(n!=0):
#     ld=n%10
#     if(ld%2!=0):
#         n=n//10
#         continue
#     print(ld)
#     n=n//10

# find the first even digit from the left in
# n = 753914286
# div = 100000000
# while div > 0:
#     digit = n // div
#     if digit % 2 == 0:
#         print ( digit )
#         break
#     n = n % div
#     div = div // 10
    
# find the first prime number between 50 and 100
# for j in range(50,101,1):
#     count=0
#     for i in range(1,i+1,1):
#         if j%i==0:
#             count=count+1
#     if count==2:
#         print(j)
#         break

#find the first number whose digit sum is 10
# for i in range(1,101,1):
#     n=i
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n=n//10
#     if sum==10:
#         print(i)
#         break

#find the first number with exactly 3 divisors b/w 1 to 100
# for j in range(1,101,1):
#     count=0
#     for i in range(1,j+1,1):
#         if j%i==0:
#             count=count+1
#     if count==3:
#         print(j) 
#         break

#stop when 3 consecutive odd numbers occur b/w 1 to 50
# count=0
# for i in range(1,51,1):
#     if i%2!=0:
#         count=count+1
#     if count==3:
#        print(i)
#        break

# find the first palindrome b/w 10 and 500
# for i in range(10,501,1):
#     n=i
#     reverse=0
#     while n>0:
#         ld=n%10
#         reverse=reverse*10+ld
#         n=n//10
#     if i==reverse:
#         print(i)
#         break

# find the first perfect number b/w 1 to 1000
# for j in range(1,1001,1):
#     sum=0
#     for i in range(1,j,1):
#          if j%i==0:
#               sum=sum+i
#     if sum==j:
#         print(j)
#         break

# print the first 5 even numbers
# count=0
# for i in range(1,21,1):
#     if i%2==0:
#         print(i)
#         count=count+1
#     if count==5:
#         break

#print the first 5 prime numbers
# count=0
# for j in range(1,21,1):
#     factors=0
#     for i in range(1,j+1,1):
#         if j%i==0:
#             factors=factors+1
#     if factors==2:
#         print(i)
#         count=count+1
#     if count==5:
#         break

# print the first 3 numbers divisible by 7
# count=0
# for i in range(1,31,1):
#     if i%7==0:
#         print(i)
#         count=count+1
#     if count==3:
#         break
#----------------------------------------------------------------------------
#  CONTINUE

# print 1-30 skipping even numbers
# for i in range(1,31,1):
#     if i%2==0:
#         continue
#     print(i)                                                         

# print 1-40 ,skipping multiples of 4
# for i in range(1,41,1):
#     if i%4==0:
#         continue
#     print(i)

# print 1-30 ,skipping numbers from 10-20
# for i in range(1,31,1):
#     if  i>10 and i<20:
#         continue
#     print(i)

# print 1-50 , skipping multiples of 3
# for i in range(1,51,1):
#     if i%3==0:
#         continue
#     print(i)

#Extract 502304 , skipping digit 0
# n=502304
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit==0:
#         continue
#     print(digit)

# Extract 5832461, printing only even digits
# n=5832461
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit%2!=0:
#         continue
#     print(digit)
        

# Extract 1432578 , skipping odd digits
# n=1432578
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit%2!=0:
#           continue
#     print(digit)
#         

# print 1-200 , skipping multiples of 3 and 5
# for i in range(1,201,1):
#     if i%3==0 or i%5==0:
#         continue
#     print(i)

# print 1-500 , sipping numbers with odd digit sum
# for i in range(1,501,1):
#     n=i
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n=n//10
#     if sum%2!=0:
#         continue
#     print(i)

# print 1-500 skipping numbers containing digit 0
# for i in range(1,501,1):
#     n=i
#     zero=0
#     while n>0:
#         digit=n%10
#         n=n//10
#         if digit==0:
#             zero=1
#     if zero==1:
#         continue
#     print(i)
#-----------------------------------------------------------------------------------------------------------

#BREAK AND CONTINUE

#print 1-50 skip multiples of 3 and stop at 40
# for i in range(1,51,1):
#     if i%3==0:
#         continue
#     if i==40:
#         break
#     print(i)

#print odd numbers skip even and stop at multiple of 7
# for i in range(1,51,1):
#     if i%2==0:
#         continue
#     if i%7==0:
#         break
#     print(i)

# Extract 5830421, skip odd digits stop at 0
# n=5830421
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit%2!=0:
#         continue
#     if digit==0:
#         break
#     print(digit)

# Extract 8325147, print digits until 5
# n=8325147
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit==5:
#         break
#     print(digit)

# search from 51, skip non-multiples of 9 stop at the first multiple of 9
# for i in range(51,101,1):
#     if i%9!=0:
#         continue
#     if i%9==0:
#         print(i)
#         break

