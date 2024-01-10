// add a list element to a list onclick

$('DIV#add_item').click(() => {
  $('UL.my_list').append('<li>Item</li>');
});
