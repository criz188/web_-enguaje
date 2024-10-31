// scrip.js o script.js

document.addEventListener("DOMContentLoaded", function() {
    const palabrasFormales = ["palabraFormal1", "palabraFormal2"]; // Agrega tus palabras formales
    const palabrasInformales = ["palabraInformal1", "palabraInformal2"]; // Agrega tus palabras informales
    const palabrasGroserias = ["groseria1", "groseria2"]; // Agrega tus groserías

    const contenedorTexto = document.getElementById("highlighted-text");
    let texto = contenedorTexto.innerHTML;

    // Función para resaltar palabras
    function resaltarPalabras(palabras, clase) {
        palabras.forEach(palabra => {
            const regex = new RegExp(`\\b(${palabra})\\b`, 'gi'); // Coincide con palabras completas
            texto = texto.replace(regex, `<span class="${clase}">$1</span>`);
        });
    }

    // Resaltar cada categoría
    resaltarPalabras(palabrasFormales, 'formal');
    resaltarPalabras(palabrasInformales, 'informal');
    resaltarPalabras(palabrasGroserias, 'groseria');

    // Actualizar el contenedor con el texto resaltado
    contenedorTexto.innerHTML = texto;
});