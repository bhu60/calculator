def eTo(n):
    s = 1
    f = 1
    for i in range(1, 1000):
        f *= i
        s += n ** i / f
    return s

e = eTo(1)

def ln(n):
    output = 0
    while n > 2:
        n /= e
        output += 1
    n -= 1
    s = n
    for i in range(2, 100000):
        if (i % 2 == 1):
            s += n ** i / i
        else:
            s -= n ** i / i
    output += s
    return output

def log(n, a):
    return ln(n) / ln(a)

def derivative(f, n):
    smallest = 2 ** -40
    x = n + smallest
    thing1 = eval(str(f))
    x = n
    thing2 = eval(str(f))
    return (thing1 - thing2) / smallest

def leftSum(f, n, start, end):
    s = 0
    a = (end - start) / n
    curr = start
    while(curr < end):
        x = curr
        s += a * eval(str(f))
        curr += a
    return s

def rightSum(f, n, start, end):
    s = 0
    a = (end - start) / n
    curr = start + a
    while(curr <= end):
        x = curr
        s += a * eval(str(f))
        curr += a
    return s

def midSum(f, n, start, end):
    s = 0
    dx = (end - start) / n
    curr = start + dx / 2
    while(curr < end):
        x = curr
        s += dx * eval(str(f))
        curr += dx
    return s

def trapSum(f, n, start, end):
    s = 0
    a = (end - start) / n
    curr = start
    while(curr <= end):
        x = curr
        if(curr == start or curr == end):
            s += eval(str(f))
        else:
            s += 2 * eval(str(f))
        curr += a
    return s * a / 2

def integral(f, start, end):
    s1 = 0
    s2 = 0
    smallest = 2 ** -10
    while (start < end):
        x = start
        s2 += eval(str(f)) * smallest
        start += smallest
        s1 += eval(str(f)) * smallest
    return (s1 + s2) / 2

def eulerMethod(differential, start, a, b, deltaN):
    # smallest = 2 ** -21
    smallest = deltaN
    while a < b:
        x = a
        y = start
        start += eval(differential) * smallest
        a += smallest
    return start

def newtonMethod(f, a):
    x = a
    for i in range(10**5):
        if derivative(f,x) == 0:
            if eval(str(f)) == 0:
                return apx
            else:
                return None
        x = x - eval(str(f))/(derivative(f,x))
    return x

def intersection(f1, f2, a):
    return newtonMethod(str(f1) + "-" + str(f2),a)

def sin(n):
    n %= 2 * pi() 
    s = n
    f = 1
    for i in range(3, 171, 2):
        f *= i * (i - 1)
        if (i // 2) % 2 != 1:
            s += ((n ** i) / f)
        else:
            s -= ((n ** i) / f)
    return s

def cos(n):
    n %= 2 * pi()
    s = 1
    f = 1
    for i in range(2, 172, 2):
        f *= i * (i - 1)
        if (i // 2) % 2 != 1:
            s += ((n ** i) / f)
        else:
            s -= ((n ** i) / f)
    return s

def tan(n):
    return sin(n) / cos(n)
    
def arcsin(n):
    s = n
    a = 1
    b = 1
    for i in range(3, 171, 2):
        a *= (i - 1) * (i - 2)
        b *= (i - 1) // 2
        s += ((n ** i) * a) / ((4 ** ((i - 1) // 2)) * (b ** 2) * i)
    return s

def arccos(n):
    return pi() - arcsin(n)

def arctan(n):
    return arcsin(n / (1 + n **2) ** 0.5)

def arcsec(n):
    return arccos(1 / n)

def arccsc(n):
    return arcsin(1 / n)

def arccot(n):
    return arctan(1 / n)

def pi():
    return 4 * (4 * arctan(1 / 5) - arctan(1 / 239))

print(0.5 * integral("((3 * x ** 0.5) * sin (x ** 2)) ** 2", 0, pi() / 2))