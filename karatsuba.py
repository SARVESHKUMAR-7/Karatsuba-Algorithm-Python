import math
def split_at(num , m2):
    num = str(num)
    high = num[:-m2]
    low = num[-m2:]
    return int(high), int(low)

def split_num(x, y):
    a = max(len(str(x)),len(str(y)))
    return math.floor(a/2)

def karatsuba(x, y):
    if x < 10 or  y < 10 :
        return x * y
    
    b = split_num(x, y)
    h1, l1 = split_at(x, b)
    h2, l2 = split_at(y, b)

    z0 = karatsuba(l1, l2)
    z1 = karatsuba(l1 + h1, l2 + h2)
    z2 = karatsuba(h1, h2)

    return (z2 * 10 ** (b * 2)) + ((z1 - z2 - z0) * 10 ** b) + z0

if __name__ == "__main__":
    x = int(input("First number = "))
    y = int(input("Second number = "))
    print(karatsuba(x, y))
