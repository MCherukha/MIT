const clicked = document.querySelector('.tabs');
clicked.addEventListener('click', (event) => {
    const item = event.target.closest('li')
    const clickedItemIndex = item.dataset.tab;
    const active = document.querySelector('.active');
    active.classList.remove( 'active');
    const clickedItem = event.target.closest('li');
    clickedItem.classList.add('active');
    const blocks = document.querySelectorAll('.tab-block');
    blocks.forEach((item) => {
        item.classList.add('hide');
        if (item.dataset.content == clickedItemIndex) { 
            item.classList.remove( 'hide');
        }
    });
});