import random
import statistics
import pandas as pd


def get_data():
    num = []
    for i in range(1, 1001):
        random.randint(1, 9999)
        num.append(random.randint(1, 9999))
    num.sort()
    return num, statistics.median(num)


if __name__ == "__main__":
    data, med = get_data()
    print(f"The median of the list is {med}")

# convert "num" to a dataframe (pandas)
df = pd.DataFrame(data, columns=['RandomNumbers'])
df.to_csv('data/captured_data.csv', index=False)
print("Data saved to captured_data.csv")
