<!DOCTYPE html>
<!DOCTYPE html>

<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css"> </link>

    <link href="https://cdn.alloyui.com/3.0.1/aui-css/css/bootstrap.min.css" rel="stylesheet"></link>
    <style>
        .label-option {
            display: inline;
            vertical-align: middle;
            margin-left: 5px;
        }
    </style>

    <script src="https://cdn.alloyui.com/3.0.1/aui/aui-min.js" type="text/javascript">
    </script>

</head>

<body>

<div id="wrapper" class="container">
    <h3>HSV palette</h3>

    <div id="hsvPaletteOptions">
        <input type="checkbox" checked id="controls"><label class="label-option" for="controls">Controls</label>
    </div>


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
    <div id="hsvPalette">
      <form action="process.php" method="POST">
      <input id="color" type='text'/ name="selected_color">
      <input class=button type='submit' value='SET COLOR'>
    </form>

    </div>

     <?php
          if(isset($_POST['selected_color'])){
          $color_selected = $_POST["selected_color"];
          echo is_null($color_selected);
          if($color_selected != NULL){
          exec("python3 python_scripts/set_color_hex.py $color_selected");
        }
        }
       ?>

    <div>
      <a href="index.php"> BACK TO MAIN PAGE </a>
    </div>



</div>

<script>

    var color_selected
    YUI({ filter:'raw' }).use(
        'aui-hsv-palette', 'aui-color-palette',
        function(Y) {
            var hsvPalette;

            var controlsCheckbox = Y.one('#controls');

            function createHSVPalette() {
                if (hsvPalette) {
                    hsvPalette.destroy();
                }

                var hsvClass = Y.HSVPalette;

                hsvPalette = new hsvClass(
                    {
                        controls: controlsCheckbox.get('checked'),
                        trigger: '#color',
                      after:{
                        colorChange: function(event){
                          Y.one('#color').val(this.get('rgb'));
                        }
                      }
                    }
                ).render('#hsvPalette');

                hsvPalette.on('selectedChange', function (event) {
                    Y.log('via selected: ' + hsvPalette.get('selected'));

                    Y.log('via new val: ' +event.newVal);

                    //Y.one('#color').val(event.newVal);
                    Y.one('#color').val(event.newVal);


                });
            }

            controlsCheckbox.after('change', createHSVPalette);

            createHSVPalette();
        }
    );

</script>

</body>
</html>
