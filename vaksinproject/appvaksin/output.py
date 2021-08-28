import pandas as pd
from .sentiment import primary

def output():
    tweet_list = pd.DataFrame(primary.tweet_list)
    neutral_list = pd.DataFrame(primary.neutral_list)
    negative_list = pd.DataFrame(primary.negative_list)
    positive_list = pd.DataFrame(primary.positive_list)
    print("total number: ",len(tweet_list))
    print("positive number: ",len(positive_list))
    print("negative number: ", len(negative_list))
    print("neutral number: ",len(neutral_list))