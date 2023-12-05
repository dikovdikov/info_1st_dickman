import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('BTC_data.csv')
a = list(df['close'])
t = list(df['time'])
for i in range(len(t)):
    t[i] = t[i][:10]

x = [i for i in range(len(a))]
z = np.polyfit(x, a, 20)
p = np.poly1d(z)
apr = [p(i) for i in x]

plt.figure(figsize=(8,5), dpi=100)

plt.plot(t, a)
plt.plot(t, apr)
plt.title('исторический график зависимости цены биткоина от времени 2018-2023 гг')
plt.legend()

plt.xlabel('время')
plt.ylabel('цена')

plt.show()
