$(document).ready(function () {
  // Submit form data for level game
  $('#upload').hide();
  $('#game').show()

  // resources statics
  const url = `${document.location.origin}/static/assets`

  // load state by default
  gameDefault(url, 'level.json');

  // load new scene
  $('#file').on('change', function () {
    if (this.files[0]) {
      $('#upload').show();
      $('#fileInput').hide();
    } else {
      $('#upload').hide();
      $('#fileInput').show();
    }
  });

  function setUploadForm() {
    $('#fileInput').val('');
    $('#fileInput').show();
    $('#upload').hide();
  }

  $("#uploadForm").submit(function (e) {
    e.preventDefault(e);

    var reader = new FileReader();
    var line_data = $('#file').get(0);

    if (line_data.files.length) {
      reader.readAsText(line_data.files[0]);
      $(reader).on('load', function (e) {
        $.ajax({
          url: '/upload',
          type: 'POST',
          data: { level: e.target.result },
          success: function (returned_data) {
            setUploadForm();
            gameDefault(url, 'load.json')
            console.log(returned_data);
          },
          error: function () {
            setUploadForm();
            console.log('sorry...');
          }
        });
      });
    }
  });
  // end load new scene

});
