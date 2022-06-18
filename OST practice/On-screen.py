x,y=map(int,input().split())

even = [2,4,6,8]
odd = [1,3,5,7]

if x in even and y in even:
    print("black")
elif x in odd and y in odd:
    print("black")
elif x in odd and y in even:
    print("white")
elif x in even and y in odd:
    print("white")




