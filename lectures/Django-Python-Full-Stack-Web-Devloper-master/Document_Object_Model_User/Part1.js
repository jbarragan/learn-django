
var header = document.querySelector("h1");

function getRandomColor() {
  var letters = "0123456789ABCDEF";
  var color = "#";
  var len = letters.length;
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*len)];
  }
  return color;
}

function changeHeaderColor() {
  var colorInput = getRandomColor();
  header.style.color = colorInput;
}

setInterval("changeHeaderColor()", 500);
