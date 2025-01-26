

document.addEventListener('DOMContentLoaded', function () {
  new Swiper('.card_wrapper_courses_list', {
    loop: false, // Вимкнути циклічне гортання
    slidesPerView: 4, // Відображати 4 елементи на сторінці
    spaceBetween: 30, // Відстань між слайдами
    watchOverflow: true,

    // Адаптивність
    breakpoints: {
      640: {
        slidesPerView: 1, // 1 слайд для екранів менше 640px
        spaceBetween: 10,
      },
      768: {
        slidesPerView: 2, // 2 слайди для середніх екранів
        spaceBetween: 15,
      },
      1024: {
        slidesPerView: 3, // 3 слайди для великих екранів
        spaceBetween: 20,
      },
      1280: {
        slidesPerView: 4, // 4 слайди для дуже великих екранів
        spaceBetween: 30,
      },
    },

    // Елементи управління
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true
    },
  });
});