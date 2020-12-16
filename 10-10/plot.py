"""
 Cipher: 392.24274, 287.17422,-304.2557 , 408.5121 , 149.03389, 306.06216,
   438.894  , 320.20078,  81.52688,-189.753
  Plaintext:  Thank you!

  sending key (W12 and b12):
 -0.5778161 ,-0.4639722 ,-1.0786507 ,-1.4716448 , 0.98838025,-0.07179666,
   0.79552335,-0.7371018 , 0.817246  , 0.45553315,
 -0.6709652 , 1.3361937 , 0.85715365, 0.7534529 , 0.03531647,-0.28524458,
  -0.53712547, 1.4220123 , 1.7516    ,-0.26768434,
  0.97250223,-0.33839196, 0.14660859, 0.34759668,-0.580761  ,-2.7897875 ,
   1.1213564 , 0.96995735,-1.7923326 ,-0.5971647 ,
  0.17832927, 0.44507983, 0.75343204, 1.1357803 ,-1.2620833 ,-1.1662494 ,
   0.6246986 , 0.6251265 ,-0.94801456, 0.9445155 ,
 -0.7496377 , 0.49857447, 0.02192044, 0.75683767, 0.39000455, 0.4217171 ,
  -1.2665563 ,-0.75882936,-1.0339766 ,-0.19273113,
  0.57958484, 0.01962007,-0.6499376 ,-0.41952753,-0.924574  , 0.62544656,
  -0.02337085, 0.05670946, 1.3962209 ,-1.0284512 ,
  0.64642596,-0.72159827,-0.63400525,-0.00940208, 1.0346452 ,-0.04868554,
  -0.9810022 ,-1.0924125 ,-0.95146847, 0.4613736 ,
  0.8029795 ,-0.3967331 , 1.6757597 ,-0.1237518 , 0.36719054, 0.65732145,
   0.94679034, 1.3317208 ,-1.000711  ,-1.4484543 ,
 -1.0708165 , 0.7237722 ,-0.98334557, 0.7508227 ,-1.867056  ,-0.00876967,
   1.4409624 , 0.3202457 ,-0.11467054, 0.55942994,
  0.8005079 ,-0.15210709, 0.19815147,-0.67873275, 0.14353713,-0.15090317,
   0.52900827, 2.1554601 ,-1.1827815 ,-1.7813509 ,
 0.841712  ,-1.4921778 , 0.10070884, 0.4297665 , 0.25087777, 0.34722206,
  2.1539927 ,-0.12884271, 0.88757074, 0.59193385
  """

import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

Nodes = np.arange(2, 11)  # 13 nodes
# print(Nodes)

Times = np.array([ 28800.00005
                     , 28800.00005
                     , 28800.00003
                     , 28800.00003
                     , 28800.00004
                     , 28800.00004
                     , 28800.00003
                     , 28800
                     , 28800.00003 ])

Loss = np.array([ 10, 10, 10, 10, 10, 10, 10, 10, 10 ])

Iterations = [ 253034181
    , 258533020
    , 255968734
    , 257723551
    , 255903827
    , 256721461
    , 257344955
    , 256775966
    , 255968734 ]

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


pictures = [ 'Error versus nodes', 'Crack time (Decryption Time: 0.96 seconds)',
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
ax_lst[ 1 ].plot(Nodes, [ 0.96 ] ˚* len(Nodes), 'r', c='r', linewidth=4)
# plt.ylim(1.232, 30000)

ax_lst[ 2 ].plot(Nodes, Iterations)
ax_lst[ 2 ].set_xlabel('Nodes')
ax_lst[ 2 ].set_ylabel('Iterations')

# for a, b in zip(Nodes, Iterations):
#     ax_lst[ 2 ].text(a, b + 0.5, '%.1f' % b, ha='right', va='bottom', fontsize=7)
# ax_lst[ 2 ].bar(Nodes, Iterations, width=0.15, align='center', color='c', alpha=0.8)
ax_lst[ 2 ].plot(Nodes, Iterations)
plt.show()
