"""
Figuring out youtube-dl's hooks
"""

import youtube_dl


class Logger(object):
    def debug(self, msg):
        print (msg)
        

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

def hook(d):
    if d['status'] == 'finished':
        return ('Done downloading, now converting ...')
    if d['status'] == 'downloading':
        return (d['filename'], d['_percent_str'],'ETA:', d['_eta_str'],'Elapsed:', d['elapsed'])
    if d['status'] == 'error':
        return (d['error'])

options = {
    "logger": Logger(),
    "progress_hooks": [hook],
}

def download(url):
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

download(input('Enter url: '))

# print(Logger.debug)   


