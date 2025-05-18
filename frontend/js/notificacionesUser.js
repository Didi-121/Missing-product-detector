const notificaciones = [
  { tipo: "alerta", mensaje: "Revisar Anaquel 1" },
  { tipo: "completo", mensaje: "Anaquel 2 analizado" },
  { tipo: "iniciado", mensaje: "Análisis Anaquel 2" },
  { tipo: "iniciado", mensaje: "Análisis Anaquel 3" }
];

const iconos = {
  alerta: "error",
  completo: "published_with_changes",
  iniciado: "arrow_circle_up"
};

function mostrarNotificaciones(lista) {
  const contenedor = document.querySelector(".notification-box");
  if (!contenedor) {
    console.warn("No se encontró '.notification-box'");
    return;
  }

  contenedor.innerHTML = "";

  lista.forEach(n => {
    const div = document.createElement("div");
    div.classList.add("notification-item", n.tipo);

    let color = "#333";
    if (n.tipo === "alerta") color = "orange";
    else if (n.tipo === "completo") color = "#5A85B1";
    else if (n.tipo === "iniciado") color = "#706CDD";

    const icono = iconos[n.tipo] || "notifications";

    div.innerHTML = `
      <div class="noti-content">
        <span class="material-symbols-outlined noti-icon" style="color: ${color};">
          ${icono}
        </span>
        <strong style="color: ${color}; text-transform: capitalize;">
          ${n.tipo}:
        </strong> ${n.mensaje}
      </div>
    `;

    contenedor.appendChild(div);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  mostrarNotificaciones(notificaciones);

  const toggleBtn = document.getElementById("notificationBtn");
  const panel = document.querySelector(".notification-box");

  if (toggleBtn && panel) {
    toggleBtn.addEventListener("click", () => {
      panel.classList.toggle("visible");
    });

    // Opcional: cerrar al hacer clic fuera
    document.addEventListener("click", (e) => {
      if (!panel.contains(e.target) && !toggleBtn.contains(e.target)) {
        panel.classList.remove("visible");
      }
    });
  }
});