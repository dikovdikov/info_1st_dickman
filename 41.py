import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(16,9))
ax1 = fig.add_subplot(111)
w_m = [177.7, 141.4, 114.6, 74.1, 58.0][::-1]
M_m = [403, 314, 253, 166, 136][::-1]
print(w_m, M_m)
M = [130, 410]
w = np.interp(M, M_m, w_m)
ax1.scatter(M_m, w_m, marker='x')
ax1.errorbar(M_m, w_m, yerr=0.2, xerr=0.1, color='k', linestyle='None')
ax1.plot(M, w, 'r')


plt.xlabel('Ω, рад/с * 10**-3')
plt.ylabel('M, мн * м')
plt.title('Зависимость Ω от M', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.grid()
plt.show()




