class Player{
  constructor(name, color){
    this.name = name;
    this.color = color;
  }

  getTurnMessage(){
    return `${this.name}: it is your turn, please pick a column to drop your ${this.color} chip.`
  }

  getWinMessage(){
    return `${this.name} with ${this.color} chips is the winner!!`;
  }
}

var player_1_name = prompt("Player One: Enter Your Name, you will be Blue");
const player1 = new Player(player_1_name, 'blue');
var player_2_name = prompt("Player Two: Enter Your Name, you will be Red");
const player2 = new Player(player_2_name, 'red');

const ROWS = 6;
const COLUMNS = 7;
const CONNECT_NUMBER_WINNER = 3;

var current_player = player1;
var we_have_a_winner = false;

changeMessage(player1.getTurnMessage());

$('td').click(function() {
  fillColumnCircle($(this).index());
})

function fillColumnCircle(column) {
  if( we_have_a_winner ) return;
  var found = false;
  var trs = $('tr');
  for (var i = 1; i <= ROWS; i++) {
    var tr = trs.eq(-i);
    row = ROWS - i;
    var circle_color = getColor(column, row);
    if( circle_color !== player1.color && circle_color !== player2.color)
    {
      found = true;
      getCircle(column, row).attr('fill', current_player.color);
      break;
    }
  }
  if( !found ) alert("Column does not have more space available. Please Select a different Column.")
  else{
    if( checkForWinner(column, row) === false ) switch_player();
    else{
      changeMessage(current_player.getWinMessage());
    }
  }
}

function checkForWinner(c, r) {
  we_have_a_winner = checkForWinnerDirection(c, r, 1, 0) ||
   checkForWinnerDirection(c, r, 0, 1) ||
   checkForWinnerDirection(c, r, 1, 1) ||
   checkForWinnerDirection(c, r, -1, 1);
   return we_have_a_winner;
}

function checkForWinnerDirection(c, r, dx, dy) {
  var x = c;
  var y = r;
  var color = getColor(x, y)
  var circle_array = [];
  circle_array.push(getCircle(x,y));
  selectConnectedCircles(c, r, dx, dy, color, circle_array);
  selectConnectedCircles(c, r, -dx, -dy, color, circle_array);
  if(circle_array.length >= CONNECT_NUMBER_WINNER) {
    for (circle of circle_array) {
      circle.attr('fill', 'green');
    }
  }
  return (circle_array.length >= CONNECT_NUMBER_WINNER);
}

function selectConnectedCircles(c, r, dx, dy, color, circle_array) {
  var x = c + dx;
  var y = r + dy;
  while( x >= 0 && x < COLUMNS && y >= 0 && y < ROWS){
    var new_color = getColor(x, y);
    if( color === new_color ) circle_array.push(getCircle(x, y));
    else break;
    x += dx;
    y += dy;
  }
}

function getColor(x, y) {
  return getCircle(x, y).attr('fill');
}

function getCircle(x, y) {
  var tr = $('tr').eq(y);
  var circle = $('circle', tr).eq(x);
  return circle;
}

function switch_player() {
  current_player = (current_player === player1) ? player2 : player1;
  changeMessage(current_player.getTurnMessage());
}

function changeMessage(msg) {
  $('h3').text(msg);
}
