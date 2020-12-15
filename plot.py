import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

Nodes = np.arange(2, 15)  # 13 nodes
# print(Nodes)

Times = np.array([ 28800.00003
                     , 28800
                     , 28800.00002
                     , 28800
                     , 28800.00002
                     , 28800.00004
                     , 28800.00823
                     , 28800.00003
                     , 28800.00001
                     , 28800
                     , 28800
                     , 28800.00004
                     , 28800.00002 ])

Loss = np.array([ 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14 ])

Iterations = [ 482277173
    , 477629785
    , 433702694
    , 424399900
    , 425888105
    , 428059217
    , 1031846801
    , 1037774429
    , 1024399360
    , 1033585786
    , 1043560696
    , 1042331850
    , 1017113489 ]

# plt.xlabel('Nodes')
# plt.ylabel('Error')
# plt.title('Error versus nodes')
# plt.ylim(1, 16)
# for a, b in zip(Nodes, Loss):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
# plt.bar(Nodes, Loss, width=0.35, align='edge', color='c', alpha=0.8)
# plt.show()
#
#
# plt.xlabel('Nodes')
# plt.ylabel('Crack Time (seconds)')
# plt.title('Crack time (Decryption Time: 1.232 seconds)')
# # plt.plot(Nodes, Times)
# for a, b in zip(Nodes, Times):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
# plt.bar(Nodes, Times, width=0.35, align='edge', color='c', alpha=0.8)
# plt.plot(Nodes, [ 1.232 ] * len(Nodes), 'r', c='g', linewidth=4)
# # plt.ylim(1.232, 30000)
# plt.show()
#
#
# plt.xlabel('Nodes')
# plt.ylabel('Iterations')
# plt.title('Iterations versus different output nodes')
# plt.plot(Nodes, Iterations)
# # for a, b in zip(Nodes, Iterations):
# #     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
# # plt.bar(Nodes, Iterations, width=0.15, align='center', color='c', alpha=0.8)
#
# plt.show()



# plt


[ 'loss', 'hidden neurons', 'learning_rate' ]
fig = plt.figure(num=None, figsize=(26, 12), dpi=80, facecolor='w', edgecolor='k')

fig, ax_lst = plt.subplots(1, 3, figsize=(18, 5))
# for i, str_ in enumerate([ 'loss', 'hidden neurons change', 'learning_rate' ]):
#     ax_lst[ i ].title.set_text(str_)

ax_lst[ 0 ].plot(iteration, loss_log)
ax_lst[ 0 ].set_xlabel('epoches')
ax_lst[ 0 ].set_ylabel('mean squared error')


ax_lst[ 1 ].plot(input_len_list, hidden_num_list)
ax_lst[ 1 ].set_xlabel('number of input neurons (including secret dimensions)')
ax_lst[ 1 ].set_ylabel('min number of hidden neurons')

ax_lst[ 2 ].plot(input_len_list, learning_rate_list)
ax_lst[ 2 ].set_xlabel('input dimensions (including secret dimensions)')
ax_lst[ 2 ].set_ylabel('learning rate')

plt.show()