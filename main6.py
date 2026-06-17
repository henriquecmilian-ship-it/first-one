from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Dependencia tecnologica!</h1>
    <h2>Dependencia tecnologica, o que é?</h2>
    <p>A dependência tecnológica refere-se à dependência crescente das pessoas e sociedades em tecnologias para realizar atividades cotidianas.</p>
    <p>Essa dependência pode trazer benefícios, mas também pode gerar riscos e desafios.</p>
    <p>esses riscos podem ser:</p>
    <ul>
        <li>Perda de autonomia</li>
        <li>Dependência excessiva</li>
        <li>Riscos à privacidade e segurança</li>
    </ul>
    <a href='/sobre_mim'>conheça mais a meu respeito</a>"""

@app.route("/sobre_mim")
def sobre_mim():
    return """<h1>Henrique</h1>
    <a href='/'>home</a>
    <p>Meu nome é Henrique e sou um desenvolvedor web</p>
    <p>Tenho experiência em Python e um pouco de HTML/CSS</p>
    <h1>TENHO MUITA AURA E EGO!!!</h1>
    <p>Jogo futebol, jogo videogame e gosto de música de Michael Jackson</P>
    <h3>AUU!<h3/>"""

app.run(debug=True)
