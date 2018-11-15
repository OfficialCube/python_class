# magicians = ["kike", "toke","romoke", "labake", "folake","amaka","caitlyn","tayo","tosin","richard","godfrey"]

# for magician in magicians:
#     print(magician)

# for magician in magicians:
#     print(magician.title() + ", that was a great Trick")

# squares = []

# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# summation = []

# for num in range(1,11):
#     sum = num + 1
#     summation.append(sum)
# print(summation)

# one_million = list(range(1,1000000))

# print(min(one_million))
# print(max(one_million))
# print(sum(one_million))

# olamide = [1, 2, 3, 4, 5, "phone", 3.0]

# print(olamide[5])
# print(olamide[5][4])


# mide = [1,2,3,4,5,6,7,8,9,10]
# mide_m = []
# for num in mide:
#     prin
# for i in range(0,2):
#     print("**" * i * 20)

# names = ["ada", "leo", "bright", "kate", "chukudi"]

# for name in names:
    
#     for value in name:
#         print(value)


# names = ["ada", "leo", "bright", "kate", "chukudi"]


# index = 0
# while True:

#     print(names[index][-1])  
#     print(index)
#     index = index + 1
#     if index == 5:
#         break

# _list = ["baller", "toaster", "baddest", "gbefun","stewing",["monday","tuesday","wednesday","friday","thursday"]]


# i = 0
# while i < 6:
#     print(_list[i])
#     for value in _list[i]:
#         print(value)
#     i = i + 1
Yes = "y"
No = "n"
diagnose = input("Do you have running nose?, Yes or No: ")
if diagnose == Yes:
    diagnose = input("do you have headache?., Yes or No; ")
    if diagnose == Yes:
        diagnose = input("Do you have pain in your eyes: ")
    elif diagnose == No:
        print("Sorry, Take paracetamol")
        if diagnose == Yes:
            print("sorry, you have sinuses")
    elif diagnose == No:
        print("Sorry, Take paracetamol")
elif diagnose == No:
    diagnose = input("do you have fever?, Yes or No: ")
    if diagnose == No:
        print("Kindly, see a doctor")
    elif diagnose == Yes:
        diagnose = input("Do you have mosquitoes in your house?, Yes or No")
        if diagnose == Yes:
            print("Please, Buy Lonart!")
        else:
            print("See a doctor!")
            