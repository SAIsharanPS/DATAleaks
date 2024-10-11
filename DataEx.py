import pandas as pd
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

file_path = 'cleaned_reddit_stock_data.csv'
df = pd.read_csv(file_path)


def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z\s]+', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return text

# Clean the 'content' column
df['cleaned_content'] = df['content'].apply(clean_text)

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'positive'
    elif sentiment['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Analyze sentiment
df['sentiment'] = df['cleaned_content'].apply(analyze_sentiment)

# Function to count stock mentions
def count_stock_mentions(text):
    return text.count('$') 

#metions
df['stock_mentions'] = df['cleaned_content'].apply(count_stock_mentions)

#saving the data
output_path = r'C:\Users\saich\Desktop\Data\processed_stock_data.csv'
df.to_csv(output_path, index=False)
print(f"Processed data saved at: {output_path}")
