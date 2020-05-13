$(document).ready(function(){
    $('.carousel').carousel({
        interval: 4000
    })
    
    const $valueSpan = $('.valueSpan')
    const $value = $('#slider11')
    $valueSpan.html($value.val())
    $value.on('input change', () => {

    $valueSpan.html($value.val())
  })
})

