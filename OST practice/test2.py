id = input(str("Enter your user-id: "))
password = input(str("Enter user password: "))

list = []

k = 0
d = 0
s = 0

def breaking(list):
    global k,d,s
    for i in list:
        if i == "dairy-milk":
            d += 1
        elif i == "kit-kat":
            k += 1
        elif i == "snicker":
            s += 1
        
    print("Name \t Quantity \t Price(Rs)")
    print("Dairy-milk \t" + str(d) + "\t" + str(d*10))
    print("Kit-Kat \t" + str(k) + "\t" + str(k*15))
    print("Snicker \t" + str(s) + "\t" + str(s*10))

    print("total = " + str(s*10 + k*15 + d*10))

if password == "bbb" and id == "XYZ":
    print("You can procede ")
    while True:
        t = int(input(">> "))
        if t == 1:
            list.append("dairy-milk")
        elif t == 2:
            list.append("kit-kat")
        elif t == 3:
            list.append("snicker")
        elif t == -1:
            breaking(list)
            break
        else:
            print("invalid")
    

