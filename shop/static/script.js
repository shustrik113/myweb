$(function() {
    // LIKES
    $('.lnkLike').click(function(e) {
        console.log(e.target)
        $.ajax({
            type: 'POST',
            url: '/articles/article/addlike/',
            data: {
                'article_id' : e.target.alt,
                'csrfmiddlewaretoken' : csrf_token
            },
            success: function(data) {
                var num = e.target.alt;
                var tar = '.likes_of_' + num
                $(tar).html(data);
            },
            dataType: 'html'
        });
    });

    // POLL
    $('#vote').click(function() {
        $.ajax({
            type: 'POST',
            url: '/other/poll/vote/1/',
            data: {
                'vote' : $('input:radio[name=choice]:checked').val(),
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: vote,
            dataType: 'html'
        });
    });

    // SEARCH
    $('#search').keyup(function() {
        $.ajax({
            type: 'POST',
            url: '/other/search/',
            data: {
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });

    $('#search').click(function() {
        $.ajax({
            type: 'POST',
            url: '/other/search/',
            data: {
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });

    $('#search_results').mouseleave(function() {
        $.ajax({
            type: 'POST',
            url: '/other/search/',
            data: {
                'search_text' : '',
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR) {
    $('#search_results').html(data);
}

function vote(data, textStatus, jqXHR) {
    $('.poll').html(data);
}

