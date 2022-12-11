from flask import Flask, send_file, jsonify

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello_world():
    print('in hello')
    return jsonify(
        {
            'response': 'hello world'
        }
    )


@app.route('/makefile/<name>', methods=['GET'])
def get_makefile(name):
    print('in /makefile')
    path = './responses/{}/makefile'.format(name)
    return send_file(path)


# Same endpoint as Canvas API
@app.route('/api/v1/files/<fileId>', methods=['GET'])
def get_canvas_file(fileId):
    path = 'responses/canvas/get-file/{}.json'.format(fileId)
    return send_file(path)


@app.route('/api/v1/courses/<course_id>/assignments/<assignment_id>'
           '/submissions/<user_id>', methods=['GET'])
def get_canvas_submission(course_id, assignment_id, user_id):
    path = ''
    return send_file(path)


if __name__ == '__main__':
    app.run(debug=True, port=55321)
