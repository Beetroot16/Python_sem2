list = list(map(str,(input("").split())))

vowels = ["a","e","i","o","u"]

score = 0
for i in list:
    count = 0
    for  x in i:
        if x in vowels:
            count += 1
        # print(count)
    if count%2 == 0 and count != 0:
        score += 2
    else:
        score += 1

print(score)
    