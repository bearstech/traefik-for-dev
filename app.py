from wsgiref.simple_server import make_server
import os


def app(environ, start_response):

    with open('html/index.html') as fd:
        html = fd.read()

    html = html.format(**os.environ)
    html = html.encode('utf8')

    status = '200 OK'
    headers = [
        ('Content-type', 'text/html; charset=utf8'),
        ('Content-Length', str(len(html))),
    ]
    start_response(status, headers)
    return [html]


httpd = make_server('', 8000, app)
print("Serving on port http://0.0.0.0:8000...")
httpd.serve_forever()
