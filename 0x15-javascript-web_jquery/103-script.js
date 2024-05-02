$(document).ready(function(){
    $("#btn_translate").click(fetchTranslation);
    
    $("#language_code").keydown(function(event){
        if (event.keyCode === 13) { // Enter key code is 13
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        var languageCode = $("#language_code").val();
        $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data){
            $("#hello").text(data.hello);
        });
    }
});
