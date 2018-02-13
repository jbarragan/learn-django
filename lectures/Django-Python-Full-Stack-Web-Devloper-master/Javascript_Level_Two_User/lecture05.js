var carInfo = {make: "Toyota", year: 1990, model: "Camry"};

console.log(carInfo);
console.log(carInfo["make"]);

var myNewO = {a: "hello", b: [1,2,3], c: {inside: ['a', 'b']}};

console.log(myNewO);
console.dir(myNewO);
console.log(myNewO["a"]);
console.log(myNewO["b"][1]);

console.log(myNewO["c"]["inside"][1]);

carInfo["year"] = 2006;
console.log(carInfo);

carInfo["year"]++;
console.log(carInfo);
console.dir(carInfo);

for (var key in carInfo) {
  console.log(`key: ${key}, value: ${carInfo[key]}`);
}
