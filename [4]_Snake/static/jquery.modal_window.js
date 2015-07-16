;(function($) {
    $.fn.modalWindow = function(options) {
        options = $.extend({
            overlay: "#MWindowOverlay",
            close: "#MWindowClose"
        }, options);

        var MWindow = this;

        var make = function() {
            $(options.overlay).fadeIn(400,
                function() {
                    $(MWindow)
                        .css('display', 'block')
                        .animate({
                            opacity: 1,
                            top: "50%"
                        }, 200);
                });
            $(options.close).click(function() {
                $(MWindow).animate({
                    opacity: 0,
                    top: '45%'
                }, 200,
                    function() {
                        $(this).css('display', 'none');
                        $(options.overlay).fadeOut(400);
                    }
                );
            });
        };

        return this.each(make);
    };
})(jQuery);

