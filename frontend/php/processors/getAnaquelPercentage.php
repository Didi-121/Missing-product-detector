<?php
header("Content-Type: application/json");
$id = json_decode(file_get_contents('php://input'), true)['id'];

if (!isset($id)) {
    echo json_encode(['error' => 'ID not provided']);
    exit;
}

try {
    // Usa la ruta absoluta si es necesario
    $db = new PDO('sqlite:/Users/Brian/DataGripProjects/lol/FEMSA.sqlite');

    // Seleccionar todo
    $stmt = $db->query("SELECT * FROM anaquel_data WHERE anaquel_id = $id ORDER BY date DESC");

    // Obtener los resultados como array asociativo
    $notificaciones = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo json_encode($notificaciones);
} catch (PDOException $e) {
    echo json_encode(['error' => $e->getMessage()]);
}
?>