let order = document.querySelector('.table__order')
    delivery = document.querySelector('.table__delivery')
    btn_order = document.getElementById('order_btn')
    btn_delivery = document.getElementById('delivery_btn')

btn_order.addEventListener('click', (e) => {
    e.preventDefault()
    delivery.style.display = 'none'
    order.style.display = ''
    order.style.width = '100%'
    console.log('gg')
})

btn_delivery.addEventListener('click', (e) => {
    e.preventDefault()
    delivery.style.display = ''
    delivery.style.width = '100%'
    order.style.display = 'none'
    console.log('gg')
})