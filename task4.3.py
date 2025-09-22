import numpy as np
import pandas as pd
b=np.random.randint(1,100,size=10)
d={"name":["shreya","anushka","priyanka","sneha","riya","komal","sonali","megha","neha","pooja"],"maths":b,"science":b,"emglish":b}
df=pd.DataFrame(d)
print(df)

