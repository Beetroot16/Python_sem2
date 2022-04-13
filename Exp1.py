# QUESTION 1

print("\nQUESTION 1 \n")
length = int(input("Enter length: "))
width = int(input("Enter width: "))
height = int(input("Enter heigth: "))

vol = length * width * height

dia = ((length)**2 + (width)**2 + (height)**2)**0.5

print("The volume of the rectangular prism is "+ str(vol) + " and the Diagonal length of the rectangular cube is " + str(dia))

#QUESTION 2

print("\nQUESTION 2 \n")
var_1 = str("Python programming")

print(var_1.index("i"))
print(len(var_1))
print(var_1[0:6])
print(var_1[7:14])
print(var_1[2:4]+var_1[15:18])
print(var_1.upper())

var_2 = " is interesting"

print(var_1 + var_2)

print(var_1.startswith("P"))
print(var_1.replace("m","t"))