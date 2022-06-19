inhale = window.document.getElementsByClassName(".inhale");

// setInterval(function () {
//   //alert(action);
//   debug;
//   action.innerHTML = "exhale";
// }, 5000),
//   setInterval(function () {
//     //alert(action);
//     debug;
//     action.innerHTML = "inhale";
//   }, 10000);

function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}
setInterval(function () {
  document.getElementById("action").innerHTML = "exhale";
}, 5000),
  setInterval(function () {

    document.getElementById("action").innerHTML = "inhale";
  }, 10000);

  window.onload = function () {
      var fiveMinutes = 60 * 2,
          display = document.querySelector('#time');
      startTimer(fiveMinutes, display);
  };
