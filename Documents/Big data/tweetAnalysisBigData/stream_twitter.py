from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'Cfnvp3OzEdr7oM3baUZjRNEbZ'
csecret = 'wb0EStemoKt2RR47Fozt6dBQgwctvLYjjWai8LAPslB2AVMAbo'
atoken = '85526705-5mwedkg34AVoVGJmHjvI0MxdOS98maaS6xaPmNwLY'
asecret = 'zxxQgtXzuQLGatkqNl06BodSQl63sJgyvRFO83bkMZWBW'

class listener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["CWC2015"])