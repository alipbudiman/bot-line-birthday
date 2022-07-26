from flask import Flask, jsonify, redirect, render_template, request, url_for, session
from flask_cors import CORS
from flask_restful import abort
from pymongo import MongoClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    FlexSendMessage,
    BlockStyle,
    BubbleStyle,
    BubbleContainer,
    CarouselContainer,
    BoxComponent,
)
import livejson, time, random


app = Flask(__name__)
CORS(app)


AUTH_ACCESS = 'JmTmVCOK07ASzl4Q9a3zHBbThawecQ3jMFrlYx8fcvlX1AM2yGN7tWm/Xf1L40wzdxJCzGA3mOD38QKyBkp2iwsb2jU+F5SrwzLeb6HgwJprmtqIpKN+X4Syw5WBL1mSkknOCAIggTm+sYtQfA3EMAdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(AUTH_ACCESS)
handler = WebhookHandler('b4107213c0cbd7306a04142de4a9be4d')

step = {}


@app.route('/')
def index():
    return "CREATE BY ALIF BUDIMAN WAHABBI"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    cmd = event.message.text

    if cmd.lower() == "friends is never die" or cmd.lower() == "friend is never die":
        message = "oke aku kenal kamu, kamu keren temennua alip yang ganteng itu."
        message += "\nSekarang kita masuk ke sessi tanya jawab ya"
        message += "\nKeren manis, kamu cukup pilih jawaban dengan ketik A, B, ayau C ya..."
        message += "\nSoal pertama, siapa yang paling ganteng di FIND"
        message += "\nA. Alif"
        message += "\nB. Martin"
        message += "\nC. Millenio"
        step[event.source.user_id] = 1
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    elif step[event.source.user_id] == 1 and cmd.lower() in ["a","b","c"]:
        if cmd.lower() == "a":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="WAH BENER BANGET ALIP YANG PALING GANTENG!!!"))
        elif cmd.lower() == "b":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Loh kok martin, alip dong yg paling ganteng!!"))
        elif cmd.lower() == "c":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Loh kok mille, alip dong yg paling ganteng!!"))
        time.sleep(3)
        if cmd.lower() != "a":
            cos1 = "Gapapalah kalo bukan Alip :("
        else:
            cos1 = "Mantap emang alip dabest"
        res = f"{cos1}. Oke, kita masuk ke pertanyaan ke dua ya!!"
        res += "\nDimana letak sekolah kita waktu masih kelas 1 semeter 1 dan 2"
        res += "\n1. Harmoni"
        res += "\n2. Gajah mada"
        res += "\n3. Mangga besar"
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text=res))
        step[event.source.user_id] = 2
    elif step[event.source.user_id] == 2 and cmd.lower() in ["a","b","c"]:
        if cmd.lower() == "a":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="WAH BENER BANGET, WAKTU KELAS 1 SEMESTER 1 & 2 KAN SEKOLAH KITA NUMPANG SAMA SEKOLAH SD ORANG WKWKWKW"))
        elif cmd.lower() == "b" or cmd.lower() == "c":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="LOH KAMU LUPA INGATAN, sekolah kita kan di harmoni!"))
        time.sleep(3)
        if cmd.lower() != "a":
            cos2 = "Masih muda udah lupa ingatan :("
        else:
            cos2 = "Mantap kamu jawab dengan benar"
        res = f"{cos2}. Oke, kita masuk ke pertanyaan ke dua ya!!"
        res += "\nDi rumah siapa yg kita jadiin basecamp?"
        res += "\nA. Martin"
        res += "\nB. Michelle"
        res += "\nC. Sasa"
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text=res))
        step[event.source.user_id] = 3
    elif step[event.source.user_id] == 3 and cmd.lower() in ["a","b","c"]:
        if cmd.lower() == "c":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Bener bgt, kita dulu suka jajan di depan SD yg ada di deket rumah sasa"))
        elif cmd.lower() == "b" or cmd.lower() == "a":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Loh kamu lupa ingatan, rumah sasa loh yg jadi basecamp kita, kan udah setuju kita"))
        time.sleep(3)
        if cmd.lower() != "c":
            cos3 = "Masih muda udah lupa ingatan :("
        else:
            cos3 = "Mantap kamu jawab dengan benar"
        res = f"{cos3}. Oke, kita masuk ke pertanyaan ke terkhir ya!!"
        res += "\nSiapa mantan keren yg paling di benci sama Alip :v"
        res += "\nA. Fredi"
        res += "\nB. Kaleb"
        res += "\nC. Jhonatan"
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text=res))
        step[event.source.user_id] = 4
    elif step[event.source.user_id] == 4 and cmd.lower() in ["a","b","c"]:
        if cmd.lower() == "b":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Hadeh, bisa-bisanya mau, padahal orangnnya kan baru putus :v"))
        elif cmd.lower() == "a" or cmd.lower() == "c":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="loh kamu lupa sama mantan? wkwkwk"))
        time.sleep(3)
        res += "Oke, selamat udah menjawab semua pertanyaan, ini bukan ulangan jadi ga ada nilai-nilai an ya"
        res += "\nPick up hadiah ulang tahun kamu di link di bawah ini"
        res += ""
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text=res))
    else:
        if event.source.user_id not in step:
            message = "Hallo apa kamu keren? kalo iya, cuma karen yang bisa jawab pertanyaan ini."
            messgae += "\napa kepanjangan dari FIND ?"
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
        else:
            message = "Pilihan kamu kurang tepa, jangan out of question ya!"
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
                 
@app.route("/gift", methods=['GET'])
def gift():
    data = random.choice(["a","b","c"])
    return render_template('main.html',data=str(data))

@app.route("/get", methods=['GET'])
def get():
    data = request.args.get('data')
    if data:
        if data == "a":
            img = "https://i.ibb.co/Vm4S88h/45fc64f46991.jpg"
        elif data == "b":
            img = "https://i.ibb.co/FqrRfmq/25763850f7e0.jpg"
        elif data == "c":
            img = "https://i.ibb.co/5YHSzvz/1b8639a07886.jpg"
        return render_template('success.html',img=img)
    else:
        num = random.choice(["a","b","c"])
        return render_template('get.html',num=num)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5005)