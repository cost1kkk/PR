from flask import Flask, request


# Create the application instance
app = Flask(__name__)


@app.route('/ball')
def ball():
    return {
        'message1': 'ball',
        'message2': 'post',
        'message3': 'foot'
    }

@app.route('/gimme', methods=['GET', 'POST'])
def easy():
    if request.method == 'GET':
        return {
            'message': 'It was easy'
        }
    elif request.method == 'POST':
        payload = request.json
        print(payload)
        return {
            'message': 'No it wasnt'
        }

# Create a URL route in our application for "/bread"
@app.route('/bread')
def bread():
    return 'butter'

# Start the server
app.run()



# Start the server
app.run()
