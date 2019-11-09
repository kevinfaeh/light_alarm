function changeAlarmImage() {
    var alarm_image = document.getElementById('AlarmImage');
    if (alarm_status_js == "False"){
      console.log("alarm off");
      alarm_image.src = "images/no-alarm.jpg";
    }
    else{
      console.log("alarm on");
      alarm_image.src = "images/alarm-on.jpg";
    }

}
changeAlarmImage();
