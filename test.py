print("hello world")
a=10
b=60
c=a+b
print('addition of two numbers is',c)
#1) Generate the first 50 odd and even numbers without including 0
#first 50 even numbers
n = 50;
print("First 50 even numbers are ")
for num in range(2,n*2+1):
  if num%2 ==0:
    print(num,end=" ,")


# first 50 odd numbers

n_o = 50;
print("\n First 50 odd numbers are ")
for num in range(1,n_o*2+1):
  if num%2 !=0:
    print(num,end=" ,")

import math
r1=2.45
r2=3.7
h1=7.9
h2=12.6
volume_of_first_cylinder=math.pi*r1*r1*h1
volume_of_second_cylinder=math.pi*r2*r2*h2
total=volume_of_first_cylinder+volume_of_second_cylinder
print("\n Volume of first cylinder is",'%.2f'%volume_of_first_cylinder,'\n & \n the Volume of second cylinder is',
      '%.2f'%volume_of_second_cylinder,"\n\n Total Volume of two cylinder is",'%.2f'%total)  

sent= "CRICket is a popular Sport. CRICKEt originated in England and slowly cricket became a popular sport. cricKET is also a name of an insect."
word_to_find= "CrIcKeT"
count = sent.count(word_to_find)

# print count
print("The count is:", count)