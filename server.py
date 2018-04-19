"""
Usage:
    server.py [options]

Options:
    -d --debug      build mode
"""
import flask
from docopt import docopt

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', array=[1,2,3,4,5])

@app.route('/api')
def json():
    return flask.jsonify(result=42)

if __name__ == "__main__":

    args = docopt(__doc__, version='0.0.1')

    @app.context_processor
    def bundle_creator():
        def bundle_url(name):
            if args['--debug']:
                return f'localhost:8000/{name}'
            else:
                return f'/static/{name}'
        return dict(bundle_url=bundle_url)

    app.run()
