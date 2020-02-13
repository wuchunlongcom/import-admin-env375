(function($) {
    'use strict';
    $(function() {
<<<<<<< HEAD
        $('.cancel-link').click(function(e) {
            e.preventDefault();
            window.history.back();
=======
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back(); // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
>>>>>>> 219290d11ca1b9abdcd9276ad6eac5ac0ca9b7cf
        });
    });
})(django.jQuery);
