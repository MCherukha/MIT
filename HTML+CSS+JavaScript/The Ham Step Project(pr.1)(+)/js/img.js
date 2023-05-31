const filterBox = document.querySelectorAll('.box');



const navigation = document.querySelector('nav'); 
navigation.addEventListener('click', (event) => { 
    if (event.target. tagName !== 'LI') return false;
    const previous = document.querySelectorAll('.active_all-list-button')
    // for (let i of previous){
    //     i.classList.remove('active_all-list-button')
    // }
    previous.forEach(item => item.classList.remove('active_all-list-button'))
    console.log(previous.values())
    event.target.classList.add('active_all-list-button')
    let filterClass = event.target.dataset['f'];
    filterBox.forEach((elem) => {
        elem.classList.remove('hide');
        if (!elem.classList.contains(filterClass) && filterClass !== 'all') { 
            elem.classList.add('hide');
        }
    })
});













