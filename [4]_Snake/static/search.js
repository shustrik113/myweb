$('#search').keyup(function() {
    var searchText = $('#search').val();
    var myExp = new RegExp(searchText, "i");

    $.getJSON('../static/snakes.json', function(data) {
        var result = '<ul class="searchRes">';
        $.each(data, function(key, val) {
            if ((val.name.search(myExp) != -1) ||
                (val.text.search(myExp) != -1)) {
                result += '<li><h2>' + val.name + '</h2>';
                result += '<img src="../static/images/snakes/' + val.img + '.jpg" />';
                result += '<p>' + val.text + '</p></li>';
            }
        });
        result += '</ul>';
        console.log(result);
        $('#snakesInfo').html(result);
    });
});