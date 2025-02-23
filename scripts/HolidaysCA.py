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

def locateSumHoliday(date):
    
    mask = (df["business_date"] == date) & (df["country"] == "CA")
    
    y = df.loc[mask]
    
    return y["bill_total_net"].sum()

canadaDay = locateSumHoliday('2024-07-01')

civicHoliday = locateSumHoliday('2024-08-05')

labourDay = locateSumHoliday('2024-09-02')

thanksgiving = locateSumHoliday('2024-10-14')

remembranceDay= locateSumHoliday('2024-11-11')

christmas= locateSumHoliday('2024-12-25')

boxingDay= locateSumHoliday('2024-12-26')

holidays = ["canadaDay", "civicHoliday", "labourDay", "thanksgiving", "remembranceDay", "christmas", "boxingDay"]

nets =  [canadaDay, civicHoliday, labourDay, thanksgiving, remembranceDay, christmas, boxingDay]

plt.bar(holidays, nets)
plt.title('Bill total net holidays in canada')
plt.xlabel('Holidays')
plt.ylabel('Money')
plt.show()