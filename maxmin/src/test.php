<?php

$url = 'http://maxmin.40112152.qpc.hal.davecutting.uk/?item_1=Lecture%20sessions&attendance_1=2&item_2=Lab%20sessions&attendance_2=2&item_3=Support%20sessions&attendance_3=2&item_4=Canvas%20activities&attendance_4=2';

$response = file_get_contents($url);

if ($http_response_header[0] === 'HTTP/1.1 200 OK') {
    echo "HTTP status is 200. Test Passed.\n";
} else {
    echo "HTTP status is not 200. Test Failed.\n";
    echo "HTTP status: " . $http_response_header[0] . "\n";
    echo "Response: " . $response . "\n";
}


require 'functions.inc.php';
$items = ['Lecture', 'Lab', 'Support', 'Canvas'];
$attendances = [10, 5, 8, 3];
$res = getMaxMin($items, $attendances);
echo "Test passed if max item is Lecture with 10 as value: " . $res[0] . "\n";
echo "Test passed if Min item is Canvas with 3 as value: " . $res[1] . "\n";