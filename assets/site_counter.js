document.addEventListener("DOMContentLoaded", function () {
    const counterDiv = document.createElement('div');
    counterDiv.id = 'site-counter';
    counterDiv.innerHTML = '总访问量 <span id="busuanzi_value_site_pv">0</span> 次';
    document.body.appendChild(counterDiv);

    const script = document.createElement('script');
    script.src = '//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js';
    script.defer = true;
    document.body.appendChild(script);
});
