$(function () {
  $('#submit').click(function (e) {
    e.preventDefault();
    const question = $('#question').val();
    const temperature = $('#temperature').val();
    $.ajax({
      url: '/predict',
      data: { 'question': question, 'temperature': temperature },
      type: 'POST',
      success: function (response, textStatus, xhr) {
        if (res.status) {
          alert('Request error');
        }

        const res = JSON.parse(response);
        if (res.status == 0) {
          $('span#result').html(res.data)
        } else {
          alert('Input error');
        }
      },
      error: function (error) {
        $('span#result').html(error);
      }
    });
  });
});