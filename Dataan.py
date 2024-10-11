import pandas as pd
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk


nltk.download('vader_lexicon')


file_path = 'processed_stock_data.csv'  
df = pd.read_csv(file_path)

# Function to clean text
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z\s]+', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return text


df['cleaned_content'] = df['content'].apply(clean_text)


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
    return text.count('$')  # Count occurrences of '$'

# Count stock mentions
df['stock_mentions'] = df['cleaned_content'].apply(count_stock_mentions)

# Save the processed data to a new CSV file
output_path = r'C:\Users\saich\Desktop\Data\processed_stock_data.csv'
df.to_csv(output_path, index=False)
print(f"Processed data saved at: {output_path}")
