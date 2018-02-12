var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

headOne.addEventListener("mouseover", function () {
  headOne.textContent = "Mouse Currently Over";
  headOne.style.color = "red";
});

headOne.addEventListener("mouseout", function () {
  headOne.textContent = "Hover Over me";
  headOne.style.color = "black";
});

headTwo.addEventListener("click", function() {
  this.textContent = "Clicked On";
  this.style.color = "blue";
})

headThree.addEventListener("dblclick", function() {
  this.textContent = "Double Clicked On";
  this.style.color = "green";
})
