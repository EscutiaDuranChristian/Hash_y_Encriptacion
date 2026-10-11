from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session
import os
import requests
from datetime import datetime


app = Flask(__name__)
app.secret_key = "loslicsenciadosrifan"

UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "img")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def obtenerNuevonombre(img):
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    if img and img.filename != "":
        filename_pic = f"{os.path.splitext(img.filename)[0]}_{fecha}{os.path.splitext(img.filename)[1]}"
        img.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_pic))
        return filename_pic
    return None
        

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    password = request.form["pass"]
    if user == "admin" and password == "123":
        session['user'] = user
        session['rol'] = 'admin'
        session['firstname'] = 'Christian'
        session['lastname'] = 'Escutia'
        session['streat'] = 'Carrara'
        session['number'] = '120A'
        session['col'] = 'Ancona'
        session['cp'] = '38920'
        return redirect("/usersView")
    return render_template("index.html", message="Usuario y/o contraseña incorrecto(s)")

@app.route('usersView')
def UsersView():
    return render_template("/usersView.html", session=session)
    
@app.route("/createuser")
def form_user():
    return render_template("createUser.html")

@app.route("/createuser", methods=["POST"])
def create_user():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    rfc = request.form["rfc"]
    curp = request.form["curp"]
    nac = request.form["nac"]
    tel = request.form["tel"]
    emTel = request.form.get("emTel")  # opcional
    call = request.form["call"]
    nCasa = request.form["nCasa"]
    col = request.form["col"]
    cp = request.form["cp"]
    rol = request.form["rol"]
    user = request.form["user"]
    password = request.form["pass"]

    # Archivos
    imgPic = request.files.get("imgPic")
    imgBack = request.files.get("imgBack")
    
    imgPic = obtenerNuevonombre(imgPic)
    imgBack = obtenerNuevonombre(imgBack)
    
    return redirect('/usersView')
    

@app.route("/delete", methods=['POST'])
def Delete():
    id = request.form["id"]
    #Borrar
    return redirect('usersView')

@app.route("/update", methods=['POST'])
def UpdatePage():
    id = request.form["id"]
    #Obtener datos
    datos = []
    return render_template('updateUser.html', datos=datos)

@app.route("/updateuser", methods=['POST'])
def Update():
    id = request.form["id"]
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    rfc = request.form["rfc"]
    curp = request.form["curp"]
    nac = request.form["nac"]
    tel = request.form["tel"]
    emTel = request.form.get("emTel")  # opcional
    call = request.form["call"]
    nCasa = request.form["nCasa"]
    col = request.form["col"]
    cp = request.form["cp"]
    rol = request.form["rol"]
    user = request.form["user"]
    password = request.form["pass"]

    # Archivos
    imgPic = request.files.get("imgPic")
    imgBack = request.files.get("imgBack")
    
    
    return redirect("usersView")
    
@app.route("/css/<css>")
def css(css):
    return send_from_directory(os.path.join("Templates/css/"), css)

@app.route("/img/<img>")
def img(img):
    return send_from_directory(os.path.join("Templates/img/"), img)

if __name__ == "__main__":
    app.run()