from flask import Flask

def create_app():
"""Create and configure an instance of the Flask application"""
app = Flask(**name**)

@app.route('/')
def root():
    return("Welcome to Twitoff!")

return app
