import sys, twitter, operator
#from dateutil.parser 
#import parse
import json
import oauth2
import time
import urllib2
import json
import time 

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


i = 1
query = 'Bali' 
fileno = 0
a =0
#for i in range(3,4): 
with open("BaliUsers_SetimentalAnalysis" +".txt","r") as f:
#		fd = open(query + str(i) +"_user_info.txt","w")
	#i = 1
  for line in f:
      if fileno < 1600:
        fileno = fileno +1
        continue
      if (fileno%100 == 0):
 #            print i
             if a!=0:
                  fd.close()
                  time.sleep(900)
             filen = fileno/100     
             fd = open(query + str(filen) +"_user_info.txt", "wb")     
        
      fileno = fileno +1 
      a =1        
      user = api.GetUser(screen_name=line)
      print_data ("Looking info for @"  + user.screen_name)
      fd.write(user.screen_name.encode('utf-8') + "\t" + user.location.encode('utf-8') +"\n")
  fd.close()  			         


