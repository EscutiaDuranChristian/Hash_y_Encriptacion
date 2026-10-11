<?php include "header.php"; ?>

<div class="main container">
    <div class="row justify-content-center align-items-center g-2">
        <!-- Form -->
        <div class="col-12 col-md-6">
            <form id="loginForm" action="/updateuser" method="post" enctype="multipart/form-data">
                <!-- Firstname -->
                <div class="mb-3">
                    <label class="form-label">Firstname</label>
                    <input type="text" class="form-control" name="firstname" value="<?php echo $data[1]; ?>" required />
                </div>
                <!-- Lastname -->
                <div class="mb-3">
                    <label class="form-label">Lastname</label>
                    <input type="text" class="form-control" name="lastname" value="<?php echo $data[2]; ?>" required />
                </div>
                <!-- Email -->
                <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" class="form-control" name="email" value="<?php echo $data[3]; ?>" placeholder="abc@mail.com" />
                </div>
                <!-- RFC -->
                <div class="mb-3">
                    <label class="form-label">RFC</label>
                    <input type="text" class="form-control" name="rfc" value="<?php echo $data[4]; ?>" required />
                </div>
                <!-- CURP -->
                <div class="mb-3">
                    <label class="form-label">CURP</label>
                    <input type="text" class="form-control" name="curp" value="<?php echo $data[5]; ?>" required />
                </div>
                <!-- Fecha de nacimiento -->
                <div class="mb-3">
                    <label class="form-label">Fecha de nacimiento</label>
                    <input type="date" name="nac" value="<?php echo $data[6]; ?>" min="1920-01-01" max="2026-10-11" required />
                </div>
                <!-- Teléfono -->
                <div class="mb-3">
                    <label class="form-label">Phone number</label>
                    <input type="number" class="form-control" name="tel" value="<?php echo $data[7]; ?>" required />
                </div>
                <!-- Teléfono emergencia -->
                <div class="mb-3">
                    <label class="form-label">Emergency Phone number</label>
                    <input type="number" class="form-control" name="emTel" value="<?php echo $data[8]; ?>" />
                </div>
                <!-- Calle -->
                <div class="mb-3">
                    <label class="form-label">Streat</label>
                    <input type="text" class="form-control" name="call" value="<?php echo $data[9]; ?>" required />
                </div>
                <!-- Número -->
                <div class="mb-3">
                    <label class="form-label">Numero de casa</label>
                    <input type="text" class="form-control" name="nCasa" value="<?php echo $data[10]; ?>" required />
                </div>
                <!-- Colonia -->
                <div class="mb-3">
                    <label class="form-label">Residence</label>
                    <input type="text" class="form-control" name="col" value="<?php echo $data[11]; ?>" required />
                </div>
                <!-- Código postal -->
                <div class="mb-3">
                    <label class="form-label">Postal code</label>
                    <input type="number" class="form-control" name="cp" value="<?php echo $data[12]; ?>" required />
                </div>
                <!-- Imagen usuario -->
                <div class="mb-3">
                    <label class="form-label">User profile picture</label>
                    <input type="file" class="form-control" name="imgPic" />
                </div>
                <!-- Imagen fondo -->
                <div class="mb-3">
                    <label class="form-label">User background picture</label>
                    <input type="file" class="form-control" name="imgBack" />
                </div>
                <!-- Rol -->
                <div class="mb-3">
                    <label class="form-label">Rol</label>
                    <select name="rol">
                        <option value="0" <?php echo ($data[15] == 0 ? "selected" : ""); ?>>Usuario</option>
                        <option value="1" <?php echo ($data[15] == 1 ? "selected" : ""); ?>>Administrador</option>
                    </select>
                </div>
                <!-- Activo -->
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" <?php echo ($data[16] ? "checked" : ""); ?> />
                    <label class="form-check-label">Activo</label>
                </div>
                <!-- User Name -->
                <div class="mb-3">
                    <label class="form-label">User Name</label>
                    <input type="text" class="form-control" name="user" value="<?php echo $data[19]; ?>" required />
                </div>
                <!-- Password -->
                <div class="mb-3">
                    <label class="form-label">Password</label>
                    <input type="password" class="form-control" name="pass" value="<?php echo $data[20]; ?>" required />
                </div>
                <!-- Botón -->
                <div class="d-grid gap-2">
                    <button type="submit" name="id" class="btn btn-primary box-shadow-white" value="<?php echo $data[0]; ?>">
                        Update user
                    </button>
                </div>
            </form>
        </div>

        <!-- Logo -->
        <div class="col-12 col-md-6">
            <img src="static/img/Logo.png" class="Logo box-shadow-white" alt="image desc" />
        </div>
    </div>
</div>

<?php include "footer.php"; ?>
