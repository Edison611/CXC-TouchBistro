import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

f = pd.read_csv("bills.csv")
#print(f.head(10))
d = pd.read_csv("venues.csv")
#print(df.head(10))
df = pd.merge(f, d, on="venue_xref_id", how="inner")
df = df[["bill_total_net", "business_date", "country"]]

df['business_date'] = pd.to_datetime(df['business_date'], format='%Y-%m-%d')

def locateSum(startDate,endDate):
    
    y = df.loc[(df["business_date"]>= startDate) & (df["business_date"] <= endDate) & (df["country"] == "US")]
    
    return y["bill_total_net"].sum()



julNet2024 = locateSum('2024-07-01', '2024-07-31') 
augNet2024 = locateSum('2024-08-01', '2024-08-31') 
sepNet2024 = locateSum('2024-09-01', '2024-09-30') 
octNet2024 = locateSum('2024-10-01', '2024-10-31') 
novNet2024 = locateSum('2024-11-01', '2024-11-30') 
decNet2024 = locateSum('2024-12-01', '2024-12-31') 

months = [ "jul2024", "aug2024","sep2024", "oct2024", "nov2024", "dec2024"]

nets = [ julNet2024, augNet2024, sepNet2024, octNet2024, novNet2024, decNet2024]

aves = [ julNet2024/31, augNet2024/31, sepNet2024/30, octNet2024/31, novNet2024/30, decNet2024/31]

plt.bar(months, nets)
plt.title('Bill total net')
plt.xlabel('Months (USA)')
plt.ylabel('Money')
plt.show()

plt.bar(months, aves)
plt.title('Bill total net per day (By month)')
plt.xlabel('Months (USA)')
plt.ylabel('Money/day')
plt.show()
