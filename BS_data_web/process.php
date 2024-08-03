<?php
session_start();

// Check if user is logged in
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header('Location: login.php');
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $arrivalAirport = $_POST['arrivalAirport'];
    $fromDate = $_POST['fromDate'];

    // Validate input
    $validArrivalAirports = ['RHO', 'KGS', 'CHQ'];

    if (!in_array($arrivalAirport, $validArrivalAirports) ||
        !preg_match('/^\d{4}-\d{2}-\d{2}$/', $fromDate)) {
        die('Invalid input');
    }

    // Generate a unique filename
    $fileName = 'BS_LABELS_' . $fromDate . '_' . $arrivalAirport . '.xlsx';
    
    // Get user's Documents folder
    $userProfile = getenv('USERPROFILE');
    $saveDir = $userProfile . '\Documents';
    $savePath = $saveDir . '\\' . $fileName;

    // Execute Python script
    $command = "python \"C:\\xampp\\htdocs\\BS_data_web\\script.py\" \"$arrivalAirport\" \"$fromDate\" \"$savePath\"";
    $output = shell_exec($command);

    if ($output !== null && strpos($output, 'successfully') !== false) {
        // Offer file for download
        if (file_exists($savePath)) {
            header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
            header('Content-Disposition: attachment; filename="' . $fileName . '"');
            header('Content-Length: ' . filesize($savePath));
            header('Cache-Control: private, max-age=0, must-revalidate');
            readfile($savePath);
            exit;
        } else {
            echo "Error: File not found";
        }
    } else {
        echo "Error: " . $output;
    }
} else {
    header('Location: main.html');
    exit;
}
?>