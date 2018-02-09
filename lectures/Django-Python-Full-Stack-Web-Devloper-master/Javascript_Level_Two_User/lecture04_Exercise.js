// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks
function selectTasks(){
  while(true){
    var answer = prompt("Would you like to start the roster web app? y/n");
    if(answer === "y") break;
    if(answer === "n") return;
    alert("Answer 'y' or 'n'.");
  }

  while(true){
    var task = prompt("Please select an action: add, remove, display, or quit.");
    if( task === "add" ) addStudent();
    else if( task === "remove" ) removeStudent();
    else if( task === "display" ) displayRoster();
    else if( task === "quit" ) return;
    else alert("Answer 'add', 'remove', 'display' or 'quit'.");
  }
}

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addStudent(){
  var name = prompt("What name would you like to add?");
  roster.push(name);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function removeStudent(){
  var name = prompt("What name would you like to remove?");
  var pos = roster.indexOf(name);
  if( pos >= 0 ) roster.splice(pos, 1);
  else alert(`Name ${name} not found in roster.`);
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function displayRoster() {
  console.log(roster);
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

selectTasks();
