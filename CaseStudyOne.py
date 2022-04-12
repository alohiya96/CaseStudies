import pandas as pd                   #Data analysis package
import matplotlib.pyplot as plt      #Data Visualization package
import seaborn as sns 

df = pd.read_csv('loans_full_schema.csv')

fig_dims = (15, 8)  #setting the size of the figure created
fig, axs = plt.subplots(nrows = 2, ncols=4, figsize = fig_dims)  #creating nine subplots in the figure
sns.set_style('whitegrid')

annual_income_Series = pd.Series(df['annual_income'], name = 'annual_income') 
debt_to_income_Series = pd.Series(df['debt_to_income'], name = 'debt_to_income')
dat = pd.merge(annual_income_Series, debt_to_income_Series, right_index = True, left_index = True) 

loan_amount_Series = pd.Series(df['loan_amount'], name = 'loan_amount')
loan_data = pd.merge(annual_income_Series, loan_amount_Series, right_index = True, left_index = True)

loan_amount_Series = pd.Series(df['loan_amount'], name = 'loan_amount')

loan_amount_Series = pd.Series(df['loan_amount'], name = 'loan_amount')

loan_amount_Series = pd.Series(df['loan_amount'], name = 'loan_amount')

home_ownerships_series =  pd.Series(df['homeownership'], name = 'home_ownerships').to_list()
#print(home_ownerships_series)

emp_length_series = pd.Series(df['emp_length'], name = 'emp_length')
new_data = pd.merge(annual_income_Series, emp_length_series, right_index = True, left_index = True)

interest_rate_series = pd.Series(df['interest_rate'], name = 'interest_rate')
ir_la_corr = pd.merge(loan_amount_Series, interest_rate_series, right_index = True, left_index = True)


sns.regplot(x = 'annual_income', y = 'debt_to_income', data = dat, ax = axs[1][0], line_kws={"color": "red"}, scatter_kws={"color": "black"})
sns.regplot(x = 'annual_income', y = 'loan_amount', data = loan_data, ax = axs[1][1], line_kws={"color": "red"}, scatter_kws={"color": "black"})

sns.regplot(x = 'annual_income', y = 'emp_length', data = new_data, ax = axs[0][2], line_kws={"color": "red"}, scatter_kws={"color": "black"})
sns.regplot(x = 'loan_amount', y = 'interest_rate', data = ir_la_corr, ax = axs[0][3], line_kws={"color": "red"}, scatter_kws={"color": "black"})

total_samples = df['homeownership'].count().item()
print(total_samples)
print(type(total_samples))
own_count = df.homeownership.value_counts().OWN
print(own_count)

rent_count = df.homeownership.value_counts().RENT
mortgage_count = df.homeownership.value_counts().MORTGAGE

slices = []

own_percentages = (own_count/total_samples) * 100
slices.append(own_percentages)

rent_percentages = (rent_count/total_samples) * 100
slices.append(rent_percentages)

mortage_percentages = (mortgage_count/total_samples) * 100
slices.append(mortage_percentages)
#print(home_count)

#new_fig_dims = (15, 8)  #setting the size of the figure created
#fig, axs = plt.subplots(nrows = 5, ncols=4, figsize = new_fig_dims)  #creating nine subplots in the figure
sns.set_style('whitegrid')

#slices = [59219, 55466, 47544, 36443, 35917]
labels = ['Mortgage', 'Rent', 'Own']
#explode = [0, 0, 0, 0.1, 0]
ax1 = plt.subplot2grid((2,4),(0,0))
plt.pie(slices, labels=labels, shadow=True,
        startangle=90, autopct='%1.1f%%', 
        wedgeprops={'edgecolor': 'black'})

plt.title("Homeownerships Allocation Distribution Pie Chart")
plt.tight_layout()


total_vi_samples = df['verified_income'].count().item()
vi_slices = df['verified_income'].value_counts().tolist()
print(vi_slices)
print(type(vi_slices))



#verified_count = df.verified_income.value_counts().Verified
#notverified_count = df.verified_income.value_counts().NotVerified
#sourceverified_count = df.verified_income.value_counts().SourceVerified

new_slices = []
verified_perc = (vi_slices[0]/total_vi_samples) * 100
new_slices.append(vi_slices[0])

notverified_perc = (vi_slices[1]/total_vi_samples) * 100
new_slices.append(vi_slices[1])

sourceverified_perc = (vi_slices[2]/total_vi_samples) * 100 
new_slices.append(vi_slices[2])

new_labels = ['Verified', 'Source Verified', 'Not Verified']

ax1 = plt.subplot2grid((2, 4), (0, 1))

plt.pie(new_slices, labels=new_labels, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

plt.title("Income Verification Distribution Pie Chart")
plt.tight_layout()

#
plt.show()





#Create a stacked bar chart
plt.show()

#sns.regplot(x = 'Center_Rebounds_per_Game', y = 'Center_FP_Per_Game', data = Center_Data, ax= axs[0][1], line_kws={"color": "red"}, scatter_kws={"color": "black"})



