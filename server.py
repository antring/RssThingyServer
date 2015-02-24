__author__ = 'Antring'

import urllib
import os
import feedparser
from time import *


class rssReader:
    '''Class for finding and downloading podcast'''
    def __init__(self, url):
        self.podLink = url.entries[0].link
        self.podName = url.entries[0].title

    def checker(self):
        '''Checking if podcastepisode is already downloaded'''
        pass

    def downloader(self):
        '''Downloading podcastepisode'''
        pass
