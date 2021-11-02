#referensi: https://math.stackexchange.com/questions/735093/method-of-solving-extended-euclidean-algorithm-for-three-numbers

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
  
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

 #mendapatkan semua koefisien dari a1*x1 + a2*x2 + a3*x3 + ... + an*xn = gcd(a1,a2,a3,...,an)
 def ExtendGCD(numbers):
    if len(numbers) > 1:
        g, x1, x2 = egcd(numbers[0], numbers[1])
        coef = [x1, x2]
        GeCeDe = g
        for i in range(2, len(numbers)):
            g, coef_mul, y = egcd(GeCeDe, numbers[i])
            coef = [c*coef_mul for c in coef]
            coef.append(y)
            GeCeDe = g
    return GeCeDe, coef
