# def add(a,b):
#         sum = a + b
#         return sum
# added_val = add(2,3)
# print(added_val)

# def divide(a,b):
#         divide = a/b
#         return divide
# div_val = divide(2,3)
# print(div_val)

# def multiply(a,b):
#         multiply = a*b
#         return multiply
# multiply_val = multiply(2,3)
# print(multiply_val)

# def subtract(a,b):
#         subtract = a-b
#         return subtract
# subtract_val = subtract(2,3)
# print(subtract_val)

# def upper(name):

#     return name.upper()

# print('upper caase is' ,upper('ayomide'))


#Simple programme to add two fractions and give answer as fraction 

# num1 = int(input ("Enter Numerator 1 :"))
# den1 = int(input ("Enter Denominator 1 :"))
# num2 = int(input ("Enter Numerator 2 : "))
# den2 = int(input ("Enter Denominator 2 :"))

# full_den = den1*den2

# up1 = (full_den/den1)*num1
# up2 = (full_den/den2)*num2

# full_num = up1 + up2
# print ("\nAnswer = ", full_num, "/", full_den)
# print("\n", num1, "/", den1, "+", num2, "/", den2, "is ---> ", full_num, "/", full_den)
x = 81
y = 36
def function_ata (x,y):
    for i in reversed(range(2,min(x,y))):
        # print(i)
        if (x % i ==0 and y % i ==0):
            x=x/i
            y=y/i
            print (x,y)

function_ata(39,169)
  