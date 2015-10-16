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


def fetch(name):

    user = api.GetUser(screen_name=name)
  #  print_data ("Looking info for @"  + user.screen_name)\
    print user.location
    	
    

if __name__ == "__main__":
    global fd
    fd = open("user_info.txt","w")
    fd.write("Name \t Location \n")  
    i = 1
    fetch("detikcom")  
  #  with open("Bali.txt","r") as f:
   #         for line in f:
    #            print i
     #           i = i+1
      #          fetch(line)
   # name = raw_input('Enter a Screen name: ') if len(sys.argv) < 2 else sys.argv[1]
    
    fd.close()
    
    #fetch(name)  
