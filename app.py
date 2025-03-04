from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "http://meme-api.com/gimme"
    response = requests.get(url).json()
    meme_pic = response['preview'][-1]  # Choose the image resolution you want
    subreddit = response['subreddit']
    return render_template('index.html', meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(debug=True)
