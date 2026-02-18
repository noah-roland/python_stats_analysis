import pandas as pd
import matplotlib.pyplot as plt

input_file = input(
    "Enter the path to the CSV file (e.g., 'data/captured_data.csv'): ")
target_col = input(
    "Enter the name of the column to analyze (e.g., 'RandomNumbers'): ")
df = pd.read_csv(input_file)

median_value = df[target_col].median()

plt.figure(figsize=(10, 6))
plt.hist(df[target_col])
plt.title(f'Distribution of {target_col}')
plt.xlabel(target_col)
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.axvline(median_value, color='red', linestyle='dashed',
            linewidth=1, label=f'Median: {median_value}')
plt.legend()
plt.show()
