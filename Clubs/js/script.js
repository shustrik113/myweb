// SLIDER

$('#slider_prev').click(function(){changeImg(false)});
$('#slider_next').click(function(){changeImg(true)});

var runSlider = setInterval(startChangeImg, 2500);

function startChangeImg() {
    changeImg(true);
}

$('.slider').mouseenter(function() {
    clearInterval(runSlider);
});

$('.slider').mouseleave(function() {
    runSlider = setInterval(startChangeImg, 2500);
});

function changeImg(switcher) {
    var switcher = switcher;
    var zMainImg = $('#mainImg').css('z-index');
    var zMainImg2 = $('#mainImg2').css('z-index');

    // Which image is upper
    if (zMainImg > zMainImg2) {
        var imgLower = $('#mainImg2');
        var imgUpper = $('#mainImg');
        var srcImg = imgUpper.attr('src');
    }
    else {
        var imgLower = $('#mainImg');
        var imgUpper = $('#mainImg2');
        var srcImg = imgUpper.attr('src');
    }

    var i;

    //Getting number of image
    i = parseInt(srcImg.substr(-5, 1));

    //Previous or next image
    if (switcher) {
        if (i >= 3) {i = 1;}
        else {++i;}
    } else {
        if (i <= 1) {i = 3;}
        else {--i;}
    }

    // Setting new source of image
    srcImg = 'img/slider/slider_0' + i + '.jpg';
    imgLower.attr('src', srcImg);
    imgLower.fadeIn(1);

    imgUpper.fadeOut(1000, function() {
        imgLower.css('z-index', '2');
        imgUpper.css('z-index', '1');
    });
}
