import numpy as np
import pandas as pd
b=np.random.randint(50,100,size=10)
d={"name":["shreya","anushka","priyanka","sneha","riya","komal","sonali","megha","neha","pooja"],"maths":b,"science":b,"emglish":b}
df=pd.DataFrame(d)
print(df)

print(d["maths"].mean())
print(d["science"].mean())
print(d["emglish"].mean())

d["total"]=d["maths"]+d["science"]+d["emglish"]
df=pd.DataFrame(d)
print(df)

print(df.loc[df["total"].idxmax(),"name"])
df["result"]=(df["total"]>= 150).map({True:"pass",False:"fail"})
sort =df.sort_values(by="total",ascending=False)
print(sort)