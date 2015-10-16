import tweepy, time, sys
import tweepy
import twitter
# assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)
#from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

CONSUMER_KEY = 'Cfnvp3OzEdr7oM3baUZjRNEbZ'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'wb0EStemoKt2RR47Fozt6dBQgwctvLYjjWai8LAPslB2AVMAbo'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '85526705-5mwedkg34AVoVGJmHjvI0MxdOS98maaS6xaPmNwLY'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'zxxQgtXzuQLGatkqNl06BodSQl63sJgyvRFO83bkMZWBW'#keep the quotes, replace this with your access token secret


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#api = tweepy.API(auth)

#auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitterURL = "http://twitter.com"
api = tweepy.API(auth)

query = 'Bali'
max_tweets = 10
searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(term=query, count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break

tweet1s = searched_tweets
f = open(query + "tweetsToFollowfor.html", "wb")
print >>f, """<html><title>Tweets for</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<body><small>"""
for i, t in enumerate(tweet1s):
   print >>f, """%d.  <a href="%s/status/%d">%s</a><br/>%s</br>""" % (
            i, twitterURL,t.id, t.text.encode("utf8"),t.user.screen_name)
   print >>f, """</small></body></html>"""
f.close() 


f = open(query + ".txt", "wb")
for i, t in enumerate(tweet1s):
   print >>f, """%d.   %s \n""" % (
            i,t.user.screen_name)
f.close()  

