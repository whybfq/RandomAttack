import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

Nodes = np.arange(2, 15)  # 13 nodes
# print(Nodes)

Times = np.array([ 3600.000008, 3604.937237, 3600.000005, 3600.000002, 3600.000017, 3600.000023, 3600.000015,
                   3600.000002, 3600.000009, 3600.000001, 3600.000014, 3600.000144, 3600.003534 ])

Loss = np.array([ 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14 ])

Iterations = [482277173
,477629785
,433702694
,424399900
,425888105
,428059217
,1031846801
,1037774429
,1024399360
,1033585786
,1043560696
,1042331850
,1017113489]

plt.xlabel('Nodes')
plt.ylabel('Error')
plt.title('Error when computing different output nodes')
plt.ylim(1, 16)
for a, b in zip(Nodes, Loss):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
plt.bar(Nodes, Loss, width=0.35, align='center', color='c', alpha=0.8)
plt.show()
