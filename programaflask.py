from flask import Flask, render_template

app = Flask(__name__)

#criar 1 pagina so site
#route -> testeflask.com/
#função -> O que vc quer exibir naquela pagina

@app.route("/")
def homepage ():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos ():
    return render_template ("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios (nome_usuario):
    return render_template ("usuarios.html", nome_usuario = nome_usuario)

if __name__=="__main__":
    app.run(debug=True)

cdcdlclc,lc,l,cld,cld,cld,cld,cld,clc,
ld,cld,c,dlc,dl,cld,cld,cld,cl,dlc,dl,contatos
cdc,ld,cld,cld,cl,dlc,ld,cld,cld,cl,cld,classmethod


