from bottle import route, error, run
from sys import argv

@route('/')
def index():
    x='<h1>Bottle verkefni 2a</h1>'
    x2='<h2><a href=/hlekk/1>Hlekkur</a></h2>'
    x3='<h2><a href=/hlekk/2>Hlekkur 2</a></h2>'
    x4='<h2><a href=/hlekk/3>Hlekkur 3</a></h2>'
    return x,x2,x3,x4
@route('/hlekk/<num>')
def link(num):
    x='<h2><a href =/>Til baka</a></h2>'
    x2='<h1>Þú val hlekkur '+ num +'</h1>'
    return x,x2
@error(404)
def error404(error):
    return '<h1>Nothing here, sorry.</h1>'
run(host='0.0.0.0', port=argv[1], debug=True, reloader=True)