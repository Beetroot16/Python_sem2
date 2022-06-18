smol = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nums = ["0","1","2","3","4","5","6","7","8","9"]
char = ["$","@","#"]

password = input(">>")

flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0

for i in password:
    if i in smol:
        flag1 = 1
    if i in caps:
        flag2 = 1
    if i in nums:
        flag3 = 1
    if i in char:
        flag4 = 1

if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1 and 8<len(password)<15:
    print("gg")
else:
    print("no gg")