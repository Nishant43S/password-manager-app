// Back link animation
const backLink = document.querySelector('.back-link');
backLink.addEventListener('mouseover', function() {
    this.style.color = '#ff8c00';
    this.style.transform = 'translateX(-5px)';
});

backLink.addEventListener('mouseout', function() {
    this.style.color = '#333';
    this.style.transform = 'translateX(0)';
});