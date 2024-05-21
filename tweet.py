import datetime
import os
import random
from dotenv import load_dotenv
import requests
from word_list import load_words, save_words  # import the functions

# Load environment variables from .env file
dotenv_path = 'variables.env'
load_dotenv(dotenv_path)

# Twitter API v2 Bearer Token
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token_key = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')


# Twitter API v2 endpoint URL
url = 'https://api.twitter.com/2/tweets'

# Define the tweet content


def get_tweet(words):
    word_of_the_day = random.choice(words)
    tweet = f"I like {word_of_the_day}."
    return tweet, word_of_the_day


# Load words from file (only once)
words_file = 'word_list.txt'
words = load_words(words_file)

# Generate the tweet
tweet, word_of_the_day = get_tweet(words)

# Twitter API v2 HTTP headers with bearer token
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

# Make request to Twitter API to post the tweet
data = {'status': tweet}
response = requests.post(url, json=data, headers=headers)

# Print response
if response.status_code == 200:
    print("Tweeted successfully:", response.json())
    # Remove the used word and save the updated list
    words.remove(word_of_the_day)
    save_words(words_file, words)
else:
    print("Failed to tweet. Status code:", response.status_code)
