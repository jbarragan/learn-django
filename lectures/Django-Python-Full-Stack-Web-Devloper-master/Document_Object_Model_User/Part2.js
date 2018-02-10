var p = document.querySelector("p");

console.log(p.textContent);

p.textContent = "No format content";

p.innerHTML = "<strong>Bold content</strong>";

var special = document.querySelector("#special");
var specialA = special.querySelector("a");

console.log(specialA.getAttribute("href"));

specialA.setAttribute("href", "https://amazon.com");
