true
false

3 > 2;
2 > 3;

"user" == "user"
"2" == 2 // true
"2" === 2 // false

"2" !== 2 // true
"2" != 2 // false

true == 1; // true
false == 0; // true

null == undefined; // true
null === undefined; // false

NaN == NaN; // true

var x = 1
var y = 2

// Exercise 1
"2" == y && x === 1;
("2" == y && x === 1) == true;

// Exercise 2
x >= 0 || y === "2";
(x >= 0 || y === "2") == true;

// Exercise 3
!(x !== 1) && y === (1+1);
(!(x !== 1) && y === (1+1)) == true;

// Exercise 4
y !== "2" && x < 10 ;
(y !== "2" && x < 10) == true;

// Exercise 5
y !== x || y == "2" || x === 3;
(y !== x || y == "2" || x === 3) == true;
