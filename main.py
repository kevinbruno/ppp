import os
from flask import Flask, render_template, url_for

app = Flask(__name__) # cria a aplicação web

@app.route('/')
def home():
     # define as variaveis
    bt1 = 'COMPRAR INGRESSOS'
    bt2 = 'WHATSAPP'
    bt3 = 'SIGA-NOS NO INSTAGRAM'
    bt4 = 'GITANNA.COM'
    bt5 = 'LOCALIZAÇÃO'
    link1 = 'https://www.gitanna.com/'
    link2 = 'https://api.whatsapp.com/send/?phone=5547992593049&text&app_absent=0'
    link3 = 'https://www.instagram.com/gitannalounge/'
    link4 = 'https://www.gitanna.com/'
    link5 = 'https://www.google.com.br/maps/place/Av.+Rodesindo+Pavan,+707+-+Barra,+Balne%C3%A1rio+Cambori%C3%BA+-+SC,+88333-120/@-26.9999094,-48.602785,3a,75y,316.52h,89.83t/data=!3m7!1e1!3m5!1sUJSlvi996xngm8FOS9ZXaQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DUJSlvi996xngm8FOS9ZXaQ%26cb_client%3Dsearch.gws-prod.gps%26w%3D86%26h%3D86%26yaw%3D241.06943%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192!4m5!3m4!1s0x94d8b64deefd0871:0x6424cbccbaa99856!8m2!3d-26.9999196!4d-48.6028408'
     # carrega o template html em sí
    return render_template('index.html',
    bt1=bt1, bt2=bt2, bt3=bt3, bt4=bt4, bt5=bt5,
    link1=link1, link2=link2, link3=link3, link4=link4,
    link5=link5)

@app.errorhandler(404)
def nao_encontrada(e):
    return home()

if __name__ == '__main__':
    porta = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=porta)
