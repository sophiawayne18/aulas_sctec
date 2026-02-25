import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

survived_counts = df['survived'].value_counts()

print(survived_counts)

plt.figure(figsize=(8,6))

plt.bar(survived_counts.index, survived_counts, color= 'orange')

plt.title('Contagem de Sobreviventes')
plt.xlabel('Survived (0 / 1)')
plt.ylabel('Contagem')

plt.show()