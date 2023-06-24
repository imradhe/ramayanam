<?php
// Read the JSON data from the file
$jsonData = file_get_contents('slokas/'.$_GET["kanda"].'.'.$_GET["sarga"].'.json');

// Convert JSON data to array
$slokas = json_decode($jsonData, true);

// Display the JSON data
foreach ($slokas as $sloka) {
    echo "Script: " . $sloka['script'] . "<br>";
    echo "Kanda: " . $sloka['kanda'] . "<br>";
    echo "Sarga: " . $sloka['sarga'] . "<br>";
    echo "Sloka: " . $sloka['sloka'] . "<br>";
    echo "Description: " . $sloka['description'] . "<br>";
    echo "Text: " . $sloka['text'] . "<br>";
    echo "Transliteration: " . $sloka['transliteration'] . "<br>";
    echo "Translation: " . $sloka['translation'] ."<br>";
    echo "Source: <a href='" . $sloka['source'] . "'>".$sloka['source']."</a> <br><br><br><br>";
}
?>
