# loopTest = int(input("Enter your lucky number: "))
# while loopTest < 5:
#     if loopTest%2 == 0:
#         print("The number " + str(loopTest) + " is even")
        
#     else:
#         print("The number " + str(loopTest) + " is odd")

#     loopTest = loopTest + 1

# def collatz(number):
#     if number % 2 == 0:
#         print(number//2)
#         return number // 2
#     elif number % 2 == 1:
#         result = 3 * number + 1
#         print(result)
#         return result
# n = input("Give me a number: ")
# while n != 1:
#     n = collatz(int(n))
       
#FOR LOOP TRIAL

# languages = ["python", "R", "Scala", "Java", "C"," Ruby"]

# for index in range(len(languages)):
#     print("Current Language: ", languages[index])

# a =int(input("Enter your Number: ") #taking input from user
# if a>10:
# 	print ("your number is greater than 10")
# else:
# 	print ("your number is smaller than 10")

print ("Enter your age.")
age = int(input())
if age < 13:
	print ("Hey! kid")
elif age>13 and age < 20:
	pass
else:
	print ("You are grown up.")