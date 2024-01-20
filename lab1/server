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


# Create a URL route in our application for "/bread"
@app.route('/bread')
def bread():
    return 'butter'




# Start the server
app.run()
