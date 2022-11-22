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
        try{
          const res = JSON.parse(response);
          $('span#result').html(res.data)
        } catch(e) {
          alert('Request error');
        }
      },
      error: function (error) {
        $('span#result').html(error);
      }
    });
  });
});