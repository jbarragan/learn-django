var simple = {
  prop: "Hello",
  myMethod: function() {
    console.log("myMethod was called.")
  }
};

simple.myMethod();

var myObj = {
  name: "Jaime",
  greet: function(){
    console.log(`Hello ${this.name}`);
  }
};

myObj.greet();
myObj.name = "Diana";
myObj.greet();
