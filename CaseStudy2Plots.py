
#Python 3.9.10

import sqlite3, csv
import pandas as pd
import matplotlib.pyplot as plt      #Data Visualization package
import seaborn as sns 
import numpy as np

df = pd.read_csv('casestudy.csv')

df = df.dropna()
print(df.dtypes)

median = df['net_revenue'].median()
print(median)

filt_one = (df['net_revenue'] > 125.73) & (df['year'] == 2015)
filt_two = (df['net_revenue'] > 125.73) & (df['year'] == 2016)
filt_three = (df['net_revenue'] > 125.73) & (df['year'] == 2017)

above_median_2015 = df.loc[filt_one]
above_median_2016 = df.loc[filt_two]
above_median_2017 = df.loc[filt_three]

print(above_median_2015)
print(type(above_median_2016))
print(above_median_2017)

num = above_median_2015['year'].count()
num2 = above_median_2016['net_revenue'].count()
num3 = above_median_2017['year'].count()
print(num)
print(num2)
print(num3)
#num1 = above_median_2016['']

filt_four = (df['net_revenue'] < 125.73) & (df['year'] == 2015)
filt_five = (df['net_revenue'] < 125.73) & (df['year'] == 2016)
filt_six = (df['net_revenue'] < 125.73) & (df['year'] == 2017)

below_median_2015 = df.loc[filt_four]
below_median_2016 = df.loc[filt_five]
below_median_2017 = df.loc[filt_six]

num4 = below_median_2015['year'].count()
num5 = below_median_2016['net_revenue'].count()
num6 = below_median_2017['year'].count()
print(num4)
print(num5)
print(num6)

#total_count_less = male_count_less + female_count_less
#data = [['Male', male_count_more], ['Male', male_count_less], ['Female', female_count_less], 
 #       ['Female', female_count_more]]
#new_df = pd.DataFrame(data, columns = ['Male', 'Female'], rows = ['<=50', '>50'])

plt.rcParams['font.size'] = 18

fig_dims = (15,8)


fig, ax = plt.subplots(figsize = fig_dims)

x_values = ['<=125.13', '>125.13']
values_2015 = [num4, num]
values_2016 = [num5, num2]
values_2017 = [num6, num3]

vals_2017 = list(np.add(values_2015, values_2016))

first_rect = ax.bar(x_values, values_2015, 0.4, label ='2015')
second_rect = ax.bar(x_values, values_2016, 0.4, bottom = values_2015, label = '2016')
third_rect = ax.bar(x_values, values_2017, 0.4, bottom = vals_2017, label =  '2017')

 #      label='Women')
ax.set_ylabel('Number of Customers')
ax.set_title('Number of Customers above and below the median income for each year')
ax.legend()

ax.bar_label(first_rect)
ax.bar_label(second_rect)
ax.bar_label(third_rect)

#fig.tight_layout()


#making a histogram
#plt.yticks(fontsize=20)
#plt.xticks(fontsize=20)




fig, ax = plt.subplots(figsize = fig_dims)
print("histogram")
year_filt = (df['year'] == 2015)
new_df = df.loc[year_filt].drop(columns = 'customer_email')

maximum = new_df['net_revenue'].max()
print(maximum)
minimum = new_df['net_revenue'].min()
print(minimum)

new_list = new_df['net_revenue'].tolist()
print(new_list)
print(type(new_list))

bins = [0, 50, 100, 150, 200, 250]

plt.yticks(fontsize=20)
plt.xticks(fontsize=20)

plt.hist(new_list, bins=bins, edgecolor='black', log=True)


#plt.legend()

plt.title('Customers and their range of Revenues')
plt.xlabel('Net Revenue ($)')
plt.ylabel('Total Customers')

plt.tight_layout()



print("hi")


fig, ax = plt.subplots(figsize = fig_dims)
#rcParams.update({'font.size': 22})
new_labels = ['Verified', 'Source Verified', 'Not Verified']

year2_filt = (df['year'] == 2016)
year3_filt = (df['year'] == 2016)


#ax1 = plt.subplot2grid((2, 4), (0, 1))

print("Pie chart")
new_labels = ['2015', '2016', '2017']

#new_df = df.loc[year_filt]
#new_series = pd.Series(new_df)

new_df = df.loc[year_filt]
tot_2015 = new_df.shape[0]
print(tot_2015)
#print(type(df.loc[year_filt]))
new_df = df.loc[year2_filt]
tot_2016 = new_df.shape[0]

new_df = df.loc[year3_filt]
tot_2017 = new_df.shape[0]

info = []
info.append(tot_2015)
info.append(tot_2016)
info.append(tot_2017)
print(tot_2016)
print(tot_2017)


plt.pie(info, labels = new_labels, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

plt.title("Customer Distribution for each Year")
plt.tight_layout()
plt.show()




        








