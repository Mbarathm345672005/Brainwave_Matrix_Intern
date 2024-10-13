import praw
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

# Set up Reddit client
reddit = praw.Reddit(
    client_id="d_0fVGvvYr2usb81o94izg",      # Replace with your client ID
    client_secret="H8CfRE6O58t6YJP0IZrATYd0D0xkGQ",  # Replace with your client secret
    user_agent="benzapp"        # Name of your app
)

# Define the subreddit and topic for analysis
subreddit_name = "technology"  # Change this to the subreddit you're interested in
topic = "AI"  # Change this to the topic you want to analyze
subreddit = reddit.subreddit(subreddit_name)

# Fetch posts related to the topic
posts = subreddit.search(topic, limit=100)  # Adjust limit as needed

# Collect sentiment scores and timestamps
titles = []
sentiment_scores = []
post_times = []

for post in posts:
    titles.append(post.title)
    analysis = TextBlob(post.title)
    sentiment_score = analysis.sentiment.polarity
    sentiment_scores.append(sentiment_score)
    post_times.append(post.created_utc)  # Capture the post timestamp

# Convert timestamps to a readable format (optional)
import datetime
post_dates = [datetime.datetime.fromtimestamp(time) for time in post_times]

# Visualization 1: Bar Chart of Sentiment Scores
plt.figure(figsize=(12, 6))
plt.bar(range(len(sentiment_scores)), sentiment_scores, color='blue')
plt.xlabel('Post Index')
plt.ylabel('Sentiment Score')
plt.title(f'Sentiment Analysis of Reddit Posts about "{topic}" in r/{subreddit_name}')
plt.show()

# Visualization 2: Sentiment Trend Over Time (Line Plot)
plt.figure(figsize=(12, 6))
plt.plot(post_dates, sentiment_scores, marker='o', linestyle='-', color='green')
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title(f'Sentiment Trend of "{topic}" in r/{subreddit_name}')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
