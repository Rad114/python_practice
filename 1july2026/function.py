#star pattern
#left side
for i in range(6):
    print("*"*i)
for i in range(6,0,-1):
    print("*"*i)
 #output-  
'''
*
**
***
****
*****
******
*****
****
***
**
*
'''
#right side
for i in range(6):
    print(" "*(6-i),"*"*i)
for i in range(6,0,-1):
    print(" "*(6-i),"*"*i)
#ouput
'''
      *
     **
    ***
   ****
  *****
 ******
  *****
   ****
    ***
     **
      *
'''
#numnber pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    print
 #output
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5    
'''
#triangle pattern
for i in range(6):
    print(" "*(5-i)+"*"*(2*i+1))
for i in range(6,0,-1):
    print(" "*(6-i)+"*"*(2*i-1))
#output:
'''
     *
    ***
   *****
  *******
 *********
***********
***********
 *********
  *******
   *****
    ***
     *
'''
#problem statement
#1] season based on month
season=input("enter the mon")
if season in ["june","july","august","september"]:
    print("its a rainy season")
elif season in ["ocotober","november","decemeber","january"]:
    print("its a winter season")
else:
    print("its a summer season")

#2] loan eligibility based on credit score
score=int(input("enter the  credit score"))
if score>=90:
    print("you are eligible for the loan")
else:
    print("you are not eligible for the loan")

#3] area of rectangle

length=int(input("enter the length"))
width=int(input("enter the width"))
area= length*width
print("area of rectangle is :",area)

#4] replace vowels with uppercase
string=input("enter the string")
string=string.replace("a","A")
string=string.replace("e","E")
string=string.replace("i","I")
string=string.replace("o","O")
string=string.replace("u","U")
print("output",string)

#same question but using for loop
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch == 'a':
        result += 'A'
    elif ch == 'e':
        result += 'E'
    elif ch == 'i':
        result += 'I'
    elif ch == 'o':
        result += 'O'
    elif ch == 'u':
        result += 'U'
    else:
        result += ch
print("Output:", result)

#5] largest no
number=int(input("enter the 1st number"))
number1=int(input("enter the 2nd number"))
number2=int(input("enter the 3rd number"))
print("Maximum is : ", max(number,number1,number2))

 #2nd method
if number>number1 and number1>number2:
    print("max no",number)
elif number1>number2:
    print("max no:",number1)
else:
    print("max no:",number2)

#default arguments
def greet(name,age=30):
    return f"Hello {name}, you are {age} years old"
message=greet("bob")
print(message)

#arbitrary positional arguments(often denoted as *args)
def calculate_sum(*args):
    total=sum(args)
    return sum(args)
result = calculate_sum(1,2,3,4,5,6,7,8,9)
print(result)

#exmaple reverse the string
def reverse_string(string):
    rev=""
    for ch in string:
        rev=ch+rev
    return rev
text=input("enter a string")
print("reversed string:",reverse_string(text))

#multiply all the numbers in a list (8,2,3,-1,7)
def multiply(mul):
    result = 1
    for i in mul:
        result=result*i
    return result
my_list=[8,2,3,-1,7]
print("multiplied list",multiply(my_list))    