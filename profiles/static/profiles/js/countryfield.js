let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', 'var(--text-light)');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', 'var(--text-light)');
    } else {
        $(this).css('color', 'var(--dark)');
    }
});