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

document.querySelector("#submit").addEventListener("click", e => {
    e.preventDefault();
  
    //INGRESE UN NUMERO DE WHATSAPP VALIDO AQUI:
    let telefono = "979828107";
  
    let paciente = document.querySelector("#paciente").value;
    let rut = document.querySelector("#rut").value;
    let fecha = document.querySelector("#fecha").value;
    let hora = document.querySelector("#hora").value;
    let empleado = document.querySelector("#empleado").value;
    let servicio = document.querySelector("#servicio").value;
    let resp = document.querySelector("#respuesta");
  
    resp.classList.remove("fail");
    resp.classList.remove("send");
  
    let url = `https://api.whatsapp.com/send?phone=${telefono}&text=
          *_MI NEGOCIO_*%0A
          *Reservas*%0A%0A
          *¿Cuál es tu nombre?*%0A
          ${paciente}%0A
          *Indique su rut cumpleto sin puntos con guion*%0A
          ${rut}%0A
          *Especialidad*%0A
          ${empleado}%0A
          *¿Cuál es el medico que desea?*%0A
          ${servicio}%0A
          *Indica la fecha de tu reserva*%0A
          ${fecha}%0A
          *Indica la hora de tu reserva*%0A
          ${hora}`;
  
    if (paciente === "" || fecha === "" || hora === "") {
      resp.classList.add("fail");
      resp.innerHTML = `Faltan algunos datos, ${paciente}`;
      return false;
    }
    resp.classList.remove("fail");
    resp.classList.add("send");
    document.forms["formulario__submit"].addEventListener(alert("Enviado"));
    
    resp.innerHTML = `Se ha enviado tu reserva, ${paciente}`;
  
    window.open(url);
  });