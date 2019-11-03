var this_js_script = $('script[src*=change_image]');
function changeImage() {
    var this_js_script = $('script[src*=change_image]');
    light_status_js = this_js_script.attr('data-variable');
    var test = "test";
    console.log(light_status_js);
    console.log(test);

    if (light_status_js == "True"){
      document.getElementById("BulbImage").src == "images/light-on.jpg";
    }
    else{
      document.getElementById("BulbImage").src == "images/light-off.jpg";
    }

}
changeImage();
