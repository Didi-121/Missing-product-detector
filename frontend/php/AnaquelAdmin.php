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
	<link rel="stylesheet" href="../css/anaquelAdmin.css">
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

	<div class="col-md-12 row m-0" style="height: 100%;">
		<div class="col-md-7 m-auto rounded" style="background-color: white;">
			<canvas id="lineChart"></canvas>
		</div>
		<div class="col-md-4 mt-5">
			<h3 class="mb-3">Estadísticas</h3>
			<div class="porcentajes px-5">
			</div>
		</div>
	</div>

	<script src="../assets/frameworks/jquery/jquery-3.7.1.min"></script>

	<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
	<script>/*
$.ajax({
type: "POST",
url: "processors/getAnaquelPercentage.php",
data: JSON.stringify({ id: 1 }),
dataType: "json",
success: function (response) {
console.log(response);
var allData = [];
var years = [];
var months = [];
var days = [];
response.forEach((item) => {
var year = new Date(item.date).getFullYear();
years.push(year);
var month = new Date(item.date).getMonth() + 1;
months.push(month);
var day = new Date(item.date).getDate();
days.push(day);
allData[year][month][day] = item.percentage;
});
var dataProcessed = [];
const uniqueYears = [...new Set(years)];
const uniqueMonths = [...new Set(months)];
const uniqueDays = [...new Set(days)];

uniqueYears.forEach((year) => {
uniqueMonths.forEach((month) => {
let contador  = 0;
let dias = 0;
uniqueDays.forEach((day) => {
if (allData[year][month][day] != undefined) {
dias++;
contador += allData[i][j][k];
} else {
allData[year][month][day] = 0;
}
});
dataProcessed[i][j] = contador / dias;
});
});
var months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
console.log(dataProcessed);
dataProcessed.forEach((item) => {
$(".porcentajes").append("<h1>"+dataProcessed.indexOf(item)+"</h1>")
item.forEach((item2) => {
item2.forEach((item3) => {
$(".porcentajes").append(`
<div class="col-md-12 d-flex justify-content-between">
<h3>`+ months[item2] +`Porcentaje de Coincidencia</h3>
<h3>${item3}%</h3>
</div>
`);
});
});
});
 
}
,error: function (error) {
console.error("Error:", error);
}
});
*/
		$.ajax({
			type: "POST",
			url: "processors/getAnaquelPercentage.php",
			data: JSON.stringify({ id: 1 }),
			dataType: "json",
			success: function (response) {
				console.log(response);
				const allData = {};

				// Agrupar por año, mes, día
				response.forEach((item) => {
					const date = new Date(item.date);
					const year = date.getFullYear();
					const month = date.getMonth(); // 0–11
					const day = date.getDate();

					if (!allData[year]) allData[year] = {};
					if (!allData[year][month]) allData[year][month] = {};
					allData[year][month][day] = item.percentage;
				});

				const dataProcessed = {};
				const monthsNames = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

				for (const year in allData) {
					dataProcessed[year] = {};
					for (const month in allData[year]) {
						let total = 0;
						let dias = 0;
						for (const day in allData[year][month]) {
							total += allData[year][month][day];
							dias++;
						}
						dataProcessed[year][month] = (total / dias).toFixed(2);
					}
				}

				console.log("Data procesada:", dataProcessed);

				// Mostrar en HTML
				for (const year in dataProcessed) {
					$(".porcentajes").append(`<div class="year-statistics"></div>`);
					const yearStatistics = $(".porcentajes").children().last();
					yearStatistics.append(`<h2>Año ${year}</h2>`);
					for (const month in dataProcessed[year]) {
						const mesNombre = monthsNames[month];
						const porcentaje = dataProcessed[year][month];
						yearStatistics.append(`
		  <div class="col-md-12 d-flex justify-content-between">
			  <h3><b>${mesNombre}</b> - Porcentaje de Coincidencia</h3>
			  <h3>${porcentaje}%</h3>
		  </div>
		`);
					}
					yearStatistics.append(`<div class="thin-bar"></div>`);
				}
				const ctx = document.getElementById('lineChart');

				new Chart(ctx, {
					type: 'line',
					data: {
						labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
						datasets: [{
							label: 'Coincidencia Real vs Planograma',
							data: [dataProcessed[2025][4], dataProcessed[2025][3], dataProcessed[2025][2], dataProcessed[2025][1], dataProcessed[2025][0]], // tus valores en eje Y
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

			},
			error: function (error) {
				console.error("Error:", error);
			}
		});
	</script>
</body>

</html>