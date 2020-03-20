from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials

class TwitterStreamer():
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            with open(file_name, 'a', encoding='utf-8') as csvfile:
                csvfile.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
    # change tag and file name to crawl corresponding tweets
    target_tag_list = ["surprise"]
    file_name = 'surprise.csv'
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(file_name, target_tag_list)