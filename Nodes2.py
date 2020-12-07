import time
import numpy as np
from numpy import random


def mean_squared_error(a, b=0):
    return 0.5 * np.sum((a - b) ** 2)  # np.square(a-b).mean()


iteration = 1
input = np.array([ -314.42844, 70.05509 ])

plaintext = np.array([ 97, 98, 97, 110, 100, 111, 110, 101, 100, 10, 81, 99, 72, 60 ])

start_time = time.time()

# for i in range(2, len(plaintext) + 1):
#     W1 = (3 + 3) * np.random.random_sample((len(input), i)) - 3
#     guess = input.dot(W1)
#     loss = mean_squared_error(guess, plaintext[ :i ]) + mean_squared_error(plaintext[ i: ])
# print(np.sum(guess == plaintext))

min_loss = len(plaintext)
i = 2  # the number of nodes

while 1:
    print(f"Iteration: {iteration}")
    W1 = (4 + 4) * np.random.random_sample((len(input), i)) - 4
    guess = input.dot(W1)
    # loss = mean_squared_error(guess, plaintext[ :i ]) + mean_squared_error(plaintext[ i: ])
    error = min(min_loss, ( len(plaintext) - np.sum(guess == plaintext[:i]) ) )
    if error < 1:
        break
    else:
        print(f"Minimum error is {error}")
        iteration += 1
    used_time = time.time() - start_time
    if used_time > 3600 * 8:
        break
print(f"used_time is: {used_time}")
