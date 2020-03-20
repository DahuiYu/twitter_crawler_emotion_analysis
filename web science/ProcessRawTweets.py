import string

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
nltk.download('punkt')
nltk.download('wordnet')
stemmer= PorterStemmer()

excitement_list = []
happy_list = []
pleasant_list = []
surprise_list = []
fear_list = []
angry_list = []

current = angry_list


def process_tweet(tweet):

    temp = tweet
    # delete 'text:"'
    tweet = tweet[6: len(tweet)]
    # convert add letters into lowercase
    tweet = tweet.lower()
    # delete numbers in tweet
    tweet = re.sub(r'\d+', '', tweet)
    # delete punctuation mark
    for c in string.punctuation:
        tweet = tweet.replace(c, '')
    # delete heading and trailing space
    tweet = tweet.strip()
    # detele url
    tweet = re.sub(r'[a-z]*[:.]+\S+', '', tweet)
    # delete rt
    tweet = tweet.replace('rt', '', 1)
    # delete stop words
    tokens = word_tokenize(tweet)
    result = [stemmer.stem(i) for i in tokens if not i in ENGLISH_STOP_WORDS and len(i) >= 2 and 'http' not in i]
    target = current
    # classify tweets based on emoticons
    try:
        if re.search('😁', temp) is not None:
            target = excitement_list
        if re.search('😀', temp) is not None:
            target = happy_list
        if re.search('😌', temp) is not None:
            target = pleasant_list
        if re.search('😯', temp) is not None:
            target = surprise_list
        if re.search('😨', temp) is not None:
            target = fear_list
        if re.search('😠', temp) is not None:
            target = angry_list
    except:
        pass
    target.append(result)
    return result


file_name = 'angry.csv'
data = pd.read_csv(file_name, header=None, usecols=[3])
processedTweets = data.applymap(process_tweet)
processed_data = pd.DataFrame(columns=None, data=excitement_list)
processed_data.to_csv('excitement_processed.csv', header=None, mode='a', encoding='gbk')
processed_data = pd.DataFrame(columns=None, data=happy_list)
processed_data.to_csv('happy_processed.csv', header=None, mode='a', encoding='gbk')
processed_data = pd.DataFrame(columns=None, data=pleasant_list)
processed_data.to_csv('pleasant_processed.csv', header=None, mode='a', encoding='gbk')
processed_data = pd.DataFrame(columns=None, data=surprise_list)
processed_data.to_csv('surprise_processed.csv', header=None, mode='a', encoding='gbk')
processed_data = pd.DataFrame(columns=None, data=fear_list)
processed_data.to_csv('fear_processed.csv', header=None, mode='a', encoding='gbk')
processed_data = pd.DataFrame(columns=None, data=angry_list)
processed_data.to_csv('angry_processed.csv', header=None, mode='a', encoding='gbk')