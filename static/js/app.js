const hamburger = document.querySelector('.hamburger')
const navLinks = document.querySelector('.nav-links')
const navLink = document.querySelector('.nav-link-user')
const line = document.querySelector('.line')


hamburger.addEventListener("click", () =>{
    navLinks.classList.toggle("open");
})




$(window).on("scroll", () =>{
    if($(window).scrollTop()){
        $('header').addClass('blue')

    }else{
        $('header').removeClass('blue')
    }
})
$(window).on("scroll", () => {
    if($(window).scrollTop()){
        $(navLink).addClass('square')
    }else{
        $(navLink).removeClass('square')
    }
})


const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button =>{
    button.addEventListener('click', () =>{
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})
closeModalButtons.forEach(button =>{
    button.addEventListener('click', () =>{
        const modal = button.closest('.modal')
        closeModal(modal)
    })
})
overlay.addEventListener('click', () =>{
    const modals = document.querySelectorAll('.modal.active')
    modals.forEach(modal =>{
        closeModal(modal)
    })
})

const openModal = (modal) =>{
    if(modal ==null) return
    modal.classList.add('active')
    overlay.classList.add('active')
}
const closeModal = modal =>{
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}
//pop1
const e = document.getElementById('popupBoxOnePosition');
const close = document.getElementById('closebox1');

document.getElementById('box1').addEventListener('click', function(){
    if(e.style.display === 'block')
        e.style.display = 'none';
    else
        e.style.display = 'block';
});

// When the user clicks on Click here to close modal
close.onclick = function() {
    e.style.display = "none";
}


