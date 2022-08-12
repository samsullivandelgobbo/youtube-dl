import youtube_dl
import asyncio 
import time


class Logger:
  def debug(self, msg):
    print(msg)
  
  def error(self, msg):
    print(msg)
  
  def warning(self, msg):
    print(msg)
  
def hook(d):
  if ['status'] == 'finished':
    print('Done downloading...')
  if ['status'] == 'downloading':
    print(d['filename'], d['_percent_str'], d['_eta_str'], d['elapsed'])
  

options = {
  'logger': Logger,
  'progress_hooks': [hook]
}
def download(url):
  with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])



async def sleep():
  print(f'Time: {time.time() - start:.2f}')
  await asyncio.sleep(1)

async def main(url, taskname):
  pass

loop = asyncio.get_event_loop()
tasks = [
  loop.create_task(download(input('Enter URL:')))
]


start = time.time()
