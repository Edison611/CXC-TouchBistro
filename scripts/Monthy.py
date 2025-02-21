import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("bills.csv", usecols=["business_date", "bill_total_net"])


df['business_date'] = pd.to_datetime(df['business_date'], format='%Y-%m-%d')

def locateSum(startDate,endDate):
    
    y = df.loc[(df["business_date"]>= startDate) & (df["business_date"] <= endDate)]
    
    return y["bill_total_net"].sum()


janNet2024 = locateSum('2024-01-01', '2024-01-31') 
febNet2024 = locateSum('2024-02-01', '2024-02-28') 
marNet2024 = locateSum('2024-03-01', '2024-03-31') 
aprNet2024 = locateSum('2024-04-01', '2024-04-30') 
mayNet2024 = locateSum('2024-05-01', '2024-05-31') 
junNet2024 = locateSum('2024-06-01', '2024-06-30') 
julNet2024 = locateSum('2024-07-01', '2024-07-31') 
augNet2024 = locateSum('2024-08-01', '2024-08-30') 
sepNet2024 = locateSum('2024-09-01', '2024-09-30') 
octNet2024 = locateSum('2024-10-01', '2024-10-31') 
novNet2024 = locateSum('2024-11-01', '2024-11-29') 
decNet2024 = locateSum('2024-12-01', '2024-12-31') 
janNet2025 = locateSum('2025-01-01', '2025-01-31') 

months = ["jan2024", "feb2024", "mar2024", "apr2024", "may2024", "jun2024", "jul2024", "aug2024","sep2024", "oct2024", "nov2024", "dec2024", "jan2025"]

nets = [janNet2024, febNet2024, marNet2024, aprNet2024, mayNet2024, junNet2024, julNet2024, augNet2024, sepNet2024, octNet2024, novNet2024, decNet2024,janNet2025]

plt.bar(months, nets)
plt.title('Bill total net')
plt.xlabel('Months')
plt.ylabel('Money')
plt.show()