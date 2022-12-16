let other = document.querySelector('other')
let input = document.getElementById('.date-input')
let btn = document.getElementById('btn')

btn.addEventListener('click', (e) => {
    e.preventDefault()
    other.style.display = 'none'
    input.style.display = 'block'
    console.log('gg')
})

