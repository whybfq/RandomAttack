import time
import numpy as np
from numpy import random
import matplotlib as plt

Nodes = np.arange(2, 15)
print(Nodes)

Times = np.array([ ])
Loss = np.array([ 51523.15785, 48379.66171, 43940.4139, 43206.58627, 42798.28442, 37087.79135
                    , 43213.4844, 45231.8186, 41810.41021, 48763.55504, 54683.88731, 60030.53221, 57551.12431 ])

plt.plot(Nodes, Loss)