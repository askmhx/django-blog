/**
 * User: MengHX
 * Date: 5/8/13
 * Time: 12:26 PM
 */

$(function(){
    var url =  $(location).attr('pathname');
    var paths = url.split("/");
    if(paths.length>1&&paths[1]!=""){
        $("#nav_item_"+paths[1]).addClass("active");
    }else{
        $("#nav_item_blog").addClass("active");
    }
});

function thumbsClick(element, bId, type) {
    var cookieKey = "blog_thumbs_" + bId;
    if ($.cookie(cookieKey) == 'true') {
        return;
    }
    $.cookie(cookieKey, "true");
    $(element).children().last().text($(element).children().last().text() - 0 + 1);
    $.ajax({
        url: 'thumbs/' + type + '/' + bId + '/' + (new Date()).getTime()
    })
}

function subForm(tid) {
    var kw = document.getElementById("kw");
    var qFrom = document.getElementById("queryForm");
    switch (tid) {
        case 1:
            qFrom.action = "http://www.google.com/search";
            kw.name = "q";
            kw.setAttribute("name", "q");
            qFrom.submit();
            break;
        case 2:
            qFrom.action = "http://www.baidu.com/baidu";
            kw.name = "wd";
            kw.setAttribute("name", "wd");
            qFrom.submit();
            break;
        case 3:
            qFrom.action = "http://wwww.bing.com/search";
            kw.name = "q";
            kw.setAttribute("name", "q");
            qFrom.submit();
            break;
    }
}

function submitForm(e) {
    var event = window.event ? window.event : e;
    if (event.keyCode == 13) {
        subForm(1);
    }
}

var params = {
    "XOffset": 0, //提示框位置横向偏移量,单位px
    "YOffset": 0, //提示框位置纵向偏移量,单位px
    "fontSize": "14px",		//文字大小
    "fontFamily": "宋体",	//文字字体
    "borderColor": "gray", 	//提示框的边框颜色
    "bgcolorHI": "#03c",		//提示框高亮选择的颜色
    "sugSubmit": false		//在选择提示词条是是否提交表单
};
try{
    BaiduSuggestion.bind("kw", params, function (kwords) {
            document.getElementById("kw").value = kwords;
            subForm(1);
    });
    document.getElementById("kw").focus();
}catch(err){}
