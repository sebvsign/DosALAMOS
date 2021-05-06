function validarFormulario(){

    var elemento = document.forms["formulario_registro"]["micheckbox"].checked;
    if(elemento == true){
        document.getElementById("info").innerHTML = "Gracias por aceptar!!";
        document.forms["formulario_registro"].reset();
        document.forms["formulario_registro"].addEventListener(alert("Enviado"));
        return false;
    }
    else{
        document.getElementById("info").innerHTML = "Favor lea y seleccione la aceptación terminos";
        return false;
    }
}

window.onload = function(){
	var toggleButton = document.querySelector('.toggleButton').addEventListener('click',function(){
		var border = document.querySelector('.border').classList.toggle("activeBorder");
		var button = document.querySelector('.button').classList.toggle("active");
		var day = document.querySelector('.day').classList.toggle("night");
	})
}