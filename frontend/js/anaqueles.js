
document.addEventListener("DOMContentLoaded", () => {
  const anaqueles = [
    { nombre: "Anaquel Botanas 1", imagen: "../assets/images/anaquel1.png", aviso: "1 día" },
    { nombre: "Anaquel Limpieza 1", imagen: "../assets/images/anaquel2.png", aviso: "2 días" },
    { nombre: "Anaquel 3", imagen: "../assets/images/anaquel1.png", aviso: "1 semana" },
    { nombre: "Anaquel 4", imagen: "../assets/images/anaquel2.png", aviso: "4 semana" }
  ];

  const container = document.getElementById("shelf-container");

  if (container) {
    anaqueles.forEach((anaquel, i) => {
      const section = document.createElement("section");
      section.className = "shelf-card";
      section.innerHTML = `
        <h3>${anaquel.nombre}</h3>
        <img src="${anaquel.imagen}" alt="Anaquel ${i + 1}" class="imagenAnaquel" />
        <div class="recommendation">Se recomienda revisar en <span>${anaquel.aviso}</span></div>
      `;
      container.appendChild(section);
    });
  } else {
    console.warn("No se encontró el contenedor con id 'shelf-container'");
  }
});