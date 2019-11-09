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

    <div class="box1">
      <h2> The current time: </h2>
      <div class="time-view" id="time_js"></div>
    </div>

    </br>

    <div class="box1">
      <p> turn the light <strong>on and off</strong>: </p>

    <?php
      if(isset($_POST['newstate'])){
        $new = $_POST['newstate'];
        if($new=='0'){
          exec("python3 python_scripts/turn_light_off.py");
          sleep(3);
        }
        elseif ($new=='1') {
          exec("python3 python_scripts/turn_light_on.py");
          sleep(3);
          }
      }
      $light_status = exec("python3 python_scripts/get_light_status.py");
      #echo $light_status;
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
  </br>
    <div class="p-box">
      <img id="BulbImage" />
    </div>
  </br>
    </div>

  </br>

    <div class="box1">
    <p> set the time to wake up: </p>


    <?php
    #session_start();
    $alarm_set = exec("env/bin/python3 python_scripts/get_alarm_status.py");
    #echo $alarm_set;
    if(isset($_POST['alarm_state'])){
      $new_alarm_state = $_POST['alarm_state'];
      if($new_alarm_state == '0'){
        #$pid_alarm = $_SESSION["pid_alarm"];
        #echo $pid_alarm;
        exec("python3 python_scripts/unset_alarm2.py");
        #echo $success;

        #$alarm_set = False;
      }
      elseif($new_alarm_state == '1'){
        $start_time = $_POST['start_time'];
        $alarm_duration = $_POST['alarm_duration'];
        if(empty($start_time) or empty($alarm_duration)){
          echo "Atart time or alarm duration is not set properly!";
        }
        else{
        echo "Alarm starts at: ";
        echo $start_time;
        echo "<p></br>";
        echo "Alarm will take minutes: ";
        echo $alarm_duration;
        echo "<p></br>";
        exec("env/bin/python3 python_scripts/set_alarm2.py $start_time $alarm_duration");
        #exec("python3 python_scripts/scratch.py");
        #$_SESSION["pid_alarm"] = $pid_alarm;
        #echo $pid_alarm;
        #$alarm_set = True;
      }}
    }


    if($alarm_set == "False" or $alarm_set == False){
      echo "<p>No alarm set";
      echo "<p><form action='index.php' method='POST'>
              <div class='my-form'>
                <label> Alarm Time </label>
                <input type='time' name = 'start_time' placeholder='06:00 AM'>
              </div>
              <div class='my-form'>
                <label> Alarm Duration </label>
               <input type='number' name='alarm_duration' min='1' max='30'>
              <p></br>
              <input type='hidden' name='alarm_state' value='1'>
              <input class=button type='submit' value='SET ALARM'>
              </form>";
    }
    else{
      echo "<p>Alarm set at $alarm_set";
      echo "<p><form action='index.php' method='POST'>
              <input type='hidden' name='alarm_state' value='0'>
              <input class=button type='submit' value='UNSET_ALARM'>
              </form>";
    }

    ?>
  </br>
    <div class="p-box">
      <img id="AlarmImage" />
    </div>
  </br>

    </div>

  </br>



  <div>
    <a href="process.php" > Click here to change the COLOR </a>
  </div>
</br>
</br>

  <!--<script src="js/main.js"> </script>-->
  <script src="js/time.js"> </script>
  <script>
  var light_status_js = "<?php echo $light_status ; ?>";
  </script>
  <script src="js/change_light_image.js"> </script>
  <script>
  var alarm_status_js = "<?php echo $alarm_set ; ?>";
  </script>
  <script src="js/change_alarm_image.js"> </script>




</body>


</html>
