<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OXXO Planograms</title>
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,300,0..1,-25&icon_names=arrow_warm_up,close,error,inventory_2,person,published_with_changes,shelves,store" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
    <link rel="stylesheet" href="../css/defaults.css">
    <link rel="stylesheet" href="../css/admin.css">



</head>

<body>
    <header>
        <a href="admin.php" class="logo">
            <img src="../assets/images/Oxxo_Logo.svg.png" alt="">
        </a>

        <span class="material-symbols-rounded"> person </span>
        <h3 class="pt-3 pe-5">
            Pedro Paramo
        </h3>
        <span class="material-symbols-rounded"> store </span>
        <h3 class="pt-3">
            10XA00841
        </h3>
    </header>
    <div class="col-12 p-5 row">
        <div class="col-md-7">
            <h3 style="color: #7A7A7A;">Notificaciones
            </h3>
            <div class="notifications-container">

            </div>
            <br><br>
            <div class="row m-0 m-0 mt-md-5">
                <div class="col-md-8">
                    <div class="card" style="background-color:#BB2C2C;border: none;">
                        <div class="card-body row">
                            <div class="col-5 mx-auto">
                                <h4 class="text-center pb-2">Rendimiento de acomodo promedio</h4>
                                <div class="progress-circle mx-auto" data-percentage="75">
                                    <svg viewBox="0 0 100 100">
                                        <circle class="bg" cx="50" cy="50" r="45" />
                                        <circle class="fg" cx="50" cy="50" r="45" />
                                    </svg>
                                    <div class="percentage-text">75%</div>
                                </div>
                            </div>
                            <div class="col-5 mx-auto">
                                <h4 class="text-center pt-3">Ultimo análisis hace</h4>
                                <div class="last-hour">

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-7 col-md-4 mt-5 mt-md-0 mx-auto">
                    <button class="btn-inventary py-3">
                        <span class="material-symbols-rounded">inventory_2</span>
                        Inventario
                    </button>
                </div>
            </div>
        </div>
        <div class="col-md-4 ms-auto">
            <h3 style="color: #7A7A7A;">Anaqueles</h3>
            <div class="anaqueles-container">

            </div>
        </div>
</body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO"
    crossorigin="anonymous"></script>
<script src="../assets/frameworks/jquery/jquery-3.7.1.min"></script>
<script src="../js/admin.js"></script>

</html>