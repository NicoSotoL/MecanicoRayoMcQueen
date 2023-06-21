//validacion Login
function validateLoginForm() {
    var email = document.forms["loginForm"]["email"].value;
    var password = document.forms["loginForm"]["password"].value;

    if (email == "") {
      alert("Por favor ingresa tu correo electrónico");
      return false;
    }

    if (password == "") {
      alert("Por favor ingresa tu contraseña");
      return false;
    }
    var passwordRegex = /^(?=.*\d)(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?])[a-zA-Z0-9!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]+$/;
if (!passwordRegex.test(password)) {
  alert("La contraseña debe contener al menos un número y un carácter especial");
  return false;
}

window.location.href = "{% url 'index'%}";

return true;
}


//contador
var contadorElemento = document.getElementById('contador');

function actualizarContador(numeroPersonas) {
  contadorElemento.textContent = numeroPersonas;
}

setInterval(function () {
  var numeroOnline = Math.floor(Math.random() * 30) + 1;
  actualizarContador(numeroOnline);
}, 1000);


//lista de sugerencias
var campoBusqueda = document.getElementById('campo-busqueda');
var listaSugerencias = document.getElementById('lista-sugerencias');

campoBusqueda.addEventListener('input', function () {
  var consulta = campoBusqueda.value;

  var sugerencias = obtenerSugerencias(consulta);

  mostrarSugerencias(sugerencias);
});

function mostrarSugerencias(sugerencias) {
  listaSugerencias.innerHTML = '';

  sugerencias.forEach(function (sugerencia) {
    var sugerenciaElemento = document.createElement('li');
    sugerenciaElemento.textContent = sugerencia;

    sugerenciaElemento.addEventListener('click', function () {
      campoBusqueda.value = sugerencia;
      listaSugerencias.innerHTML = '';
    });

    listaSugerencias.appendChild(sugerenciaElemento);
  });

  listaSugerencias.style.width = campoBusqueda.offsetWidth + 'px';
}

document.addEventListener('click', function (event) {
  if (!campoBusqueda.contains(event.target)) {
    listaSugerencias.innerHTML = '';
  }
});

function obtenerSugerencias(consulta) {
  var sugerencias = [];

  if (consulta === 'motor') {
    sugerencias = ['autismo', 'asperger', 'funao'];
  } else if (consulta === 'choche') {
    sugerencias = ['esto es una falta de respeto', 'me dicen waton', 'lo editan con editores de video como camtasia studio, adobe premier'];
  } else if (consulta === 'mecanicos') {
    sugerencias = ['pastero', 'cocainomano', 'weko'];
  }

  return sugerencias;
}
