from flask import Flask, request, render_template, abort, redirect
from .adapter.base import HymnPlatform

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')

@app.post('/')
def get_mp3():
    url = request.form.get('url')
    if not url:
        abort(400, '请输入网址')
    url = url[url.find('http'):]
    if not url:
        abort(400, '请输入网址')
    platform = HymnPlatform.from_url(url)
    return redirect(platform.get_mp3_url(url))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
