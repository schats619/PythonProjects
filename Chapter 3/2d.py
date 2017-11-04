import cmath

rad = 2
alpha = 180
cosine = cmath.cos(alpha)
sine = cmath.sin(alpha)
print("Find the square root of the function")
value = cmath.sqrt(rad * (cosine * cosine) + rad * (sine * sine))
solution = cmath.sqrt(value)

print("The solution is ", solution)

