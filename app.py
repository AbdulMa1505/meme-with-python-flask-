from flask import Flask,render_template
import json
import requests

app =Flask(__name__)
@app.route('/')
def getMeme():
    url="http://meme-api.com/gimme"
    response =json.loads(requests.request("GET",url).text)
    meme_large=response['preview'][-2]
    subbreddit =response['subreddit']
    return meme_large,subbreddit
def index():
    meme_pic,subrredit =getMeme()
    return render_template('index.html',meme_pic=meme_pic,subrredit=subrredit)

if __name__=="__main__":
    app.run(debug=True)
