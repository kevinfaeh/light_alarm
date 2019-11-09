function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

var dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
function startTime() {
  var today = new Date();
  var date = today.getDate();
  var day = dayNames[today.getDay()];
  var year = today.getFullYear();
  var month = months[today.getMonth()];
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  // add a zero in front of numbers<10
  m = checkTime(m);
  s = checkTime(s);
  //console.log(day + " " + date + " " + month + " " + year + " " + h + ":" + m + ":" + s);
  var element = document.getElementById('time_js');
  element.innerHTML = day + " " + date + " " + month + " " + year + " " + h + ":" + m + ":" + s;
  //document.getElementById('time_js').innerHTML = h + ":" + m + ":" + s;
  t = setTimeout(function() {
    startTime()
  }, 500);
}
startTime();
