import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the processed data
processed_data_path = 'processed_stock_data.csv'
df = pd.read_csv(processed_data_path)

#Count sentiment occurrences
sentiment_counts = df['sentiment'].value_counts()

#Visualize Sedimentation 
plt.figure(figsize=(10, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Counting
stock_mentions_count = df['stock_mentions'].sum()

#Print the stocks
print(f'Total stock mentions in discussions: {stock_mentions_count}')

# Just saving the data for faster Access
sentiment_counts.to_csv(r'C:\Users\saich\Desktop\Data\sentiment_counts.csv')

