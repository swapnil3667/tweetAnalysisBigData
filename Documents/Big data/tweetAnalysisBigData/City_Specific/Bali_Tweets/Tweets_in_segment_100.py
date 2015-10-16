import sys, twitter, operator
#from dateutil.parser 
#import parse
import json
import oauth2
import time
import urllib2
import json

reload(sys)
sys.setdefaultencoding("utf-8")

twitterURL = "http://twitter.com"

api = twitter.Api(
          consumer_key="Cfnvp3OzEdr7oM3baUZjRNEbZ",
          consumer_secret="wb0EStemoKt2RR47Fozt6dBQgwctvLYjjWai8LAPslB2AVMAbo",
          access_token_key="85526705-5mwedkg34AVoVGJmHjvI0MxdOS98maaS6xaPmNwLY",
          access_token_secret="zxxQgtXzuQLGatkqNl06BodSQl63sJgyvRFO83bkMZWBW"
       )

query = 'Bali'
max_tweets = 100000
searched_tweets = []
last_id = 0
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
 #   try:
    new_tweets = api.GetSearch(term=query, count=count, max_id=str(last_id - 1))
    if not new_tweets:
       break
    for i, t in enumerate(new_tweets):
	if last_id == 0:
		last_id = t.id
	else:
		last_id = min(last_id,t.id)
    searched_tweets.extend(new_tweets)
    last_id = last_id-1
#    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
#        break

tweet1s = searched_tweets
#f = open(query + "tweetsToFollowfor.html", "wb")
#print >>f, """<html><title>Tweets for</title>
#<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
#<body><small>"""
#for i, t in enumerate(tweet1s):
 #  print >>f, """%d.  <a href="%s/status/%d">%s</a><br/>%s</br>""" % (
  #          i, twitterURL,t.id, t.text.encode("utf8"),t.GetUser().GetScreenName())
   #print >>f, """</small></body></html>"""
#f.close()  


#f = open(query + ".txt", "wb")
a = 0
for i, t in enumerate(tweet1s):
   print i	
   if (i%100 == 0):
	print i
	if a!=0:
        	f.close()
        filen = i/100
	f = open(query + str(filen) + ".txt", "wb")
	a = 1
   print >>f, """%s""" % (
            t.text.encode("utf8"))
f.close() 
