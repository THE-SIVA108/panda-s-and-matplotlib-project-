import pandas as pd

d1 = [[11, 22], [33, 44]]
d2 = [[55, 66], [77, 88]]

c1 = ["A", "B"]
c2 = ["X", "Y"]

df1 = pd.DataFrame(d1, columns = c1)
df2 = pd.DataFrame(d2, columns = c2)

a = [df1, df2]
b = pd.concat(a, axis = 1)

print(b)