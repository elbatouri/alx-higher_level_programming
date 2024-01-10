// Wait for the document to be fully loaded
$(document).ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
        $('#hello').text(data.hello);
    });
});
