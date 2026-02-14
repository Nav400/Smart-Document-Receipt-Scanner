import pandas as pd

data = {'item': ['Coffee', 'Lunch'], 'amount': [5.50, 12.00]}
df = pd.DataFrame(data)

print(df)

df.to_csv('expenses.csv', index = False)


#Create some sample data (2 expenses)
#Turn it into a pandas table
#Print it to see what it looks like
#Save it as a CSV file