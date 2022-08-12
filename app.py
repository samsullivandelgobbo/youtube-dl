from flask import Flask, render_template, request
from download import download
import asyncio 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST', 'GET']) 
async def download_video():
  if request.method == 'POST':
    url = request.form['url']
    print(f'downloading:{ url }')
    # download(url)
    task1 = asyncio.create_task(download(url))
    await asyncio.sleep(3)
    task2 = asyncio.create_task(print('downloading'))
    await task2
    await task1    
    return 'Downloading'



@app.route('/config', methods=['POST', 'GET'])
def config():
  if request.method == 'POST':
    config = request.data



  return render_template('config.html')

@app.route('/progress')
def progress():
  pass