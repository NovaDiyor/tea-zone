let showInput = document.getElementById('input')
let dateInfo = document.getElementById('datepickerNoOfMonths')
let btnOrder = document.getElementById('btn__order')

btnOrder.addEventListener('click', function () {
    showInput.style.display = 'block'
    dateInfo.style.display = 'none'
    console.log('end function')
})