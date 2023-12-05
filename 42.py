import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(20,20))
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)
x = [i for i in range(50)]
y = [j for j in range(50)]
S = [i + j for i in x for j in y]
print(S)
ax1.hist(S, 20)
ax2.hist(S, 50)
ax3.hist(S, 75)
ax4.hist(S, 100)
ax5.hist(S, 200)
ax6.hist(S, 300)

plt.show()

