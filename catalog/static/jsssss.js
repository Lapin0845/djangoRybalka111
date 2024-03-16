$(document).ready(function() {
    // Обработка нажатия на кнопку покупки
    $('#buyButton').click(function() {
        // Показ сообщения о покупке
        $('#purchaseMessage').fadeIn();

    // Скролл к сообщению о покупке
    $('html, body').animate({
        scrollTop: $('#purchaseMessage').offset().top
    }, 1000);
    });
});