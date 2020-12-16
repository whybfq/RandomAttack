import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

Nodes = np.arange(2, 6)  # 13 nodes
# print(Nodes)

Times = np.array([ 28800.00258
                     , 28800.00004
                     , 28800.00006
                     , 28800.00002 ])

Loss = np.array([ 5, 5, 5, 5 ])

Iterations = [ 297726029
    , 298343583
    , 297264181
    , 298193927 ]

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


pictures = [ 'Error versus nodes', 'Crack time (Decryption Time: 1.232 seconds)',
             'Iterations versus nodes' ]
fig = plt.figure(num=None, figsize=(26, 12), dpi=80, facecolor='w', edgecolor='k')

fig, ax_lst = plt.subplots(1, 3, figsize=(18, 5))
for i, str_ in enumerate(pictures):
    ax_lst[ i ].title.set_text(str_)

ax_lst[ 0 ].plot(Nodes, Loss)
ax_lst[ 0 ].set_xlabel('nodes')
ax_lst[ 0 ].set_ylabel('Error')
# ax_lst[ 0 ].title('Error versus nodes')
# plt.ylim(0, 16)
for a, b in zip(Nodes, Loss):
    ax_lst[ 0 ].text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
ax_lst[ 0 ].bar(Nodes, Loss, width=0.35, align='edge', color='c', alpha=0.8)

ax_lst[ 1 ].plot(Nodes, Times)
ax_lst[ 1 ].set_xlabel('Nodes')
ax_lst[ 1 ].set_ylabel('Time (seconds)')
for a, b in zip(Nodes, Times):
    ax_lst[ 1 ].text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
ax_lst[ 1 ].bar(Nodes, Times, width=0.35, align='edge', color='c', alpha=0.8)
ax_lst[ 1 ].plot(Nodes, [ 1.232 ] * len(Nodes), 'r', c='g', linewidth=4)
# plt.ylim(1.232, 30000)

ax_lst[ 2 ].plot(Nodes, Iterations)
ax_lst[ 2 ].set_xlabel('Nodes')
ax_lst[ 2 ].set_ylabel('Iterations')

# for a, b in zip(Nodes, Iterations):
#     ax_lst[ 2 ].text(a, b + 0.5, '%.1f' % b, ha='right', va='bottom', fontsize=7)
# ax_lst[ 2 ].bar(Nodes, Iterations, width=0.15, align='center', color='c', alpha=0.8)
ax_lst[ 2 ].plot(Nodes, Iterations)
plt.show()
