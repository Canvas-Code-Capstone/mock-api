from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    print('in hello')
    return jsonify(
        {
            'response': 'hello world'
        }
    )

@app.route('/makefile/<name>')
def get_makefile(name):
    print('in /makefile')
    path = './responses/{}/makefile'.format(name)
    return send_file(path)


if __name__ == '__main__':
    app.run(debug=True, port=55321)