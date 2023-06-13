document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var userType = ""; 

    if (email === "" || password === "") {
        alert("Por favor, ingresa tu correo electrónico y contraseña.");
        return;
    }

    var sanitizedEmail = email.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    var sanitizedPassword = password.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
 
    if (sanitizedEmail === "cliente@cuchau.com" && sanitizedPassword === "cliente123") {
        userType = "cliente";
    } else if (sanitizedEmail === "mecanico@cuchau.com" && sanitizedPassword === "mecanico123") {
        userType = "mecanico";
    } else if (sanitizedEmail === "admin@cuchau.com" && sanitizedPassword === "admin123") {
        userType = "administrador";
    } else {
        alert("Correo electrónico o contraseña incorrectos.");
        return;
    }

    if (userType === "cliente") {
        window.location.href = "Index.html";
    } else if (userType === "mecanico") {
        window.location.href = "IndexM.html";
    } else if (userType === "administrador") {
        window.location.href = "IndexA.html";
    }
});
