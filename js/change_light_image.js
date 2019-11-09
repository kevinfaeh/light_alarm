//var this_js_script = $('script[src*=change_image]');
//console.log(light_status_js);
function changeLightImage() {
    //var this_js_script = $('script[src*=change_image]');
    //light_status_js = this_js_script.attr('data-variable');
    //var light_status_js = "<?php echo $light_status ; ?>";
    var test = "test";

    var bulb_image = document.getElementById('BulbImage');
    if (light_status_js == "True"){
      console.log("light on");
      bulb_image.src = "images/light-on_small.jpg";
    }
    else{
      console.log("light off");
      bulb_image.src = "images/light-off_small.jpg";
    }

}
changeLightImage();
