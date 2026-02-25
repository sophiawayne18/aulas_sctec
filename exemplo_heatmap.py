import seaborn as sns
import matplotlib.pyplot as plt

voos = sns.load_dataset("flights")

voos = voos.pivot(index='month', columns='year', values='passengers')

plt.figure(figsize=(10,6))

sns.heatmap(voos, annot=True, fmt='.0F')

plt.show()