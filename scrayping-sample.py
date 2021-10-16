import requests
import re
from bs4 import BeautifulSoup
from flask import Flask, request,render_template

# Webページを取得して解析する
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        print("URL?:" + str(request.form['surl']))
        #送信されたURL
        load_url = request.form['surl']
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content, "html.parser")
        #TODO:URLに合わせてセレクタ動的に変えられる？
        elems = soup.select('#uamods > header > h1')
        elems
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        return render_template('form.html')

#お約束
if __name__ == "__main__":
    app.run(port = 8000, debug=True)
