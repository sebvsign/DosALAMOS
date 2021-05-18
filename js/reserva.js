/*agrego las const para ejecutar validaciones */
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

alert("Bienvenido");
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    //toggle del nav
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
    });

    //animacion de los links
    navLinks.forEach((link, nav) => {
        link.style.animation = 'navLinkFade 0.5 ease forwards ${ nav / 7 + 2}s';
    });
}

navSlide();

const expresiones = {
    rutV: /^[0-9]+[-|‐]+[0-9kK]$/
  
}

const validarFormulario = (e) => {
	switch(e.target.name){
        case "paciente":

        break;
        case "amaterno":
            console.log()
        break;
        case "apaterno":

        break;
        case "rut":

        break;
        case "fecha":

        break;
        case "hora":

        break;
    }
}

/* validaciones en formulario  */
inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
});