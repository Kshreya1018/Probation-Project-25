import pandas as pd

df = pd.read_csv(r"C:\Users\shrey\OneDrive\Desktop\DataClean.csv")
print(df.head(20))

df.columns = df.columns.str.lower()
df['status'] = df['status'].str.lower()
df['ai risk'] = df['ai risk'].str.lower()
df['education'] = df['education'].str.lower()
df['industry'] = df['industry'].str.lower()
df['location'] = df['location'].str.lower()
df['age group'] = df['age group'].str.replace('_', '-')
df["date recorded"] = pd.to_datetime(df["date recorded"], errors='coerce')
df = df.drop_duplicates()
print(df.head(20))

df.to_csv(r"C:\Users\shrey\OneDrive\Desktop\DataClean.csv", index=False)