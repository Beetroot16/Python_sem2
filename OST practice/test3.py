n = int(input(">>"))

sum = 0

def numbers(n):
    global sum
    sum = sum + n**2
    if n == 1:
        print(sum)
        return sum
    else:
        numbers(n-1)

numbers(n)