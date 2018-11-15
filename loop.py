# _usern = input("Enter something separated by a comma: ")
# test = (_usern.lower()).split()
# if test [0] == "age":
#     print("thank you for telling me your age")
# elif test[0] == "name":
#     print ("thank you for telling me your age")
# else:
#     print("i dont know what you told me")

# baby_names = open("babies.csv","r")

# name_str = baby_names.read() #assign csv data to a variable
# name_list = []
# splitted_list = (name_str.split()) #split into individual babies
# list_length = len(splitted_list) #list length to use in for loop over split cell

# for i in range(list_length):
#     target_value = splitted_list[i].split(",")
#     name_list.append(target_value[2])
#     john_list = name_list.count("Ian")

# baby_names.close()kj




# non_duplicate_list = []
# occurences = []
# length_name_list = len(name_list)

# for i in range(length_name_list):
#     if name_list[i] in non_duplicate_list:
#         pass
#     elif name_list not in non_duplicate_list:
#         occurence = name_list.count(name_list[i])
#         non_duplicate_list.append(name_list[i])
#         occurences.append(occurence)

# # print(len(non_duplicate_list), len(name_list))

# for i in range(len(non_duplicate_list)):
#     pass
#     # print("name : ", non_duplicate_list[i], "\t\toccurence : ", occurences[i])

# my_file = open("max_occurence.txt", "w")

# for i in range(length_name_list): 
#     my_file.write("")
#     x = occurences.index(max(occurences))

# print(non_duplicate_list[x])

# my_file.close()


# var = "i am a baby girl"
# print(var.upper())
# print(var.capitalize())
# print(var.index("b"))
# print(count(var))

# var = 'ruby is walking a dog'
# print(var.split(' ')) 

# var_split = var.split(" ")
# print(''.join(var_split)) 

# computer_brands = ["apple","asus","lenovo","samsung","dell"]

# for computer in computer_brands:
#     print(computer)


# numbers = [1,15,12,13,18,99,100,76,24,76,11,45]
# sum = 0
# for number in numbers:
#    sum = sum + number
# print (sum)
# guys = ["John", "Sam", "Jill"]
# for name in guys:
#     print("Hello " + name)

# for i in range(10):
#     print (i)

# total = 0
# for i in 2,4,6,8:
#     print(i)
#     total = total + i

# print(total)

# for i in range(10):
#     turtle.forward(15)
#     turtle.penup()
#     turtle.forward()
#     turtle.pendown(5

loopTest = int(input("Enter your lucky number: "))
while loopTest < 5:
    if loopTest%2 == 0:
        print("The number " + str(loopTest) + "is even")
        
    else:
        print("The number " + str(loopTest) + " is odd")

    loopTest = loopTest + 1