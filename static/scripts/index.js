$(function () {
  $('#submit').click(function (e) {
    e.preventDefault();
    var question = $('#question').val();
    $.ajax({
      url: '/predict',
      data: { 'question': question },
      type: 'POST',
      success: function (response) {
        const res = JSON.parse(response);
        $('span#result').html(res.data)
      },
      error: function (error) {
        console.log(error);
      }
    });
  });
});