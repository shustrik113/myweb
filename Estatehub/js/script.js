// SLIDER

$('.slider_nav1').click(function(){changeImg(false)});
$('.slider_nav2').click(function(){changeImg(true)});

$('input[name=header]:radio').click(function(e) {
    var targetID = e.target.id;

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

    // Setting new source of image
    var i = parseInt(targetID.substr(-1, 1));
    var srcImg = 'images/header_0' + i + '.jpg';
    imgLower.attr('src', srcImg);
    imgLower.fadeIn(1);

    imgUpper.fadeOut(1000, function() {
        imgLower.css('z-index', '2');
        imgUpper.css('z-index', '1');
    });
});

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
    srcImg = 'images/header_0' + i + '.jpg';
    imgLower.attr('src', srcImg);
    imgLower.fadeIn(1);

    // Changing radio markers
    var radio = '#img_0' + i;
    $(radio).prop('checked', true);

    imgUpper.fadeOut(1000, function() {
        imgLower.css('z-index', '2');
        imgUpper.css('z-index', '1');
    });
}

// TABS
$('#tab1, #tab2').click(function(e) {
    var tab = e.target;
    if (tab.className != 'active') {
        tab.className = 'active';
        if (tab.id == 'tab1') {
            $('#tab2').removeClass('active');
            $('.select_block_tab2').removeClass('active');
            $('.select_block_tab1').addClass('active');
        } else {
            $('#tab1').removeClass('active');
            $('.select_block_tab1').removeClass('active');
            $('.select_block_tab2').addClass('active');
        }
    }
});

