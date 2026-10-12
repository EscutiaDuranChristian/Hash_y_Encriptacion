from flask import render_template, request, redirect, url_for, session
import requests
from datetime import datetime
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "img")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def obtenerNuevonombre(img):
    fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
    if img and img.filename != "":
        filename_pic = f"{os.path.splitext(img.filename)[0]}_{fecha}{os.path.splitext(img.filename)[1]}"
        #Guardar archivo
        return filename_pic
    return None
        


def root():
    return render_template("index.html")

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

def UsersView():
    return render_template("api/usersView.html", session=session)
    
def form_user():
    return render_template("pages/createUser.html")

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
    

def Delete():
    id = request.form["id"]
    #Borrar
    return redirect('/usersView')

def UpdatePage():
    id = request.form["id"]
    #Obtener datos
    datos = []
    return render_template('pages/updateUser.html', datos=datos)

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
    
    
    return redirect("/usersView")