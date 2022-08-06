from flask import Flask, render_template, request
from download import download

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST', 'GET']) 
def download_video():
  if request.method == 'POST':
    url = request.form['url']
    download(url)
    return 'downloading...'

  return 'Downloaded!'


@app.route('/config', methods=['POST', 'GET'])
def config():
  if request.method == 'POST':
    config = request.data


  return render_template('config.html')

@app.route('/progress')
def progress():
  pass