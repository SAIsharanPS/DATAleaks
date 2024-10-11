import pandas as pd
import matplotlib.pyplot as plt

# Load the processed sentiment analysis data
sentiment_data = pd.read_csv('processed_stock_data.csv')  # Adjust the path if necessary

# Count the sentiment values
sentiment_counts = sentiment_data['sentiment'].value_counts()

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
