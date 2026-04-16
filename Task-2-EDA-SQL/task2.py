import pandas as pd
df = pd.read_csv("cleaned_dataset.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df['city'].value_counts())
print(df['gender'].value_counts())

#Bar chart
import matplotlib.pyplot as plt
df.groupby('city')['sales'].sum().plot(kind='bar')
plt.title("Sales by City")
plt.show()

#Pie chart
df['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.show()

#Line chart
df['order_date'] = pd.to_datetime(df['order_date'])
df.groupby('order_date')['sales'].sum().plot()
plt.title("Sales Over Time")
plt.show()

#Advanced
plt.scatter(df['sales'], df['profit'])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()


print(df['sales'].sum())
print(df['profit'].sum())
print(df['sales'].mean())
print(len(df))

