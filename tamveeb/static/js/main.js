jQuery(function(){

    var minimized_elements = $('p.lead');

    minimized_elements.each(function(){
        var t = $(this).text();
        if(t.length < 150) return;

		t = t.replace(/#/g, "<br />");
		t = t.replace(/{/g, "<h3>");
		t = t.replace(/}/g, "</h3>");

        $(this).html(
            t.slice(0,100)+'<span>... </span><a href="#" class="more">Loe edasi...</a>'+
            '<span style="display:none;">'+ t.slice(100,t.length)+' <a href="#" class="less">Sulge</a></span>'
        );

    });

    $('a.more', minimized_elements).click(function(event){
        event.preventDefault();
        $(this).hide().prev().hide();
        $(this).next().show();
    });

    $('a.less', minimized_elements).click(function(event){
        event.preventDefault();
        $(this).parent().hide().prev().show().prev().show();
    });

});


function autoPlayModal(){
  var trigger = $("body").find('[data-toggle="modal"]');
  trigger.click(function() {
    var theFrame = $(this).data( "frame" );
    var theModal = $(this).data( "target" );
    videoSRC = $(this).attr( "data-theVideo" );
    videoSRCauto = videoSRC+"?autoplay=1";
    $(theModal+' '+ theFrame).attr('src', videoSRCauto);
    $("[id=videoModal]").on('hidden.bs.modal', function () {
        $("[id=videoModal] "+ theFrame).removeAttr('src');
    })
  });
}
