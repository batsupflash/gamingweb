from flask import Flask, render_template, request
import mlab
from mongoengine import *
app = Flask(__name__)

mlab.connect()


class TheGame(Document): #collection
    name = StringField()
    image = StringField()
    description = StringField()


the_game = TheGame(name = "Grand theft auto V",
                        image = "http://cdn.akamai.steamstatic.com/steam/apps/271590/header.jpg?t=1504193224",
                        description = "Trò chơi nằm trong mạch truyện chính của series Grand Theft Auto, mạch truyện này được tính là từ khi bắt đầu nội dung của trò chơi Grand Theft Auto IV (2008), không liên hệ nội dung đến các phần trước Grand Theft Auto IV. Nằm trong tiểu bang hư cấu San Andreas, mô phỏng Nam California, câu chuyện nói về ba tên tội phạm và nỗ lực của họ trong việc thực hiện các cuộc tấn công trong thế giới ngầm bên cạnh là chống lại chính phủ và các thế lực khác. Trò chơi được thiết kế theo kiểu thế giới mở cho phép người chơi tự do đi khắp nơi, các vùng nông thôn, rừng núi, hoang mạc và thành phố hư cấu Los Santos, mô phỏng thành phố Los Angeles ngoài đời.")

the_game.save()

@app.route('/')
def index():
    return render_template('index.html',the_games = TheGame.objects())




if __name__ == '__main__':
  app.run(debug=True)
