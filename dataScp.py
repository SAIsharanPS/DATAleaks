import praw
import pandas as pd
import re
import os

# Function to authenticate Reddit API
def authenticate_reddit():
    try:
        reddit = praw.Reddit(
            client_id="LgKNwTeYjpU9iralF68opw",       
            client_secret="ENBKhfo7zL7pKf0r5yXVnA0mWmqlzg", 
            user_agent="YOUR_USER_AGENT"     
        )
        print("Reddit API authenticated successfully.")
        return reddit
    except Exception as e:
        print(f"Failed to authenticate Reddit API: {e}")
        return None

# HEre I am using the data for pre processing 
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
   
    text = re.sub(r'[^A-Za-z\s]+', '', text)
    # Convert text to lowercase
    text = text.lower()
    return text

# Scrape data from a subreddit that is wallstreetbets
def scrape_reddit(reddit, subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    print(f"Scraping {limit} posts from subreddit '{subreddit_name}'...")

    try:
        for submission in subreddit.hot(limit=limit):
            post_data = {
                "title": submission.title,
                "selftext": submission.selftext,
                "score": submission.score,
                "comments": submission.num_comments,
                "created_utc": submission.created_utc,
            }
            posts.append(post_data)
        
        if not posts:
            print("No posts found.")
        else:
            print(f"Scraped {len(posts)} posts from subreddit '{subreddit_name}'.")
        return pd.DataFrame(posts)

    except Exception as e:
        print(f"Error while scraping Reddit: {e}")
        return pd.DataFrame()

# Clean and preprocess Reddit data
def preprocess_reddit_data(df):
    # Self text removed
    df['selftext'].fillna('', inplace=True)

    # Repeats are moved
    df['content'] = df['title'] + ' ' + df['selftext']

    # Comnbined stuff is removed
    df['cleaned_content'] = df['content'].apply(clean_text)

    # Removing redundace 
    df.drop(columns=['title', 'selftext'], inplace=True)

    print("Data preprocessing completed.")
    return df

# This the Main Func
def main():
   
    reddit = authenticate_reddit()
    if reddit is None:
        return  

    # Scrape Reddit data
    subreddit_name = 'wallstreetbets' #The Reddit location which was given in the PDF file
    reddit_data = scrape_reddit(reddit, subreddit_name, limit=100)

    # Ensure there is data to process
    if reddit_data.empty:
        print("No data to process.")
        return

    # Preprocess Reddit data
    cleaned_data = preprocess_reddit_data(reddit_data)

    # Create directory if it doesn't exist
    output_dir = r'C:\Users\saich\Desktop\Data'
    os.makedirs(output_dir, exist_ok=True)

    # Save the cleaned data to CSV at the specified location
    file_path = os.path.join(output_dir, 'cleaned_reddit_stock_data.csv')
    try:
        cleaned_data.to_csv(file_path, index=False)
        print(f"Data saved successfully at {file_path}!")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
