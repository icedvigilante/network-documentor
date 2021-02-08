$(document).ready(function() {
    $('#access-select').change(function() {
        if ($(this).val() == "console"){
            $('#access-method-details').hide();
        } else {
            $('#access-method-details').show();
        }
    })

    $('#device-add-button').click(function() {
        $('#device-add-form').toggle();
        $(this).text($(this).text() == 'Add Device' ? 'Close Form' : 'Add Device');
    })
});