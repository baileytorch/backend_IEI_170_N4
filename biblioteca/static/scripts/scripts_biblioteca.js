$(document).ready(function() {
    $('label').each(function() {
        $(this).addClass('form-label');
    });
    
    $(':input:not(:button)').each(function() {
        $(this).addClass('form-control');
    });
});