from flask import Flask, render_template, request
import mlab
from mongoengine import *
app = Flask(__name__)

mlab.connect()


class TheGame(Document): #collection
        name = StringField()
        image = StringField()
        description = StringField()




@app.route('/')
def index():
    return render_template('index.html',the_games = TheGame.objects())




if __name__ == '__main__':
  app.run(debug=True)
