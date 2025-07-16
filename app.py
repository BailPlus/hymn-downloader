from flask import Flask, request, render_template, abort, redirect
import libgetmp3

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')

@app.post('/')
async def get_mp3():
    url = request.form.get('url')
    url = url[url.find('http'):]
    if not url:
        abort(400, '请输入网址')
    try:
        return redirect(
            await libgetmp3.get_music(url)
        )
    except libgetmp3.ParseFailed as e:
        abort(500, str(e))


if __name__ == '__main__':
    app.run()
