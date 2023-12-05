import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('BTC_data.csv')
a = list(df['close'])
t = list(df['time'])
for i in range(len(t)):
    t[i] = t[i][:10]
plt.figure(figsize=(8,5), dpi=100)

plt.plot(t, a)

plt.title('исторический график зависимости цены биткоина от времени 2018-2023 гг')
plt.legend()

plt.xlabel('время')
plt.ylabel('цена')

plt.show()

