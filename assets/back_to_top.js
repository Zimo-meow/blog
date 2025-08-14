document.addEventListener("DOMContentLoaded", function () {
    const btn = document.createElement('button');
    btn.id = 'back2top';
    btn.innerText = '↑';
    document.body.appendChild(btn);

    window.addEventListener('scroll', () => {
        btn.style.display = window.scrollY > 600 ? 'block' : 'none';
    });

    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
