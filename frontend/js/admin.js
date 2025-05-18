$(document).ready(function () {


    fetch('../php/processors/getNotifications.php', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
        .then(res => res.json())
        .then(function (data) {
            data.forEach(notification => {
                const fecha = new Date(notification.date);
                const today = new Date();
                const months = [
                    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
                ];
                function formatearHoraAMPM(fecha) {
                    const horas = fecha.getHours();
                    const minutos = fecha.getMinutes().toString().padStart(2, '0');
                    const ampm = horas >= 12 ? 'pm' : 'am';
                    const hora12 = horas % 12 || 12;
                    return `${hora12}:${minutos} ${ampm}`;
                }
                if (fecha.getDay() == today.getDay() && fecha.getMonth() == today.getMonth() && fecha.getFullYear() == today.getFullYear()) {
                    notification.date = "Hoy " + formatearHoraAMPM(fecha);
                } else if (fecha.getDay() == today.getDay() - 1 && fecha.getMonth() == today.getMonth() && fecha.getFullYear() == today.getFullYear()) {
                    notification.date = "Ayer " + formatearHoraAMPM(fecha);
                } else if (fecha.getFullYear() == today.getFullYear()) {
                    notification.date = fecha.getDate() + " de " + (months[fecha.getMonth()]);
                } else {
                    notification.date = fecha.getDate() + " de " + (months[fecha.getMonth()]) + " del " + fecha.getFullYear();
                }
                $('.notifications-container').append(`
            <div class="notification ${notification.type}" data-id="${notification.id}">
                <span class="material-symbols-rounded main-icon pe-3"> ${notification.icon} </span>
                <div class="info">
                    <div class="head">
                        <h4 class="pt-1">${notification.title}</h4>
                        <span class="ps-2"> ${notification.date}</span>
                    </div>
                    <p class="m-0">${notification.content}</p>
                </div>
                <span class="material-symbols-rounded close ms-auto"> close </span>
            </div>
        `);

            });
            $('.close').click(function () {
                const notificationId = $(this).parent().data('id');
                fetch('../php/processors/deleteNotification.php', {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ id: notificationId })
                })
                    .then(res => res.json())
                    .then(data => {
                        if (data.success) {
                            $(`.notification[data-id="${notificationId}"]`).remove();
                        } else {
                            console.error('Error deleting notification:', data.error);
                        }
                    })
                    .catch(err => console.error(err));
            });
        })
        .catch(err => console.error(err));
    function diferenciaConAhora(fechaStr, reduced = false) {
        const ahora = new Date();
        const fecha = new Date(fechaStr);
        const msDiff = Math.abs(ahora - fecha);

        const segundos = Math.floor(msDiff / 1000);
        const minutos = Math.floor(segundos / 60);
        const horas = Math.floor(minutos / 60);
        const dias = Math.floor(horas / 24);
        const meses = Math.floor(dias / 30); // aproximado
        if (!reduced) {
            if (meses >= 1) return `${meses} mes${meses > 1 ? 'es' : ''}`;
            if (dias >= 1) return `${dias} día${dias > 1 ? 's' : ''}`;
            if (horas >= 1) return `${horas} hora${horas > 1 ? 's' : ''}`;
            if (minutos >= 1) return `${minutos} minuto${minutos > 1 ? 's' : ''}`;
            return `${segundos} segundo${segundos > 1 ? 's' : ''}`;
        } else {
            if (meses >= 1) return `${meses} m`;
            if (dias >= 1) return `${dias} día${dias > 1 ? 's' : ''}`;
            if (horas >= 1) return `${horas} h}`;
            if (minutos >= 1) return `${minutos} min}`;
            return `${segundos} s`;
        }
    }

    $.ajax({
        type: "GET",
        url: "../php/processors/getAnaquelesPercentage.php",
        dataType: "json",
        success: function (response) {
            response[0].date
            $(".last-hour").text(diferenciaConAhora(response[0].date, true));

            let total = 0;
            let average = 0;
            for (let i = 1; i < response.length; i++) {
                for (let j = 0; j < response.length; j++) {
                    const element = response[j];

                    var diferencia = diferenciaConAhora(element.date);
                    if (element.anaquel_id == i) {
                        total += 1;
                        average += element.percentage;
;                        $(".anaqueles-container").append(`
                        <a href="../php/AnaquelAdmin.php?id=`+ element.anaquel_id + `">
                            <div class="anaquel">
                                <span class="material-symbols-rounded main-icon"> shelves</span>
                                <div class="data me-5">
                                    <h4 class="m-0">Anaquel `+ element.anaquel_id + `</h4>
                                    <p class="m-0">Ultimo análisis hace <span class="primary">`+ diferencia + `</span></p>
                                </div>
                                <div class="percentage">
                                    `+ element.percentage + "%" + `
                                </div>
                            </div>
                        </a>
                        `);
                        $(".anaqueles-container").append("<div class='thin-bar'></div>");
                        break;
                    }
                }
            }
            $(".progress-circle").data("percentage", Math.round(average / total));
            drawCircle();
        },
        error: function (error) {
            console.error("Error:", error);
        }
    });

    function drawCircle() {
        $(".progress-circle").each(function () {
            const percent = $(this).data("percentage");
            const circle = $(this).find(".fg");
            const radius = circle.attr("r");
            const circumference = 2 * Math.PI * radius;

            circle.css({
                "stroke-dasharray": circumference,
                "stroke-dashoffset": circumference
            });

            setTimeout(() => {
                const offset = circumference - (percent / 100) * circumference;
                circle.css("stroke-dashoffset", offset);
            }, 100);
            $(".percentage-text").text(`${percent}%`);
        });
     };
});
