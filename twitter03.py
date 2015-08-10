import ConfigParser
import tweepy, datetime, sys
import csv
import codecs
import json

config = ConfigParser.ConfigParser()
config.readfp(open(r'/Users/marcusguttenplan/Desktop/proj/2015_thesis/008_twitter/tweeze/config.txt'))
CKEY = config.get('config', 'CKEY')
CSECRET = config.get('config', 'CSECRET')
ATKEY = config.get('config', 'ATKEY')
ATSECRET = config.get('config', 'ATSECRET')

auth = tweepy.OAuthHandler(CKEY, CSECRET)
auth.set_access_token(ATKEY, ATSECRET)
api = tweepy.API(auth) 




class CustomStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

        f = codecs.open('rawtweet.txt','a', encoding='utf-8', errors='replace')
        f.write('Author,Date,Text''\n')
        writer = csv.writer(f)
        # writer.writerow([status.author.screen_name, status.created_at, status.text])
        writer.writerow((decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))

    def on_error(self, status):
        print status

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=[-118.481084, 34.006270, -118.142280, 34.154361]) 





sapi.filter(track=['curiosity'])









api.update_status()



LOS ANGELES BOUNDING BOX
-118.481084, 34.006270, -118.142280, 34.154361

Ocean Park
Santa Monica, CA
34.006270, -118.481084


Pasadena WIC Program
363 E Villa St, Pasadena, CA 91101
34.154361, -118.142280