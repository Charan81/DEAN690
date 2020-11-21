var $ = jQuery.noConflict();

$("#simpleRadio").click(function () {
    $('#customMenu').hide();
});

$("#customRadio").click(function () {
    $('#customMenu').show();
});

$("#submitButton").click(function () {
    $('#loader').show();
});




