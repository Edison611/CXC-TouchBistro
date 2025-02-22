import pandas as pd
import numpy as np

f = pd.read_csv("CxCData/bills.csv")
#print(f.head(10))
df = pd.read_csv("CxCData/venues.csv")
#print(df.head(10))
combine = pd.merge(f, df, on="venue_xref_id", how="inner")
combine.to_csv("output.csv", index=False)
print(combine)
combine = combine[["bill_paid_at_local", "concept", "bill_total_billed"]]
