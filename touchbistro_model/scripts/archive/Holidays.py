import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("bills.csv", usecols=["business_date", "bill_total_net"])


df['business_date'] = pd.to_datetime(df['business_date'], format='%Y-%m-%d')

def locateSumHoliday(date):
    
    y = df.loc[df["business_date"] == date]
    
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
plt.title('Bill total net')
plt.xlabel('Holidays')
plt.ylabel('Money')
plt.show()