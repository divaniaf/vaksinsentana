import tweepy
import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .forms import userinput
import pandas as pd
import matplotlib.pyplot as plt

# Authentication
consumerKey = "kJgSIMo5SDmVrdvZ1ZQ9VUB1s"
consumerSecret = "1D6cPtxCxk6geQSQAkTdWtUiuLKsLrN5g1X8MmeQOgMWygKFIX"
accessToken = "1628924311-xVKMX2VifBpBV0LdP6pBLGjx4vejla9eqVHpUDF"
accessTokenSecret = "cKFXenpnrYtmTrYEN6rrRZGe2YcYGMjliSfoxmlifEhP8"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Sentiment Analysis

nltk.download('vader_lexicon')

def percentage(part,whole):
    return 100 * float(part)/float(whole) 

keyword = ['vaksin covid']

def primary(input_jumlah):
    T = input_jumlah
    tweets = tweepy.Cursor(api.search, q=keyword).items(T)
    positive  = 0
    negative = 0
    neutral = 0
    polarity = 0
    tweet_list = []
    neutral_list = []
    negative_list = []
    positive_list = []

    for tweet in tweets:
        
        #print(tweet.text)
        tweet_list.append(tweet.text)
        analysis = TextBlob(tweet.text)
        score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        polarity += analysis.sentiment.polarity
        
        if neg > pos:
            negative_list.append(tweet.text)
            negative += 1

        elif pos > neg:
            positive_list.append(tweet.text)
            positive += 1
        
        elif pos == neg:
            neutral_list.append(tweet.text)
            neutral += 1

    positive = percentage(positive, T)
    negative = percentage(negative, T)
    neutral = percentage(neutral, T)
    polarity = percentage(polarity, T)
    positive = format(positive, '.1f')
    negative = format(negative, '.1f')
    neutral = format(neutral, '.1f')

    tweet_list = pd.DataFrame(tweet_list)
    neutral_list = pd.DataFrame(neutral_list)
    negative_list = pd.DataFrame(negative_list)
    positive_list = pd.DataFrame(positive_list)

    labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
    sizes = [positive, neutral, negative]
    colors = ['yellowgreen', 'blue','red']
    patches, texts = plt.pie(sizes,colors=colors, startangle=90)
    plt.style.use('default')
    plt.legend(labels)
    plt.title("Sentiment Analysis Result for keyword = Vaksin" )
    plt.axis('equal')
    plt.savefig('static/media/piechart.png', dpi=100) 