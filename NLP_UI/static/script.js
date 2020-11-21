var $ = jQuery.noConflict();

$("#simpleRadio").click(function () {
    $('#customMenu').hide();
});

$("#customRadio").click(function () {
    $('#customMenu').show();
});

$("#submitButton").click(function () {
    if(document.getElementById("searchQuery").value.length != 0){
        $('#loader').show();
    }
});




