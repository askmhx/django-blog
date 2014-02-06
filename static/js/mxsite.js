/**
 * User: MengHX
 * Date: 5/8/13
 * Time: 12:26 PM
 */

function thumbsClick(element, bId, type) {
    var cookieKey = "blog_thumbs_" + bId;
    if ($.cookie(cookieKey) == 'true') {
        return;
    }
    $.cookie(cookieKey, "true");
    $(element).children().last().text($(element).children().last().text() - 0 + 1);
    $.ajax({
        url: 'thumbs/'+type+'/' + bId+ '/'+(new Date()).getTime()
    })
}