'''
'''
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from pymongo import MongoClient
import django
import json
import os
import twitter

# http://knoesis.org/projects/emotion


class Command(BaseCommand):

    args = ''
    help = ''

    DATA_HOME = '/Users/bowmanmc/workspace/ntent/knoesis.data/'

    DATA_FILES = [
    #    'dev.txt',
    #    'test.txt',
    #    'train_1.txt',
        'train_2_1.txt',
    #    'train_2_2.txt',
    #    'train_2_3.txt',
    #    'train_2_4.txt',
    #    'train_2_5.txt',
    #    'train_2_6.txt',
    #    'train_2_7.txt',
    #    'train_2_8.txt',
    #    'train_2_9.txt',
    #    'train_2_10.txt'
    ]

    def handle(self, *args, **options):
        for data_file in Command.DATA_FILES:
            self.load_file(os.path.join(Command.DATA_HOME, data_file))

    def load_file(self, file_path):
        print 'loading file from %s' % file_path
        f = open(file_path, 'r')
        for line in f:
            try:
                self.load_line(line)
            except Exception, e:
                print 'Error loading line %s with error %s' % (line, e)

    def load_line(self, line):
        parts = line.split()
        id = parts[0]
        emotion = parts[1]
        print 'tweet %s is %s' % (id, emotion)
#        auth = tweepy.OAuthHandler(
#            settings.TWITTER_CONSUMER_KEY,
#            settings.TWITTER_CONSUMER_SECRET
#        )
#        auth.set_access_token(
#            settings.TWITTER_ACCESS_TOKEN,
#            settings.TWITTER_TOKEN_SECRET
#        )
#        api = tweepy.API(auth)
        t = twitter.Twitter(domain='api.twitter.com', api_version='1')
        # No authentication required, but rate limiting is enforced
        tweet = t.statuses.show(id=id, include_entities=1)
        tweet['emotion'] = emotion
        # print 'saving tweet %s: %s' % (tweet.id, tweet.text)
        if tweet['text']:
            self.save_tweet(tweet)
        else:
            print 'Error loading tweet %s' % id

    def save_tweet(self, tweet):
        connection = MongoClient()
        db = connection['knoesis']
        print '----'
        print dir(tweet)
        print tweet
        print '----'
        id = db['tweets'].insert(tweet)
        print 'Saved to id %s' % id
