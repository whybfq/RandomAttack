import time
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

Nodes = np.arange(2, 15)
print(Nodes)

Times = np.array([ 3600.000008, 3604.937237, 3600.000005, 3600.000002, 3600.000017, 3600.000023, 3600.000015,
                    3600.000002, 3600.000009, 3600.000001, 3600.000014, 3600.000144, 3600.003534 ])
Loss = np.array([ 51523.15785, 48379.66171, 43940.4139, 43206.58627, 42798.28442, 37087.79135
                    , 43213.4844, 45231.8186, 41810.41021, 48763.55504, 54683.88731, 60030.53221, 57551.12431 ])
Iterations = np.array([70201467
,3955505
,70224459
,51914791
,51048032
,50517600
,51286417
,50635654
,57538680
,57308891
,57526325
,58385946
,68993737])

# plt.xlabel('Nodes')
# plt.ylabel('Crack Time')
# plt.title('Crack time when computing different output nodes')
# plt.plot(Nodes, Times)
# plt.show()

# plt.xlabel('Nodes')
# plt.ylabel('Minimum mean squared error')
# plt.title('Minimum mean squared error when computing different output nodes')
# plt.plot(Nodes, Loss)
# plt.show()

# plt.xlabel('Nodes')
# plt.ylabel('Iterations')
# plt.title('Iterations when computing different output nodes')
# plt.plot(Nodes, Iterations)
# plt.show()


plt.xlabel('Nodes')
plt.ylabel('Minimum mean squared error')
plt.title('Minimum mean squared error when computing different output nodes')
plt.ylim(32000, 65000)
for a,b in zip(Nodes,Loss):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
plt.bar(Nodes,Loss,width = 0.35,align='center',color = 'c',alpha=0.8)
plt.show()