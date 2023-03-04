import pandas as pd

# Load the order history CSV file
order_history = pd.read_csv('order_history.csv')

# Convert the 'Item Total' column to a numeric data type
order_history['Item Total'] = pd.to_numeric(order_history['Item Total'].str.replace('$', ''))

# Calculate the total amount spent on Amazon
total_spent = order_history['Item Total'].sum()

# Determine the most frequently used card
most_used_card = order_history['Payment Instrument Type'].value_counts().index[0]

# Determine the month and year of each order
order_history['Order Date'] = pd.to_datetime(order_history['Order Date'])
order_history['Month'] = order_history['Order Date'].dt.month
order_history['Year'] = order_history['Order Date'].dt.year

# Map month numbers to month names
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
order_history['Month Name'] = order_history['Month'].apply(lambda x: month_names[x-1])

# Determine the month with the highest spending
total_spent_by_month = order_history.groupby(['Year', 'Month', 'Month Name'])['Item Total'].sum()
year, month, month_name = total_spent_by_month.idxmax()

# Determine the most frequent ordering customer email
most_frequent_email = order_history['Ordering Customer Email'].value_counts().index[0]

# Determine the most frequent category
most_frequent_category = order_history['Category'].value_counts().index[0]

print(f'Total amount spent on Amazon: ${total_spent:.2f}')
print(f'Most frequently used card: {most_used_card}')
print(f'Highest spending month: {month_name} {year}')
print(f'Most frequent ordering customer email: {most_frequent_email}')
print(f'Most frequent category: {most_frequent_category}')
