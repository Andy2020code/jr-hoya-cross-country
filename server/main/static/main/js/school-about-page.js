document.addEventListener('DOMContentLoaded', function () {
    const titles = document.querySelectorAll('.about-collapsible .about-title-01');
    titles.forEach(title => {
      title.addEventListener('click', function () {
        const content = this.nextElementSibling;
        const arrow = this.querySelector('.arrow-01');
        if (content.style.display === 'block') {
          content.style.display = 'none';
          arrow.style.transform = 'rotate(0deg)';
        } else {
          content.style.display = 'block';
          arrow.style.transform = 'rotate(90deg)';
        }
      });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const titles = document.querySelectorAll('.about-collapsible-02 .about-title-02');
    titles.forEach(title => {
      title.addEventListener('click', function () {
        const content = this.nextElementSibling;
        const arrow = this.querySelector('.arrow-02');
        if (content.style.display === 'block') {
          content.style.display = 'none';
          arrow.style.transform = 'rotate(0deg)';
        } else {
          content.style.display = 'block';
          arrow.style.transform = 'rotate(90deg)';
        }
      });
    });
});
