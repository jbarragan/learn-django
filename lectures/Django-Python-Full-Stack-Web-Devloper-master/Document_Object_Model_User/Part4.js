var tds = document.querySelectorAll("td");
var symbols = " XO";

tds.forEach(
  function(td){
    console.log(`${td.parentNode.rowIndex}, ${td.cellIndex}`);
    td.addEventListener("click", function() {
      var index = symbols.indexOf(td.textContent);
      if( index === 2) this.textContent = "";
      else this.textContent = symbols[index+1];
    });
  });

var reset_button = document.querySelector("#button_reset");
reset_button.addEventListener("click", function() {
  tds.forEach(function(td){
    td.textContent = "";
  });
});
