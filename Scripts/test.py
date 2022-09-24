import pandas as pd
df = pd.read_csv('../files/SampleCSVFile_2kb.csv', encoding="cp1252")
print(df.head(5))
