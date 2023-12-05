import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)

df = pd.read_csv('iris_data.csv')
A = list(df['SepalLengthCm'])
B = list(df['SepalWidthCm'])
C = list(df['PetalLengthCm'])
D = list(df['PetalWidthCm'])

ax1.scatter(A, B, marker='.')
ax2.scatter(A, C, marker='.')
ax3.scatter(A, D, marker='.')
ax4.scatter(B, C, marker='.')
ax5.scatter(B, D, marker='.')
ax6.scatter(C, D, marker='.')

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

plt.show()
