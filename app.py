from flask import Flask, render_template, request, redirect
import mlab
from mongoengine import *
app = Flask(__name__)

mlab.connect()


class TheGame(Document): #collection
        name = StringField()
        image = StringField()
        description = StringField()
        image_detail = StringField()
        description_detail = StringField()


@app.route('/')
def index():
    return render_template('index.html',the_games = TheGame.objects())

@app.route('/<game_id>')
def game_detail(game_id):
    the_game1 = TheGame.objects().with_id(game_id)
    if the_game1 is not None:
        return render_template('detail_game.html', the_game = TheGame.objects().with_id(game_id))

@app.route('/admin')
def admin():
    return render_template("admin.html",the_games = TheGame.objects())

@app.route('/admin/delete_game/<game_id>')
def delete_game(game_id):
    # 1. delete game from database
    the_game = TheGame.objects().with_id(game_id)
    if the_game is not None:
        #found
        the_game.delete()

    # 2. Come back to admin

    return redirect("/admin")
@app.route('/admin/edit_game/<game_id>')
def edit_name(game_id):
    the_game = TheGame.objects().with_id(game_id)
    if the_game is not None:

        return str(the_game)
    #1.
    #2.
@app.route('/admin/add_game')
def add_game():
    return render_template('expression')

if __name__ == '__main__':
  app.run(debug=True)
