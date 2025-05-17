var admin_user = "Pedro Paramo";
var admin_password = "12345678";
var common_user = "Juan Rulfo";
var common_password = "87654321";

document.getElementById("login-button").addEventListener("click", () => login());


function login() { 
    var user = document.getElementById("user").value;
    var password = document.getElementById("password").value;

    if (user === admin_user && password === admin_password) {
        window.location.href = "frontend/html/admin.html";
    } else if (user === common_user && password === common_password) {
        window.location.href = "frontend/html/usuario.html";
    } else {
        alert("Invalid username or password");
    }
}