let offset = 0 // храним смещения slider-line от левого края
const sliderLine = document.querySelector(".slider_line")
const windowWidth = 1
const pics = document.querySelectorAll('.one_of_sl')
const dots = document.querySelectorAll('.circle')
const dotsPanel = document.querySelector('.circle_pics')

document.querySelector(".slider_next").addEventListener('click', ()=>{
    let index = offset / windowWidth
    dots.item(index).classList.remove('activ')
    pics.item(index).classList.remove('act')
    offset += windowWidth

    if(index === pics.length - 1) {
        offset = 0;
    }

    index = offset / windowWidth
    dots.item(index).classList.add('activ')
    pics.item(index).classList.add('act')
})

document.querySelector(".slider_prev").addEventListener('click', ()=>{
    let index = offset / windowWidth
    dots.item(index).classList.remove('activ')
    pics.item(index).classList.remove('act')
    offset -= windowWidth

    if(index === 0) {
        offset = windowWidth * (pics.length - 1);
    }

    index = offset / windowWidth
    dots.item(index).classList.add('activ')
    pics.item(index).classList.add('act')
})

dotsPanel.addEventListener('click', (event)=>{
    event.preventDefault()
    const clickedDot = event.target.closest('.circle');
    const indexclickedDot = Array.prototype.indexOf.call(dots, clickedDot)

    if(!clickedDot) return

    // const activeDot = document.querySelector('.active')
    // activeDot.classList.remove('active')
    dots.item(offset).classList.remove('activ')
    pics.item(offset).classList.remove('act')
    clickedDot.classList.add('activ')
    offset = windowWidth * indexclickedDot
    pics.item(indexclickedDot).classList.add('act')
    
})