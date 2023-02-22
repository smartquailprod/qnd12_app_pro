    //   sliders ------------------		
     if ($(".multi-slideshow_1").length > 0) {
         var ms1 = new Swiper(".multi-slideshow_1 .swiper-container", {
             preloadImages: false,
             loop: true,
             speed: 1400,
             spaceBetween: 0,
             effect: "slide",
             autoplay: {
                 delay: 3500,
                 disableOnInteraction: false
             },
         });
         var ms2 = new Swiper(".multi-slideshow_2 .swiper-container", {
             preloadImages: false,
             loop: true,
             speed: 1400,
             spaceBetween: 0,
             direction: "vertical",
             effect: "slide",
         });
         var ms3 = new Swiper(".multi-slideshow_3 .swiper-container", {
             preloadImages: false,
             loop: true,
             speed: 1400,
             spaceBetween: 0,
             effect: "slide",
         });
         ms1.controller.control = ms2;
         ms2.controller.control = ms1;
         ms2.controller.control = ms3;
         ms3.controller.control = ms2;
         kpsc();
         ms1.on("slideChangeTransitionStart", function() {
             eqwe();
         });
         ms1.on("slideChangeTransitionEnd", function() {
             kpsc();
         });
     }
     if ($(".multi-slideshow_fs").length > 0) {
         var ms1 = new Swiper(".multi-slideshow_fs .swiper-container", {
             preloadImages: false,
             loop: true,
             speed: 1400,
             spaceBetween: 0,
             effect: "fade",
             autoplay: {
                 delay: 3500,
                 disableOnInteraction: false
             },
         });
         kpsc();
         ms1.on("slideChangeTransitionStart", function() {
             eqwe();
         });
         ms1.on("slideChangeTransitionEnd", function() {
             kpsc();
         });
     }
     function kpsc() {
         $(".slide-progress").css({
             width: "100%",
             transition: "width 3000ms"
         });
     }
     function eqwe() {
         $(".slide-progress").css({
             width: 0,
             transition: "width 0s"
         });
     };
    function setUpCarouselSlider() {
        $('.fw-carousel .swiper-wrapper').addClass('no-horizontal-slider');
     if ($(".fw-carousel").length > 0) {      
            if ($(window).width() >= 640 && j2 == undefined)
            {                
         var totalSlides2 = $(".fw-carousel .swiper-slide").length;
         var mouseContr = $(".fw-carousel").data("mousecontrol");
         var j2 = new Swiper(".fw-carousel .swiper-container", {
             preloadImages: false,
             loop: false,
             freeMode: true,
             slidesPerView: 'auto',
             spaceBetween: 10,
             grabCursor: true,
             mousewheel: mouseContr,
             speed: 1400,
             direction: "horizontal",
             scrollbar: {
                 el: '.hs_init',
                 draggable: true,
             },
             effect: "slide",
             pagination: {
                 el: '.fw-carousel-counter',
                 type: 'fraction',
                 renderFraction: function(currentClass) {
                     return '<span class="' + currentClass + '"></span>' + '' + '<span class="j2total">' + totalSlides2 + '</span>';
                 }
             },
             navigation: {
                 nextEl: '.fw-carousel-button-next',
                 prevEl: '.fw-carousel-button-prev',
             },
             on: {
                 resize: function() {
                     if ($(window).width() < 640) {
                         j2.update();
                     }
                 },
             }
         });
         $(".fw-carousel.thumb-contr .swiper-slide img").each(function() {
             var ccasdc = $(this).attr("src");
             $("<div class='thumb-img'><img src='" + ccasdc + "'></div>").appendTo(".thumbnail-wrap");
         });
         $(".thumb-img").on('click', function() {
             j2.slideTo($(this).index(), 500);
             hideThumbnails();
         });
            }

            if ($(window).width() < 640 && j2 !== undefined)
            {
                j2.destroy();
                j2 = undefined;
                $('.fw-carousel .swiper-wrapper').removeAttr('style').addClass('no-horizontal-slider');
                $('.swiper-slide').removeAttr('style');

            }
        }
    }
 	setUpCarouselSlider();
     if ($(".fs-slider").length > 0) {
         var mouseContr2 = $(".fs-slider").data("mousecontrol2");
         var j3 = new Swiper(".fs-slider .swiper-container", {
             preloadImages: false,
             loop: true,
             grabCursor: true,
             speed: 1400,
             spaceBetween: 0,
             effect: "slide",
             mousewheel: mouseContr2,
             pagination: {
                 el: '.hero-slider-wrap_pagination',
                 clickable: true,
             },
             navigation: {
                 nextEl: '.hero-slider-button-next',
                 prevEl: '.hero-slider-button-prev',
             },
             autoplay: {
                 delay: 2500,
                 disableOnInteraction: false
             },
             on: {
                 init: function() {
                     var fsslideract = $(".fs-slider .swiper-slide-active").data("fsslideropt1"),
                         fsslideract2 = $(".fs-slider .swiper-slide-active").data("fsslideropt2"),
                         fsslideract3 = $(".fs-slider .swiper-slide-active").data("fsslideropt3"),

                         fsslideurl = $(".fs-slider .swiper-slide-active").data("fssurl");


                     $(".opt-one").html(fsslideract);
                     $(".opt-two").html(fsslideract2);
                     $(".opt-three").html(fsslideract3);
                     $(".hero-slider_details_url").attr("href", fsslideurl);
                 },
             }
         });

         j3.on("slideChangeTransitionStart", function() {
             sliderDetailsChangeStart();
         });
         j3.on("slideChangeTransitionEnd", function() {
             sliderDetailsChangeEnd();
         });
         j3.on('slideChange', function() {
             var csli = j3.realIndex + 1,
                 curnum = $('#current');
             TweenMax.to(curnum, 0.2, {
                 force3D: true,
                 y: -10,
                 opacity: 0,
                 ease: Power2.easeOut,
                 onComplete: function() {
                     TweenMax.to(curnum, 0.1, {
                         force3D: true,
                         y: 10
                     });
                     curnum.html(csli);
                 }
             });
             TweenMax.to(curnum, 0.2, {
                 force3D: true,
                 y: 0,
                 delay: 0.3,
                 opacity: 1,
                 ease: Power2.easeOut
             });
         });
         var totalSlides = j3.slides.length - 2;
         $('#total').html(totalSlides);
     }
     var sliderDetailsItem = $(".hero-slider_details li");
     function sliderDetailsChangeStart() {
         TweenMax.to(sliderDetailsItem, 0.8, {
             force3D: true,
             y: "-30px",
             opacity: "0",
             ease: Power2.easeOut,
             onComplete: function() {

                 TweenMax.to(sliderDetailsItem, 0.1, {
                     force3D: true,
                     y: "30px",
                     ease: Power2.easeOut,

                 });
                 var fsslideract = $(".fs-slider .swiper-slide-active").data("fsslideropt1"),
                     fsslideract2 = $(".fs-slider .swiper-slide-active").data("fsslideropt2"),
                     fsslideract3 = $(".fs-slider .swiper-slide-active").data("fsslideropt3"),
                     fsslideurl = $(".fs-slider .swiper-slide-active").data("fssurl");
                 	$(".opt-one").html(fsslideract);
                 	$(".opt-two").html(fsslideract2);
                 	$(".opt-three").html(fsslideract3);
                 	$(".hero-slider_details_url").attr("href", fsslideurl);
             }
         });
     }
     function sliderDetailsChangeEnd() {
         sliderDetailsItem.each(function(ace) {
             var bp2 = $(this);
             setTimeout(function() {
                 TweenMax.to(bp2, 0.6, {
                     force3D: true,
                     y: "0",
                     opacity: "1",
                     ease: Power2.easeOut
                 });
             }, 110 * ace);
         });
     }
     if ($(".fs-slider2").length > 0) {
         $(".fs-slider2.thumb-contr .swiper-slide .bg").each(function() {
             var ccasdc3 = $(this).attr("data-bg");
             $("<div class='thumb-img'><img src='" + ccasdc3 + "'></div>").appendTo(".thumbnail-wrap");
         });
         $(".thumb-img").on('click', function() {
             fsSlider2.slideTo($(this).index() + 1, 500);
             hideThumbnails();
         });
         var mouseContr2 = $(".fs-slider2").data("mousecontrol2");
         var totalSlides2 = $(".fs-slider2 .swiper-slide").length;
         var fsSlider2 = new Swiper(".fs-slider2 .swiper-container", {
             preloadImages: false,
             loop: true,
             grabCursor: true,
             speed: 1400,
             spaceBetween: 0,
             effect: "slide",
             mousewheel: mouseContr2,
             pagination: {
                 el: '.fw-carousel-counter',
                 type: 'fraction',
                 renderFraction: function(currentClass) {
                     return '<span class="' + currentClass + '"></span>' + '' + '<span class="j2total">' + totalSlides2 + '</span>';
                 }
             },
             autoplay: {
                 delay: 3500,
                 disableOnInteraction: false
             },
             navigation: {
                 nextEl: '.ss-slider-cont-next',
                 prevEl: '.ss-slider-cont-prev',
             },
         });
     }

     function showfs() {
         $("#wrapper").addClass("fs-mode-active");

         TweenMax.to($(".bottom-panel"), 0.3, {
             force3D: true,
             bottom: "-100px",
             ease: Power2.easeOut
         });
         TweenMax.to($("header.main-header"), 0.3, {
             force3D: true,
             top: "-100px",
             ease: Power2.easeOut,
             onComplete: function() {
                 TweenMax.to($(".close-fs"), 0.8, {
                     force3D: true,
                     bottom: 0,
                 });

             }
         });
     }
     function hidefs() {
         $("#wrapper").removeClass("fs-mode-active");
         TweenMax.to($(".bottom-panel"), 0.3, {
             force3D: true,
             bottom: "0",
             ease: Power2.easeOut
         });
         TweenMax.to($("header.main-header"), 0.3, {
             force3D: true,
             top: "0",
             ease: Power2.easeOut
         });

         TweenMax.to($(".close-fs"), 0.8, {
             force3D: true,
             bottom: "-100px",
         });

     }
     $(".fs-mode").on("click", function() {
         showfs();
         return false;
     });
     $(".close-fs").on("click", function() {
         hidefs();
         return false;
     });
     var thumbcont = $(".thumbnail-container"),
         thumbItrm = $(".thumb-img"),
         stbtn = $(".show_thumbnails");
     function showThumbnails() {
         TweenMax.to(thumbcont, 1.0, {
             force3D: true,
             right: 0,
             ease: Expo.easeInOut,
             onComplete: function() {
                 thumbItrm.addClass("visthumbnails");
                 thumbcont.addClass("visthumbnails");
             }
         });
         stbtn.removeClass("unvisthum");
         hideDetails();
     }
     function hideThumbnails() {
         thumbItrm.removeClass("visthumbnails");
         TweenMax.to(thumbcont, 1.0, {
             force3D: true,
             delay: 0.2,
             left: "100%",
             ease: Expo.easeInOut,
             onComplete: function() {
                 TweenMax.to(thumbcont, 0.1, {
                     force3D: true,
                     left: 0,
                     right: "100%",
                     ease: Expo.easeInOut


                 });
                 thumbcont.removeClass("visthumbnails");
             }

         });
         stbtn.addClass("unvisthum");
     }
     stbtn.on("click", function() {
         if ($(this).hasClass("unvisthum")) showThumbnails();
         else hideThumbnails();
     });
     function showDetails() {
         $(".det-overlay").fadeIn(400);
         TweenMax.to($(".hid-det-anim"), 0.4, {
             force3D: true,
             left: 0,
             ease: Power2.easeOut,
             onComplete: function() {
                 $(".det-anim").each(function(ab) {
                     var bp3 = $(this);
                     setTimeout(function() {
                         TweenMax.to(bp3, 0.6, {
                             force3D: true,
                             y: "0",
                             opacity: "1",
                             ease: Power2.easeOut
                         });
                     }, 110 * ab);
                 });
             }

         });
         $(".shibtn").removeClass("unvisthum2");
         hideThumbnails();
     }
     function hideDetails() {
         $(".det-overlay").fadeOut(400);
         TweenMax.to($(".hid-det-anim"), 0.4, {
             force3D: true,
             left: "-650px",
             ease: Power2.easeOut,
             onComplete: function() {
                 TweenMax.to($(".det-anim"), 0.1, {
                     force3D: true,
                     y: "50",
                     opacity: "0",
                     ease: Power2.easeOut
                 });
             }
         });
         $(".shibtn").addClass("unvisthum2");
     }
     $(".shibtn").on("click", function() {
         if ($(this).hasClass("unvisthum2")) showDetails();
         else hideDetails();
     });

     $(".act-closedet").on("click", function() {
         hideDetails();
     });
     $(".initscroll").niceScroll({
         cursorwidth: "0",
         cursorborder: "none",
         cursorborderradius: "0px",
         scrollspeed: 10,
         mousescrollstep: 40,
         hwacceleration: true,
     });
     if ($(".testilider").length > 0) {
         var j2 = new Swiper(".testilider .swiper-container", {
             preloadImages: false,
             slidesPerView: 2,
             spaceBetween: 20,
             loop: true,
             grabCursor: true,
             mousewheel: false,
             navigation: {
                 nextEl: '.ss-slider-next',
                 prevEl: '.ss-slider-prev',
             },
             breakpoints: {
                 640: {
                     slidesPerView: 1,
                 },

             }
         });
     }
     if ($(".single-slider").length > 0) {
         var j2 = new Swiper(".single-slider .swiper-container", {
             preloadImages: false,
             slidesPerView: 1,
             spaceBetween: 0,
             loop: true,
             autoHeight: true,
             grabCursor: false,
             mousewheel: false,
             pagination: {
                 el: '.ss-slider-pagination',
                 clickable: true,
             },
             navigation: {
                 nextEl: '.ss-slider-cont-next',
                 prevEl: '.ss-slider-cont-prev',
             },
         });
     }