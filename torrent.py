import urllib, requests, os
from bs4 import BeautifulSoup

'''
    The base class for all torrent downloaders to derive from.
    It shares an interface that is used throughout all download instances.
'''

# TODO: abstract
class TorrentDownloader(object):

    '''
        #
    '''
    def __init__(self):
        base = ''

    '''
        # description
        This function merely starts the magnet link, using the default
        software that the operating system designates it should use,
        for example, uTorrent. It does not in itself download the file.

        # params
        @magnet_link: a full path to a magnet link, it usually resides on torrent sites anchor tag
    '''
    def download(self, magnet_link):
        try:
            os.startfile(magnet_link)
        except Exception as err:
            print("Err: %s" % err)


'''
    A specific implementation of a class that downloads from the site piratebay: www.piratebay.se
'''
class PirateBayDownloader(TorrentDownloader):

    def __init__(self):
        base = 'https://thepiratebay.se'

    '''
        # description
        Make a request to a given url and find the magnet link on a pre-determined html structure.

        # params
        @url: The full path to the torrent to download, for ex:
            https://thepiratebay.se/torrent/10176531/Game.of.Thrones.S04E07.720p.HDTV.x264-KILLERS_[PublicHD]
    '''
    def get_magnet(self, url):
        request = requests.get(url)
        if request:
            html = BeautifulSoup(request.content)
            if html:
                magnet = html.find('div', attrs={'class': 'download'})
                return magnet.a['href']
        else:
            raise Exception("Could not request url %s" % url)


    '''
        # description
        Search for hd shows on piratebay and order it by most seeds.

        # params
        @query: The query to search for, it will be automatically url escaped.
    '''
    def search_hdshows(self, query):
        url = base + '/search/%s/0/7/208' % urllib.request.pathname2url(query)
        request = requests.get(url)

        if request:
            html = BeautifulSoup(request.content)

            if html:
                divs = html.find_all('div', attrs={'class':'detName'})
                for div in divs:
                    anchor = div.a

                    (name, href) = anchor.text, anchor['href']

                    # TODO: check if file does not already exist in local lib
                    if True:
                        download_url = self.base + href
                        magnet_link = get_magnet(download_url)
                        print(magnet_link)
        else:
            raise Exception("Could not request url %s" % url)









