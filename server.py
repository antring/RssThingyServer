__author__ = 'Antring'

import urllib.request
import os
import feedparser
import datetime
from time import *


class rssReader:
    '''Class for finding and downloading podcast'''

    def __init__(self, url):
        self.rssurl = url
        self.podstream = feedparser.parse(self.rssurl)
        self.podLink = self.podstream.entries[0].link
        self.podName = self.podstream.entries[0].title
        self.rsslen = len(self.podstream.entries)


    def checker(self):
        '''Checking if a podcast episode is already downloaded'''

        curDir = os.getcwd() #Get current working dir
        #TODO Write rest of this...

    def downloader(self, podcasturl, filename):
        '''For downloading podcasts given a url to the .mp3 and the filename that it should be stored with'''

        try:
            urllib.request.urlretrieve(podcasturl, filename + '.mp3')
            f = open('log.txt', 'a')
            f.write('(+)Downloaded ' + filename + ' - ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + ('\n'))
            f.close()
        except IOError:
            f = open('log.txt', 'a')
            f.write('(!)Downloader error ' + IOError + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + ('\n'))
            f.close()

    def infoprinter(self):
        '''Prints information about the podcast'''
        print("PodLink: ", self.podLink, "\nPodName: ", self.podName, "\nRSSLen: ", self.rsslen)


if __name__ == '__main__':
    misjonen = "http://www.p4.no/lyttesenter/podcast.ashx?pid=330"
    podcast1 = rssReader(misjonen)
    podcast1.infoprinter()