const active = document.querySelector('.active').querySelector('button');
const tabsTitle = document.querySelectorAll('.tabs-title');
const triangle = document.createElement('div')
triangle.className = 'triangle_down'
triangle.style.transform = 'translateY(-20%)'
active.after(triangle)
const tabs = document.querySelector('.tabs')
tabs.addEventListener("click", (event) => {
    const citem = event.target.closest('button')
    citem.after(triangle)
})