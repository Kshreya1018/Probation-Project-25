import pandas as pd
arr= {
    "Name": ["Adi", "Bobby", "Candy", "Dior", "Ena"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 75, 95, 88]
}

d= pd.DataFrame(arr)
print(d)

print("First 3 rows:",d.head(10))

print("name column:",d["Name"])

b=d["Marks"] > 85
print(d[b])

d["Grade"] = ["A+", "A", "C", "A+", "A"] 
print(d)

c = d.drop(columns=["Age"])
print(c)