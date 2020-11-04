const navSlide = () => {
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".nav-links");
  const navLinks = document.querySelectorAll(".nav-links li");
  //Toggle Nav

  burger.addEventListener("click", () => {
    nav.classList.toggle("nav-active");
    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = "";
      } else {
        link.style.animation = `navLinkFade 0.5s ease forwards ${
          index / 5 + 0.5
        }s`;
      }
    });
    burger.classList.toggle("toggle");
  });
};

navSlide();

const modalButton = document.querySelector('.harmo')
const modalBg = document.querySelector('.modal-bg')
const closeButton = document.querySelector('.modal-close')

modalButton.addEventListener('click', () => {
    modalBg.classList.add('bg-active')
})

closeButton.addEventListener('click', () => {
    modalBg.classList.remove('bg-active')
})