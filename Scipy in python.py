from scipy.misc import derivative

# Derivative
def my_function(x):
    return x**2 + x + 1

print(derivative(func = my_function, x0=2))
# my_function()

# ?combination?s

from scipy.special import comb

com = comb(4,2)

print(com)


# Permutations

from scipy.special import perm

per = perm(4,2)

print(per)




