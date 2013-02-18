'''
twitter/harvester.py
A harvester for twitter
'''
from ntent import keys
import tweepy


class TwitterHarvester(object):
    def run(self):
        print 'Connecting to stream...'
        auth = tweepy.OAuthHandler(
            keys.TWITTER_CONSUMER_KEY,
            keys.TWITTER_CONSUMER_SECRET
        )
        auth.set_access_token(
            keys.TWITTER_ACCESS_TOKEN,
            keys.TWITTER_TOKEN_SECRET
        )
        print 'Attaching to stream...'
        streaming_api = tweepy.streaming.Stream(
            auth,
            TwitterStreamListener(),
            timeout=60
        )
        streaming_api.filter(follow=None, track=['need', 'want'])


class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            # print '%s\t%s\t%s\t%s' % (
            #    status.text,
            #    status.author.screen_name,
            #    status.created_at,
            #    status.source
            # )
            if (status.coordinates):
                c = status.coordinates
                print 'from %s, %s' % (
                    c['coordinates'][1],
                    c['coordinates'][0]
                )

        except Exception, e:
            print 'Exception! %s' % e

    def on_error(self, status_code):
        print 'Encountered error with status code %s' % status_code
        return True  # Don't kill the stream

    def on_timeout(self):
        print 'Timeout...'
        return True  # Don't kill the stream
