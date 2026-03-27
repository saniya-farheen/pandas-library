import pandas as pd

# directly reads from internet!
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# save to your computer
df.to_csv("titanic.csv", index=False)
print("Downloaded!")
print(df.head())
