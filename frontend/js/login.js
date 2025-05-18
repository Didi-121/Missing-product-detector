var admin_user = ["Pedro Paramo","Octavio Paz", "Carlos Fuentes"];
var admin_password = "12345678";
var common_users = ["Juan Rulfo","Jorge Luis Borges", "Gabriel Garcia Marquez"];
var common_password = "87654321";


document.getElementById("login-button").addEventListener("click", () => login());


function login() { 
    var user = document.getElementById("user").value;
    var password = document.getElementById("password").value;
    if (admin_user.includes(user) && password === admin_password) {
        window.location.href = "frontend/html/admin.php";
    } else if (common_users.includes(user) && password === common_password) {
        window.location.href = "frontend/html/usuario.php";
    } else {
        alert("Invalid username or password");
    }
}