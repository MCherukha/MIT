const lm_button = document.querySelector('.lm_button');
let times = 0


lm_button.addEventListener('click', (event) => { 
    const previous = document.querySelectorAll('.hidden')
    const previous_slice = Array.prototype.slice.call(previous)
    const hprevious =  previous_slice.slice(0, 12)
    hprevious.forEach(item => item.classList.remove('hidden'))
    times+=1
    if (times == 2) lm_button.style.display = "none"
});