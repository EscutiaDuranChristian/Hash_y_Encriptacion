<?php include "header.php"; ?>

<div class="container">
    <div class="row">
        <div class="col-md-7">
            <!-- Picture -->
            <?php if (!empty($_SESSION['fondo'])): ?>
                <img class="banner" src="static/img/<?php echo $_SESSION['fondo']; ?>">
            <?php else: ?>
                <img class="banner" src="static/img/defaultBack.png">
            <?php endif; ?>

            <?php if (!empty($_SESSION['pic'])): ?>
                <img class="card-img-top profile" src="static/img/<?php echo $_SESSION['pic']; ?>" alt="Title" />
            <?php else: ?>
                <img class="card-img-top profile" src="static/img/defaultPic.png" alt="Title" />
            <?php endif; ?>
        </div>

        <div class="col-md-5">
            <!-- Información de usuario -->
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Firstname: <?php echo $_SESSION['firstname']; ?></h4>
                    <h4 class="card-title">Lastname: <?php echo $_SESSION['lastname']; ?></h4>
                    <h4 class="card-title">Address:</h4>
                    <p class="card-text">
                        <?php echo $_SESSION['streat'] . " " . $_SESSION['number'] . " " . $_SESSION['col']; ?>
                    </p>
                    <h4 class="card-title">Postal Code: <?php echo $_SESSION['cp']; ?></h4>
                </div>
            </div>
        </div>
    </div>
</div>

<hr style="width: 100%; border: 30px 1px black;">
<center><h3>Usuarios:</h3></center>

<!-- Lista usuarios -->
<div class="container">
    <div class="row">
        <div class="col-4">
            <?php foreach ($users as $user): ?>
                <?php if (!empty($user['imagen_fondo_url'])): ?>
                    <div class="card" style="text-align: center; align-items: center; width: 100%;
                         background-image: url(static/img/<?php echo $user['imagen_fondo_url']; ?>);">
                <?php else: ?>
                    <div class="card" style="text-align: center; align-items: center; width: 100%;
                         background-image: url(static/img/defaultBack.png);">
                <?php endif; ?>

                <?php if (!empty($user['imagen_usuario_url'])): ?>
                    <img class="card-img-top" src="static/img/<?php echo $user['imagen_usuario_url']; ?>" alt="Title" style="width: 30%;" />
                <?php else: ?>
                    <img class="card-img-top" src="static/img/defaultPic.png" alt="Title" style="width: 30%;" />
                <?php endif; ?>

                <div class="card-body">
                    <h4 class="card-title">UserName: <?php echo $user['username']; ?></h4>
                </div>

                <?php if ($_SESSION['rol'] === 'admin'): ?>
                    <!-- Solo admin -->
                    <div class="container" style="margin-left: -5%;">
                        <div class="row">
                            <div class="col-6">
                                <!-- Botón actualizar -->
                                <form action="/update" method="post">
                                    <button type="submit" class="btn btn-outline-success" name="id" value="<?php echo $user['id']; ?>">
                                        Update
                                    </button>
                                </form>
                            </div>
                            <div class="col-6">
                                <!-- Botón borrar -->
                                <form action="/delete" method="post">
                                    <button type="submit" class="btn btn-outline-danger" name="id" value="<?php echo $user['id']; ?>">
                                        Delete
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                <?php endif; ?>
            </div>
            <?php endforeach; ?>
        </div>
    </div>
</div>

<?php if ($_SESSION['rol'] === 'admin'): ?>
    <a class="btn btn-primary" href="/createuser" role="button">Crear usuario</a>
<?php endif; ?>

<?php include "footer.php"; ?>
