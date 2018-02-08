var first_name = prompt("First Name:");
var last_name = prompt("Last Name:");
var age = prompt("Age:");
var stature = prompt("Stature in cm.:");
var pet = prompt("Pet's Name:");

alert("Thanks for the information.");

if(
  first_name && first_name.length > 0 &&
  last_name && last_name.length > 0 &&
  first_name[0] === last_name[0] &&
  age && !isNaN(age) && age > 20 && age < 30 &&
  stature && !isNaN(stature) && stature >= 170 &&
  pet && pet.length > 0 && pet[pet.length-1] === "y"
){
  console.log("Welcome Spy!!")
}else{
  console.log("Sorry nothing to see here!!")
}
