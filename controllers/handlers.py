from flask import render_template, request, redirect, session, current_app
import requests
from datetime import datetime
import os
import jwt


API_BASE = "https://api-usuarios-gerogevt2026.azurewebsites.net"

def obtenerNuevonombre(img):
    if img and img.filename != "":
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{os.path.splitext(img.filename)[0]}_{fecha}{os.path.splitext(img.filename)[1]}"
        ruta_guardado = os.path.join(current_app.root_path, "tmp", "img", filename)

        return filename, ruta_guardado, img
    return None, None, None

def root():
    return render_template("index.html")


def logout():
    session.clear()
    return redirect("/")


def login():
    username = request.form["user"]
    password = request.form["pass"]

    data = {
        "grant_type": "password",
        "username": username,
        "password": password,
        "scope": "",
        "client_id": "string",
        "client_secret": ""
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(f"{API_BASE}/login", data=data, headers=headers)

    if resp.status_code == 200:
        data = resp.json()
        token = data.get("access_token")
        session["jwt"] = token
        session["rol"] = data.get("rol")

        # Decodificar para obtener el id
        decoded = jwt.decode(token, options={"verify_signature": False})
        user_id = decoded.get("sub")
        session["user_id"] = user_id

        # Pedir datos del usuario logeado
        headers = {"Authorization": f"Bearer {token}"}
        user_resp = requests.get(f"{API_BASE}/usuarios/{user_id}", headers=headers)
        if user_resp.status_code == 200:
            usuario = user_resp.json()
            print(usuario)
            # Guardar en sesión lo que necesitas para el template
            session["firstname"] = usuario.get("nombre")
            session["lastname"] = usuario.get("apellido")
            session["usuario"] = usuario.get("usuario")
            session["email"] = usuario.get("email")
            session["streat"] = usuario.get("calle")
            session["number"] = usuario.get("numero")
            session["col"] = usuario.get("colonia")
            session["cp"] = usuario.get("codigo_postal")
            session["pic"] = usuario.get("imagen_usuario_url")
            session["fondo"] = usuario.get("imagen_fondo_url")

        return redirect("/usersView")
    else:
        return render_template("index.html", message="User or/and password incorrect(s)")

def UsersView():
    token = session.get("jwt")
    if not token:
        return redirect("/")

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{API_BASE}/usuarios", headers=headers)

    if resp.status_code == 200:
        usuarios = resp.json()  # lista de usuarios
        return render_template("api/usersView.html", usuarios=usuarios, session=session)
    else:
        return "Error al obtener usuarios"

    
def form_user():
    return render_template("pages/createUser.html")

def create_user():
    token = session.get("jwt")
    if not token:
        return redirect("/")
    
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

    print(f"{call} {col} {nCasa} {cp}")
    # Archivos
    imgPic = request.files.get("imgPic")
    imgBack = request.files.get("imgBack")
    
    imgPic, ruta, img1 = obtenerNuevonombre(imgPic)
    imgBack, ruta2, img2 = obtenerNuevonombre(imgBack)
    
    # JSON para la API
    nuevo_usuario = {
        "nombre": firstname,
        "apellido": lastname,
        "email": email,
        "rfc": rfc,
        "curp": curp,
        "fecha_nacimiento": nac,
        "telefono": tel,
        "telefono_emergencia": emTel,
        "calle": call,
        "numero": nCasa,
        "colonia": col,
        "codigo_postal": cp,
        "imagen_usuario_url": imgPic,
        "imagen_fondo_url": imgBack,
        "rol": rol,
        "activo": True,
        "usuario": user,
        "password": password
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    resp = requests.post(f"{API_BASE}/usuarios", json=nuevo_usuario, headers=headers)

    if resp.status_code == 201:
        if img1 and ruta:
            img1.save(ruta)
        if img2 and ruta2:
            img2.save(ruta2)
        return redirect('/usersView')
    else:
        return render_template("pages/createUser.html", message=f"Error creating a new user: {resp.text}")
    

def Delete():
    token = session.get("jwt")
    if not token:
        return redirect("/")

    user_id = request.form["id"] 

    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.delete(f"{API_BASE}/usuarios/{user_id}", headers=headers)

    if resp.status_code == 200:
        return redirect("/usersView")
    else:
        return f"Error al eliminar usuario: {resp.text}"

def UpdatePage():
    token = session.get("jwt")
    if not token:
        return redirect("/")
    
    id = request.form["id"]
    headers = {"Authorization": f"Bearer {token}"}
    user_resp = requests.get(f"{API_BASE}/usuarios/{id}", headers=headers)
    
    if user_resp.status_code == 200:
        usuario = user_resp.json()
        return render_template('pages/updateUser.html', user = usuario)
    else: return "Cant get user"

def Update():
    token = session.get("jwt")
    if not token:
        return redirect("/")
        
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
    activo = request.form["activo"] == "true"

    # Archivos
    imgPic = request.files.get("imgPic")
    imgBack = request.files.get("imgBack")
    
    imgPic, ruta, img1 = obtenerNuevonombre(imgPic)
    imgBack, ruta2, img2 = obtenerNuevonombre(imgBack)
    
    # JSON para la API
    usuario_actualizado = {
        "nombre": firstname,
        "apellido": lastname,
        "email": email,
        "rfc": rfc,
        "curp": curp,
        "fecha_nacimiento": nac,
        "telefono": tel,
        "telefono_emergencia": emTel,
        "calle": call,
        "numero": nCasa,
        "colonia": col,
        "codigo_postal": cp,
        "imagen_usuario_url": imgPic,
        "imagen_fondo_url": imgBack,
        "rol": rol,
        "activo": activo,
        "usuario": user,
        "password": password
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    resp = requests.put(f"{API_BASE}/usuarios/{id}", json=usuario_actualizado, headers=headers)

    if resp.status_code == 200:
        if img1 and ruta:
            img1.save(ruta)
        if img2 and ruta2:
            img2.save(ruta2)
        return redirect("/usersView")
    else:
        return render_template("pages/updateUser.html", message=f"Error al actualizar usuario: {resp.text}")