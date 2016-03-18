#import necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#adding user credentials to the following variables
access_token = ''
access_token_secret = '' 
consumer_key = ''
consumer_secret = ''

file = open('twitter_data.txt', 'w')
#printing tweets
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        file.write(data)               
                
        #print data
        return True
        
    def on_error(self, status):
        print status
        
if __name__=='__main__':
    
    #handling authentication and connection to twitter api
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #filtering twitter streams by keywords
    stream.filter(track=['python','javascript','ruby'])
    
    

