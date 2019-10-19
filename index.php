<!DOCTYPE html>
<html>

<head>
  <title> Light Control </title>
  <link rel="stylesheet" type="text/css"
  href="css/style.css">
</head> <!-- a comment -->

<body>
  <div class="container">
    <h1> Here you can control the lights </h1>
    <h2> The current time: </h2>
    <?php
      echo date("j.n.Y H:i", time());
     ?>
    <div class="box1">
      <p> turn the light <strong>on and off</strong> </p>
    </div>
    <?php
      if(isset($_POST['newstate'])){
        $new = $_POST['newstate'];
        if($new=='0'){
          exec("python3 light_alarm/turn_light_off.py");
          sleep(3);
        }
        elseif ($new=='1') {
          exec("python3 light_alarm/turn_light_on.py");
          sleep(3);
          }
      }
      $light_status = exec("python3 light_alarm/get_light_status.py");
      echo $light_status;
      if($light_status == 'False'){
        echo "<p>The light is OFF.";
        echo "<p><form action='index.php' method='POST'>
                <input type='hidden' name='newstate' value='1'>
                <input class=button type='submit' value='LED ON'>
                </form>";
      }
      else{
        echo "<p>The light is ON.";
        echo "<p><form action='index.php' method='POST'>
                <input type='hidden' name='newstate' value='0'>
                <input class=button type='submit' value='LED OFF'>
                </form>";
      }

    ?>
    <p> try the <em>voice module</em> </p>
    <p> set the time to wake up </p>

    <form action="process.php" method="POST">
      <div class="my-form">
          <label> First Name </label>
          <input type="text" name = "first-name">
      </div>
      <div class="my-form">
          <label>  Alarm </label>
            <input type="time" name = "alarmtime" placeholder="06:30 AM">
      </div>
        <input class=button type="submit" name="set time" value="set time">
    </form>
  </br>
  <div class="p-box">
  </div>

  </div>

</body>


</html>
