# Websocket Chat
A simple chat using websockets with Socket.io

## Demo
Only tested on Google Chrome Version 43.0.2357.124 (64-bit) on Mac OSX

[http://hidden-wildwood-6596.herokuapp.com/chat](http://hidden-wildwood-6596.herokuapp.com/chat)


## To Run

You will need the Python virtualenv and pip to install dependencies

```
cd <path/to/this/repo>

// create Python virtual environment and activate
virtualenv venv
source venv/bin/activate

// install dependencies
pip install -r requirements.txt

// set port in environment variable
export PORT=5000

// run
python application.py

```

Go to `http://localhost:5000/chat` to start chatting! Open another window and chat with yourself so it's not so lonely 

## Tech Stack

* Heroku
* Flask
* Flask-SocketIO
* AngularJS
* Socket.io
* SASS

## Known bugs

* Sometimes sends message out twice