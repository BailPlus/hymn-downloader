from flask import Flask, request, render_template, abort, redirect
import libgetmp3, urllib.parse, liblingting

IZM_DOMAIN = 'izanmei.net'
LT_DOMAIN = 'share.lingtingmusic.com'

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
    parsed_url = urllib.parse.urlparse(url)
    match parsed_url.netloc:
        case d if d == IZM_DOMAIN:
            try:
                return redirect(
                    await libgetmp3.get_music(url)
                )
            except libgetmp3.ParseFailed as e:
                abort(500, str(e))
        case d if d == LT_DOMAIN:
            return redirect(
                await liblingting.get_music(url)
            )
        case d:
            abort(400, f'未支持的网站：{d}')


if __name__ == '__main__':
    app.run()
