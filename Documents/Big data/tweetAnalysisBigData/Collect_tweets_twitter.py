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

################
# Print data to the console and log file
################
def print_data(data):
	try:
		print data
	#	if arg_output:
	#		tmp = filter(lambda x: x in string.printable, data)
	#		newdata = tmp.replace(color, " ").replace("[0m", " ")
	#		fd.write(newdata + "\n")
		
	except Exception, e:
		print "\n[ print_data() Error ]\n\tError message:\t ", e, "\n"
		sys.exit(1)

def fetch(name):

    user = api.GetUser(screen_name=name)
    print_data ("Looking info for @"  + user.screen_name)
  #  print_data(chr(27) + color + "\tAccount info" + chr(27) + "[0m")
 #   print_data("\t-------------------")
  #  print_data("\tScreen Name:\t\t " + user.screen_name.encode('utf-8'))
   # print_data("\tUser name:\t\t " + user.name.encode('utf-8'))
    #print_data("\tTwitter Unique ID:\t " + str(user.id))
    #print_data("\tAccount created at:\t " + user.created_at.strftime('%m/%d/%Y'))
    #print_data("\tFollowers:\t\t " + str(user.followers_count))
    #print_data("\tTweets:\t\t\t " + str(user.statuses_count))
    #print_data("\tLocation:\t\t " + str(user.location.encode('utf-8')))
    #print_data("\tDescription:\t\t " + str(user.description.encode('utf-8')))
    #print_data("\tURL:\t\t\t " + str(user.url))
    #print_data("\tProfile image URL:\t " + str(user.profile_image_url))
    #print_data("")
    fd.write(user.screen_name.encode('utf-8') + "\t" + user.location.encode('utf-8') +"\n")






query = 'Paris'
max_tweets = 1000
searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
 #   try:
    new_tweets = api.GetSearch(term=query, count=count, max_id=str(last_id - 1))
    if not new_tweets:
       break
    searched_tweets.extend(new_tweets)
#    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
#        break

tweet1s = searched_tweets
f = open(query + "tweetsToFollowfor.html", "wb")
print >>f, """<html><title>Tweets for</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<body><small>"""
for i, t in enumerate(tweet1s):
   print >>f, """%d.  <a href="%s/status/%d">%s</a><br/>%s</br>""" % (
            i, twitterURL,t.id, t.text.encode("utf8"),t.GetUser().GetScreenName())
   print >>f, """</small></body></html>"""
f.close()  


f = open(query + ".txt", "wb")
for i, t in enumerate(tweet1s):
   print >>f, """%s""" % (
            t.user.screen_name)
f.close() 

fd = open(query + "_user_info.txt","w")
fd.write("Name \t Location \n")
i = 1  
with open(query + ".txt","r") as f:
        for line in f:
            print i
            i = i+1
            fetch(line)           
fd.close
