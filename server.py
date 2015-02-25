__author__ = 'Antring'

import urllib
import os
import feedparser
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
        #os.getcwd() current working directory
        #
        pass

    def downloader(self, podcasturl, filename):
        '''For downloading podcasts given a url to the .mp3 and the filename that it should be stored with'''
        fileRetriever = urllib.URLopener()

        try:
            fileRetriever.retrieve(podcasturl, filename + '.mp3')
            f = open('log.txt', 'a')
            # FIXME f.write('(+)Downloaded ' + filename + ' - ' + time.asctime(time.localtime(time.time())) + ('\n'))
            f.close()
        except IOError:
            f = open('log.txt', 'a')
            # FIXME f.write('(!)Downloader error ', IOError, time.asctime(time.localtime(time())), ('\n'))
            f.close()

    def infoprinter(self):
        '''Prints information about the podcast'''
        print("PodLink: ", self.podLink, "\nPodName: ", self.podName, "\nRSSLen: ", self.rsslen)


if __name__ == '__main__':
    misjonen = "http://www.p4.no/lyttesenter/podcast.ashx?pid=330"
    podcast1 = rssReader(misjonen)
    podcast1.infoprinter()