import time
import urllib.request


def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']

_hello_resp = (
               '    <html>\n'
               '        <head>\n'
               '            <title>Hello {name}</title>\n'
               '        </head>\n'
               '        <body>\n'
               '            <h1>Hello {name}!</h1>\n'
               '        </body>\n'
               '    </html>')


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.getvalue('name'))
    yield resp.encode('utf-8')


def image(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    if params.getvalue('url') is None:
        url = 'http://www.burpee.org/wp-content/uploads/2017/10/bald-eagle-in-flight-1024x683.jpg'
    else:
        url = params.getvalue('url')
    urllib.request.urlretrieve(url, 'my_image.jpg')
    resp = _img_resp.format(url)
    yield resp.encode('utf-8')


_localtime_resp = ('<?xml version="1.0"?>\n'
                   '        <time>\n'
                   '            <year>{t.tm_year}</year>\n'
                   '            <month>{t.tm_mon}</month>\n'
                   '            <day>{t.tm_mday}</day>\n'
                   '            <hour>{t.tm_hour}</hour>\n'
                   '            <minute>{t.tm_min}</minute>\n'
                   '            <second>{t.tm_sec}</second>\n'
                   '        </time>')

#html code to display image in browser
_img_resp =(
    '<!DOCTYPE html>\n'
    '        <head>\n'
    '            <title>Image to server</title>\n'
    '         </head>\n'
    '       <body>\n'
    '            <img src="{}" alt="Image to server">\n'
    '       </body></html>'
)


def localtime(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/xml')])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')
