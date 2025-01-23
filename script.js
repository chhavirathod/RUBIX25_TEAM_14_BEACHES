const mapImage = document.querySelector('.map-image');

window.addEventListener('scroll', () => {
  const scrollPosition = window.scrollY;
  const imagePosition = mapImage.offsetTop;

  if (scrollPosition >= imagePosition - window.innerHeight * 0.5) {
    mapImage.classList.add('visible');
  } else {
    mapImage.classList.remove('visible');
  }
});