import time
import numpy as np
from numpy import random


def mean_squared_error(a, b=0):
    return 0.5 * np.sum((a - b) ** 2)  # np.square(a-b).mean()


iteration = 1
input = np.array([ -314.42844, 70.05509 ])

plaintext = np.array([ 97, 98, 97, 110, 100, 111, 110, 101, 100, 10, 81, 99, 72, 60 ])

start_time = time.time()

# while 1:
#     print(f"Iteration: {iteration}")
#     for i in range(2, len(plaintext) + 1):
#         W1 = np.random.random_sample((len(input), i))
#         guess = input.dot(W1)
#         loss = mean_squared_error(guess, plaintext[ :i ]) + mean_squared_error(plaintext[ i: ])
#         if loss < 0.5:
#             break
#         else:
#             print(loss)
#             iteration += 1
#         used_time = time.time() - start_time
#         if used_time > 3600 * 3:
#             break

min_loss = mean_squared_error(plaintext)
i = 9

while 1:
    print(f"Iteration: {iteration}")
    W1 = np.random.random_sample((len(input), i))
    guess = input.dot(W1)
    loss = mean_squared_error(guess, plaintext[ :i ]) + mean_squared_error(plaintext[ i: ])
    min_loss = min(min_loss, loss)
    if min_loss < 0.5:
        break
    else:
        print(f"loss is {loss}， minimum loss is {min_loss}")
        iteration += 1
    used_time = time.time() - start_time
    if used_time > 3600:
        break
print(f"used_time is: {used_time}")
