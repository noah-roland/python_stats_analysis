import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/captured_data.csv')

median_value = df['RandomNumbers'].median()

plt.figure(figsize=(10, 6))
plt.hist(df['RandomNumbers'])
plt.title('Distribution of Random Numbers')
plt.xlabel('Random Numbers')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.axvline(median_value, color='red', linestyle='dashed',
            linewidth=1, label=f'Median: {median_value}')
plt.legend()
plt.show()
