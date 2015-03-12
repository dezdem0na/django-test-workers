$(document).ready(function () {

    // input manipilations
    $('table.table td').dblclick(function () {
        try {
            var val = $(this).text();
            var id = $(this).attr('data-id');
            var field = $(this).attr('data-field');
            var type = $(this).attr('data-type');

            $(this).wrapInner('<input type=' + type + ' min="0" class="form-control">');
            $(this).find('input').focus();
            var obj_td = $(this);

            $(this).find('input').blur(function () {
                var new_val = $(this).val();
                $(this).parent().html(new_val);

                if ((new_val == '') || (new_val < 0)) {
                    alert('The field must be of the correct type and is not empty!');
                    obj_td.html($.trim(val));
                } else {
                    $.ajaxSetup({
                        headers: {"X-CSRFToken": getCookie('csrftoken')}
                    });

                    $.post('ajax_update/',
                        {
                            value: new_val, guid: id, field: field
                        });
                }
            });
        } catch (e) {

        }
    });


    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});