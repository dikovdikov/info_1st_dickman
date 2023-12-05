import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

df = pd.read_csv('iris_data.csv')

setosa = 0
virginica = 0
versicolor = 0
for flower in df['Species']:
    if flower == 'Iris-setosa':
        setosa += 1
    elif flower == 'Iris-virginica':
        virginica += 1
    else:
        versicolor += 1
total1 = setosa + virginica + versicolor
setosa_part = setosa / total1
virginica_part = virginica / total1
versicolor_part = versicolor / total1

ax1.pie([virginica_part, versicolor_part, setosa_part], labels=['Iris-virginica', 'Iris-versicolor', 'Iris-setosa'])
#ax1.title('The share of iris species in the dataset', fontdict={'fontname': 'sans-serif', 'fontsize': 20})


short = 0
middle = 0
long = 0
for lenght in df['PetalLengthCm']:
    if float(lenght) < 1.2:
        short += 1
    elif float(lenght) >= 1.2 and float(lenght) < 1.5:
        middle += 1
    else:
        long += 1
total2 = short + middle + long
short_part = short / total2
middle_part = middle / total2
long_part = long / total2

ax2.pie([short_part, middle_part, long_part], labels=['short', 'middle', 'long'])
#ax2.title('The length of the iris petals in the dataset', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

print(setosa_part, setosa_part, versicolor_part)
print(short_part, middle_part, long_part)
plt.show()
