$(document).ready(function () {
  // Submit form data for level game
  $('#upload').hide();
  // $('#game').show()

  // resources statics
  const url = `${document.location.origin}/static/assets`

  // load state by default
  gameDefault(url, 'level1');
  // save the current level
  let currentLevel = 'level1';

  // change of level
  $('#level1').on('click', function () {
    gameDefault(url, 'level1');
    currentLevel = 'level1';
  });
  $('#level2').on('click', function () {
    gameDefault(url, 'level2');
    currentLevel = 'level2';
  })
  $('#level3').on('click', function () {
    gameDefault(url, 'level3');
    currentLevel = 'level3';
  })

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
            gameDefault(url, 'load')
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

  // send value of input select
  /*
  0 -> Breadth first search
  1 -> Depth first search
  2 -> Uniform cost search
  3 -> Avara
  4 -> A*
  */
  $('#play').on('click', function () {
    $.ajax({
      url: '/game',
      type: 'POST',
      data: {
        option: $('#algoritm').val(),
        level: currentLevel
      },
      success: function (data) {
        data = JSON.parse(data);
        insertResults(data);
        gameDefault(url, currentLevel, false, data);
      },
      error: function () {
        console.log('sorry...');
      }
    });
  });

  function insertResults(data) {
    mov = data['mov'].join(', ')
    moves = `<p>${mov}</p>`
    report = `<p>Expanded nodes: ${data['node']}</p>
        <p>Depth: ${data['depth']}</p>
        <p>Computation time: ${data['compute']}</p> `
    $('#report').append($.parseHTML(report))
    $('#moves').append($.parseHTML(moves))
  }

});
