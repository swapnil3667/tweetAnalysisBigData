import tweepy
import sys
import getopt
import datetime
import urllib2
import os
import string


# OAuth Settings
# How to obtain the API key:
# Go to https://dev.twitter.com/apps/new
# Copy the consumer key (API key), consumer secret, access token and access token secret
CONSUMER_KEY = 'Cfnvp3OzEdr7oM3baUZjRNEbZ' 
CONSUMER_SECRET = 'wb0EStemoKt2RR47Fozt6dBQgwctvLYjjWai8LAPslB2AVMAbo' 
ACCESS_TOKEN = '85526705-5mwedkg34AVoVGJmHjvI0MxdOS98maaS6xaPmNwLY' 
ACCESS_TOKEN_SECRET = 'zxxQgtXzuQLGatkqNl06BodSQl63sJgyvRFO83bkMZWBW'

# User authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

	

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


# Tweepy (a Python library for accessing the Twitter API)

def fetch(name):

    user = api.get_user(name)
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


if __name__ == "__main__":
    global fd
    fd = open("user_info.txt","w")
    fd.write("Name \t Location \n")  
    i = 1  
    with open("Bali.txt","r") as f:
            for line in f:
                print i
                i = i+1
                fetch(line)
   # name = raw_input('Enter a Screen name: ') if len(sys.argv) < 2 else sys.argv[1]
    
    fd.close()
    
    #fetch(name)  
