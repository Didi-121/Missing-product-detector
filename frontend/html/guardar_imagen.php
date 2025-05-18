<?php
// Recibir datos JSON del frontend
$data = json_decode(file_get_contents("php://input"), true);

if (!$data || !isset($data['imagen']) || !isset($data['nombre'])) {
    http_response_code(400);
    echo json_encode(["error" => "Datos inválidos"]);
    exit;
}

// Obtener datos
$nombre = basename($data['nombre']); // evitar rutas maliciosas
$base64 = $data['imagen'];

// Decodificar y guardar la imagen
$imagen_binaria = base64_decode($base64);
$ruta = "../../backend/cache/" . $nombre;

// Asegurarse que exista el directorio
if (!is_dir("imagenes_guardadas")) {
    mkdir("imagenes_guardadas", 0777, true);
}

// Guardar archivo
if (file_put_contents($ruta, $imagen_binaria)) {
    echo json_encode(["mensaje" => "Imagen guardada", "ruta" => $ruta]);
} else {
    http_response_code(500);
    echo json_encode(["error" => "No se pudo guardar la imagen"]);
}
?>