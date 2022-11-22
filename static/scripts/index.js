$(function () {
  $('#submit').click(function (e) {
    e.preventDefault();
    const question = $('#question').val();
    const temperature = $('#temperature').val();
    $.ajax({
      url: '/predict',
      data: { 'question': question, 'temperature': temperature },
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