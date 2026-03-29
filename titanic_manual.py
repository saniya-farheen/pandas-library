import pandas as pd

# directly reads from internet!



df.to_csv("titanic.csv", index=False)
print("Downloaded!")
print(df.head())
print(df.info())        
print(df.isnull().sum()) 

with open("titanic.csv", "r") as file:
    frst_line = file.readline()
    print(frst_line)
