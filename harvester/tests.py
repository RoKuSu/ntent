'''
'''
from harvester.twitter import TwitterHarvester
from django.utils import unittest


class TwitterHarvesterTest(unittest.TestCase):

    def testHarvest(self):
        print 'Howdy Michael!'
        h = TwitterHarvester()
        h.run()
