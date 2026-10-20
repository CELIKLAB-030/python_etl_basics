import pandas as pd
import numpy as np

df = pd.read_csv("unbereinigte_namen.csv", sep=";",
                 on_bad_lines='skip', encoding='utf-8')

df = (
    df.apply(lambda col: col.str.strip().str.title())
      .replace("", pd.NA)
      .dropna()
      .drop_duplicates()
)
print(df.to_markdown(index=False))
