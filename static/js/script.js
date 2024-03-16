let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
};

document.addEventListener('click', (event) => {
    const clickedElement = event.target;
    if (!clickedElement.closest('#menu-btn') && !clickedElement.closest('.navbar')) {
        menu.classList.remove('fa-times');
        navbar.classList.remove('active');
    }
});
