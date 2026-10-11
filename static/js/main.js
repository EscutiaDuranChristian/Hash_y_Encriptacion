// app.js
const express = require("express");
const session = require("express-session");
const path = require("path");
const multer = require("multer");

const app = express();

// Configuración de sesión
app.use(session({
  secret: "loslicsenciadosrifan",
  resave: false,
  saveUninitialized: true
}));

// Configuración de subida de archivos
const UPLOAD_FOLDER = path.join(__dirname, "static", "img");
const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, UPLOAD_FOLDER),
  filename: (req, file, cb) => {
    const fecha = new Date().toISOString().replace(/[-:.TZ]/g, "");
    const ext = path.extname(file.originalname);
    const base = path.basename(file.originalname, ext);
    cb(null, `${base}_${fecha}${ext}`);
  }
});
const upload = multer({ storage });

// Middleware para formularios
app.use(express.urlencoded({ extended: true }));
app.use(express.static("static"));

// Rutas
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "templates", "index.html"));
});

app.post("/login", (req, res) => {
  const { user, pass } = req.body;
  if (user === "admin" && pass === "123") {
    req.session.user = user;
    req.session.rol = "admin";
    req.session.firstname = "Christian";
    req.session.lastname = "Escutia";
    req.session.streat = "Carrara";
    req.session.number = "120A";
    req.session.col = "Ancona";
    req.session.cp = "38920";
    res.redirect("/usersView");
  } else {
    res.sendFile(path.join(__dirname, "templates", "index.html"));
  }
});

app.get("/usersView", (req, res) => {
  res.sendFile(path.join(__dirname, "templates", "usersView.html"));
});

app.get("/createuser", (req, res) => {
  res.sendFile(path.join(__dirname, "templates", "createUser.html"));
});

app.post("/createuser", upload.fields([{ name: "imgPic" }, { name: "imgBack" }]), (req, res) => {
  const { firstname, lastname, email, rfc, curp, nac, tel, emTel, call, nCasa, col, cp, rol, user, pass } = req.body;
  // Aquí podrías guardar en DB
  res.redirect("/usersView");
});

app.post("/delete", (req, res) => {
  const { id } = req.body;
  // Borrar usuario
  res.redirect("/usersView");
});

app.post("/update", (req, res) => {
  const { id } = req.body;
  // Obtener datos
  res.sendFile(path.join(__dirname, "templates", "updateUser.html"));
});

app.post("/updateuser", upload.fields([{ name: "imgPic" }, { name: "imgBack" }]), (req, res) => {
  const { id, firstname, lastname, email, rfc, curp, nac, tel, emTel, call, nCasa, col, cp, rol, user, pass } = req.body;
  // Actualizar usuario
  res.redirect("/usersView");
});

// Servir CSS e imágenes desde static/
app.use("/css", express.static(path.join(__dirname, "static", "css")));
app.use("/img", express.static(path.join(__dirname, "static", "img")));

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
