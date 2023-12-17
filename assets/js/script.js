const wrapper = document.querySelector('.wrapper');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');




btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
})

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
})

document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById('menu');
    const navigation = document.getElementById('itens');

    menuIcon.addEventListener('click', function () {
        navigation.classList.toggle('active');
    });
});






