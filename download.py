import youtube_dl
import asyncio


class Logger(object):
    def debug(self, msg):
        return msg

    def warning(self, msg):
        return msg

    def error(self, msg):
        return msg

def my_hook(d):
    if d['status'] == 'finished':
        return 'Done downloading, now converting ...'

options = {
    "logger": Logger(),
    "progress_hooks": [my_hook],
}

async def download(url):
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])



