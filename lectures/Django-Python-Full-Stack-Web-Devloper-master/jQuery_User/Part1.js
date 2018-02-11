var x = $('h1');

x.css('color', 'red');
x.css('background', 'blue');

var newCss = { 'color': 'white',
  'background': 'blue',
  'border': '20px solid red'
}

x.css(newCss);

var listItems = $('li');

listItems.css('color', 'blue');
listItems.eq(0).css('color', 'orange');
listItems.eq(-1).css('color', 'orange');

$('h1').text();
$('h1').text("BRAND NEW TEXT");
$('h1').html();
$('h1').html("<em>new</em>");

$('input').eq(1).attr('type', 'checkbox');
$('input').eq(0).val('new value!');

$('h1').addClass('turnRed');
$('h1').removeClass('turnRed');
$('h1').toggleClass('turnBlue');
$('h1').toggleClass('turnBlue');
