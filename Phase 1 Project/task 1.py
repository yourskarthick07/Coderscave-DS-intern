import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = (r'C:\Users\knsma\Downloads\Data\Transaction data.csv')
df = pd.read_csv(file_path)


print("Overview Statistics:")
print(df.describe())


plt.figure(figsize=(10, 6))
sns.histplot(df['BILL_AMT'], bins=30, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Transaction Amount (BILL_AMT)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='MONTH', y='BILL_AMT', data=df.groupby('MONTH')['BILL_AMT'].sum().reset_index())
plt.title('Monthly Trend of Total Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

top_products_by_quantity = df.groupby('GRP')['QTY'].sum().sort_values(ascending=False).head(10)
top_products_by_value = df.groupby('GRP')['VALUE'].sum().sort_values(ascending=False).head(10)


customer_segments = pd.cut(df['BILL_AMT'], bins=[0, 100, 500, 1000, float('inf')],
                           labels=['Low Value', 'Medium Value', 'High Value', 'Very High Value'])
df['Customer Segment'] = customer_segments

plt.figure(figsize=(10, 6))
sns.barplot(x='BRD', y='VALUE', data=df.groupby('BRD')['VALUE'].sum().reset_index().sort_values(by='VALUE', ascending=False).head(10))
plt.title('Top 10 Brands by Total Sales')
plt.xlabel('Brand')
plt.ylabel('Total Sales')
plt.show()

numeric_columns = ['BILL_AMT', 'QTY', 'VALUE', 'PRICE']  # Update with your numeric columns
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')                                                     
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
