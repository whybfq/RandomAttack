import time
import numpy as np
from numpy import random


def mean_squared_error(a, b=0):
    return 0.5 * np.sum((a - b) ** 2)  # np.square(a-b).mean()


iteration = 1
input = np.array([ -98.36499, -45.615704, 35.624004, -91.82865, -158.26599, -147.02539,
                   36.7076, 20.750473, 14.900537, -171.53038, -66.60556, -99.393616,
                   -25.43512, -66.25455, 77.57463, -212.91815, -53.07083, 137.94112,
                   -103.54969, -214.36864 ])

plaintext = np.array([  97, 98, 101, 10, 27 ])

start_time = time.time()

i = 5
W1 = np.random.random_sample((len(input), i))
guess = input.dot(W1)
loss = mean_squared_error(guess, plaintext[ :i ]) + mean_squared_error(plaintext[ i: ])
print(loss)


# min_loss = mean_squared_error(plaintext)
# i = 2
#
# while 1:
#     print(f"Iteration: {iteration}")
#     W1 = np.random.random_sample((len(input), i))
#     guess = input.dot(W1)
#     loss = mean_squared_error(guess, plaintext[ :i ]) + mean_squared_error(plaintext[ i: ])
#     min_loss = min(min_loss, loss)
#     if min_loss < 0.5:
#         break
#     else:
#         print(f"loss is {loss}， minimum loss is {min_loss}")
#         iteration += 1
#     used_time = time.time() - start_time
#     if used_time > 3600:
#         break
# print(f"used_time is: {used_time}")
