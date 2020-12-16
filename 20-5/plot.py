"""
"Cipher:  -84.114265,  59.810097, 104.55785 , 227.77936 , 225.72765 , -98.97675 ,
  -232.89426 , -41.002956, -40.825134, 100.58848 ,-143.09496 , 245.6924  ,
  -115.23982 , -32.235516, -26.236336, 124.21535 ,  12.000608, 267.8395  ,
  -231.79288 ,-180.24928 "
  Plaintext:  "abeZW"

  sending key (W12 and b12):
 -0.6717912 , 1.3653713 , 0.09918854, 0.06713872,-2.4206223 ,
  1.9164733 , 0.4550089 , 1.6818423 ,-1.2356025 , 0.34466356,
  0.7713794 , 0.8146725 ,-0.35070297, 1.741917  ,-0.91374665,
  1.0820915 ,-0.34832582, 0.2080725 ,-1.1836312 ,-0.5201203 ,
 -0.5745343 , 1.0374976 , 1.8578953 , 1.2648255 , 1.1491303 ,
  0.59593356, 0.53720635, 1.3577791 , 0.38733402, 0.89778864,
 -1.7120047 ,-0.54062206, 1.4280549 ,-0.5318543 , 1.2636068 ,
  0.98461294, 0.9025531 ,-0.8630909 ,-0.84963965,-1.4899219 ,
  0.61473   ,-0.5658123 , 0.27871093,-0.11628205,-1.0147816 ,
  0.89648366,-0.0477333 , 0.7714332 , 0.96284527,-1.2355624 ,
 -0.15945973, 1.5301523 ,-0.05575457,-0.14233145, 1.6607068 ,
  2.0599258 , 1.6917266 , 0.6081293 ,-1.3465043 , 0.40484473,
  1.3057375 ,-0.1778804 ,-0.4316187 , 0.67624503,-1.274494  ,
 -0.26314333,-0.4186242 ,-1.2165604 , 0.27638587, 0.48672372,
 -0.63527536, 0.23406363, 0.13656823,-0.85191417, 0.1834343 ,
  0.14212808,-1.0100871 ,-0.18957828, 0.7659493 ,-0.4695784 ,
 -1.6872578 ,-1.7206402 , 0.06692824, 1.2838625 , 1.0067936 ,
 -0.8955588 ,-1.286141  ,-0.64873844, 2.200079  ,-0.07652581,
 -2.6636767 ,-0.8521463 ,-0.36870039,-0.7622433 , 0.72801656,
-0.3162513 , 0.6057236 ,-0.6900968 ,-0.5934992 ,-0.23945104
  """



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


pictures = [ 'Error versus nodes', 'Crack time (Decryption Time: 1.445 seconds)',
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
ax_lst[ 0 ].bar(Nodes, Loss, width=0.35, align='center', color='c', alpha=0.8)

ax_lst[ 1 ].plot(Nodes, Times)
ax_lst[ 1 ].set_xlabel('Nodes')
ax_lst[ 1 ].set_ylabel('Time (seconds)')
for a, b in zip(Nodes, Times):
    ax_lst[ 1 ].text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
ax_lst[ 1 ].bar(Nodes, Times, width=0.35, align='center', color='g', alpha=0.8)
ax_lst[ 1 ].plot(Nodes, [ 1.445 ] * len(Nodes), 'r', c='r', linewidth=4)
# plt.ylim(1.232, 30000)

ax_lst[ 2 ].plot(Nodes, Iterations)
ax_lst[ 2 ].set_xlabel('Nodes')
ax_lst[ 2 ].set_ylabel('Iterations')

# for a, b in zip(Nodes, Iterations):
#     ax_lst[ 2 ].text(a, b + 0.5, '%.1f' % b, ha='right', va='bottom', fontsize=7)
# ax_lst[ 2 ].bar(Nodes, Iterations, width=0.15, align='center', color='c', alpha=0.8)
ax_lst[ 2 ].plot(Nodes, Iterations)
plt.show()
