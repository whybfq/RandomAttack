import numpy as np
from numpy import random

input = [ -314.42844, 70.05509 ]

plaintext = [ 97, 98, 97, 110, 100, 111, 110, 101, 100, 10, 81, 99, 72, 60 ]


x = random.rand(2, 14)
print(input.dot(input, x))
