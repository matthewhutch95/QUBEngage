<?php

$url = 'http://sort.40112152.qpc.hal.davecutting.uk/?item_1=Lecture%20sessions&attendance_1=2&item_2=Lab%20sessions&attendance_2=2&item_3=Support%20sessions&attendance_3=2&item_4=Canvas%20activities&attendance_4=2';

$response = file_get_contents($url);

if ($http_response_header[0] === 'HTTP/1.1 200 OK') {
    echo "HTTP status is 200. Test Passed.\n";
} else {
    echo "HTTP status is not 200. Test Failed.\n";
    echo "HTTP status: " . $http_response_header[0] . "\n";
    echo "Response: " . $response . "\n";
}


require 'functions.inc.php';
$items = ['Lecture sessions', 'Lab sessions', 'Support sessions', 'Canvas activities'];
$attendances = [10, 5, 8, 3];

$sortedAttendance = getSortedAttendance($items, $attendances);

// Echo the sorted attendance
echo "Sorted Attendance:\n";
foreach ($sortedAttendance as $item) {
    echo $item['item'] . ' - ' . $item['attendance']  . "\n";
}
echo "\n";

$expected = "Sorted Attendance:\n"
    . "Lecture sessions - 10\n"
    . "Support sessions - 8\n"
    . "Lab sessions - 5\n"
    . "Canvas activities - 3\n";

echo "Test passed if output is:\n " . $expected;