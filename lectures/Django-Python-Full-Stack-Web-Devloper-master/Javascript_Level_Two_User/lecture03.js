var countries = ["USA", "Germany", "China"];

console.log(countries);

console.log(countries[2]);

// Array are mutable
countries[2] = "Spain";

var myArr = ["one", "two", "three"];

var lastItem = myArr.pop();
console.log(lastItem);
console.log(myArr);

myArr.push("new_item");
console.log(myArr);
console.log(myArr[myArr-1]);

var matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
console.log(matrix.length);

var arr = ["A", "B", "C"];

for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

for (letter of arr) {
  console.log(letter);
}

function addAwesome(name){
  console.log(`${name} is awesome!`);
}

var topics = ["python", "django", "science"];
topics.forEach(addAwesome);
