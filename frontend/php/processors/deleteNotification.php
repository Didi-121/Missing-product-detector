<?php
header("Content-Type: application/json");


$id = json_decode(file_get_contents('php://input'), true)['id'];
if (empty($id)) {
    echo json_encode(['error' => 'ID no proporcionado']);
    exit;
}
try {
    // Usa la ruta absoluta si es necesario
    $db = new PDO('sqlite:/Users/Brian/DataGripProjects/lol/FEMSA.sqlite');

    // Preparar la consulta para eliminar la notificación
    $stmt = $db->prepare("DELETE FROM notifications WHERE id = :id");
    $stmt->bindParam(':id', $id, PDO::PARAM_INT);

    // Ejecutar la consulta
    if ($stmt->execute()) {
        echo json_encode(['success' => 'Notificación eliminada']);
    } else {
        echo json_encode(['error' => 'Error al eliminar la notificación']);
    }
} catch (PDOException $e) {
    echo json_encode(['error' => $e->getMessage()]);
}

?>