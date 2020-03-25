$(document).ready(function(){
    $(window).on("load", function(){
        $(".progress").each(function(issuedetail, progress ){
           var progressBar = $(progress).find(".progress-bar");
           var progressPercent = parseInt($(progressBar).attr("data-progress"));
           if ($(window).scrollTop() > $(progress).offset().top - 400){
                $(progressBar)
                    .css("width", progressPercent+"%")
                    .text(progressPercent+"%");
           }  
        })
    });
});