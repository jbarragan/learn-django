var x = 0;

while (x < 5) {
  console.log("x is currently: " + x)
  console.log("x is still less than 5, adding 1 to x");
  x = x + 1;
}

x = 0;
while (x < 5) {
  console.log("x is currently: " + x)
  console.log("x is still less than 5, adding 1 to x");
  if (x == 3) {
    console.log("X IS EQUAL TO " + x)
    break;
  }
  x = x + 1;
}

x = 1;
while (x <= 10){
  if( x % 2 == 0) console.log(x);
  x++;
}
