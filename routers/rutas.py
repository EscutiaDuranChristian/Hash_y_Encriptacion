from controllers import root, login, logout, UsersView, form_user, create_user, Delete, UpdatePage, Update, verUsuario

def registrar_rutas(app):
    @app.route('/')
    def ruta_inicio():
        return root()

    @app.route("/login", methods=["POST"])
    def ruta_login():
        return login()
    
    @app.route("/logout")
    def ruta_logout():
        return logout();

    @app.route('/usersView')
    def ruta_vista_usuarios():
        return UsersView()

    @app.route("/createuser")
    def ruta_form_user():
        return form_user()
    
    @app.route("/createuser", methods=["POST"])
    def ruta_create_user():
        return create_user()
    
    @app.route("/delete", methods=['POST'])
    def ruta_delete():
        return Delete()
    
    @app.route("/update", methods=['POST'])
    def ruta_update_page():
        return UpdatePage()
    
    @app.route("/updateuser", methods=['POST'])
    def ruta_update():
        return Update()
    
    @app.route("/viewUser", methods=['POST'])
    def ruta_view_user():
        return verUsuario()