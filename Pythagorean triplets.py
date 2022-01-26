# Pythagorean triplets
# We know that in a triangle a^2+b^2 = c^2
# => √a^2+b^2 = c
# Sometimes, a^2+b^2 is a perfect square and sometimes it isn't but it will always be a whole number
# So, if we consider one of them to be the coefficient of imaginary numbers, a+bi, then on squaring this,
# Now let's consider a graph
"""
            /|
           / |
 √a^2+b^2 /  | (b i)
         /   |
        /____|
          (a)
"""
# So, if we square both sides,
# (a+bi)(a+bi)          = a^2+b^2
# (a^2 +(bi)^2 + 2abi)  = a^2+b^2
# (a^2-b^2      +    2abi)       = a^2+b^2
#   real           imaginary  
#   part             part
# (x-axis)         (y-axis)
"""
            /|
           / |
  a^2+b^2 /  | (abi)
         /   |
        /    |
       /     |
      /      |
     /       |
    /________|
    (a^2-b^2)
"""

def py_triplets():
    x = int(input('Enter any whole number:'))
    y = int(input('Enter any whole number:'))
    a = max(x,y)
    b = min(x,y)
    print("A Python triplet made using the above integers:\n", "("+str(a**2-b**2)+","+str(2*a*b)+","+str(a**2+b**2)+")")

py_triplets()
