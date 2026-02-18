import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('captured_data.csv')

plt.figure(figsize=(10, 6))
plt.hist(df['RandomNumbers'])
plt.title('Distribution of Random Numbers')
plt.xlabel('Random Numbers')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.show()
