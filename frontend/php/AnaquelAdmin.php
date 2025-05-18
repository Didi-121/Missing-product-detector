
<?php 
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OXXO Planograms</title>
    <link rel="stylesheet"href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,300,0..1,-25&icon_names=arrow_warm_up,close,error,inventory_2,person,published_with_changes,shelves,store" />
    <link rel="stylesheet" href="../css/defaults.css">
</head>
<body>

<header>
        <img src="../assets/images/Oxxo_Logo.svg.png" alt="">
        <span class="material-symbols-rounded"> person </span>
        <h3 class="pt-3 pe-5">
            Pedro Paramo
        </h3>
        <span class="material-symbols-rounded"> store </span>
        <h3 class="pt-3">
            10XA00841
        </h3>
    </header>
    <div style="width: 50%;">
        <canvas id="lineChart"></canvas>
    </div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const ctx = document.getElementById('lineChart');

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
      datasets: [{
        label: 'Coincidencia Real vs Planograma',
        data: [30, 45, 60, 80, 75], // tus valores en eje Y
        borderColor: '#BB2C2C',
        backgroundColor: 'rgba(187, 44, 44, 0.2)',
        tension: 0.3, // suaviza las curvas
        fill: true,
        pointRadius: 5,
        pointBackgroundColor: '#BB2C2C'
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          max: 100,
          title: {
            display: true,
            text: 'Porcentaje de Coincidencia (%)'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Mes'
          }
        }
      }
    }
  });
  ctx.offsetWidth = 50;
</script>
</body>
</html>