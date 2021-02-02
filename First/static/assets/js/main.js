
$(document).ready(function() {
    $(".rating a").click(function() {

    let value = $(this).data('value');
    let id = $("#did").val();

    for(i=1;i<=value;i++)
    {
        let n="#r" + i;
        $(n).css("color","orange");
    }


        $.ajax({
            url: "/add_rating/",
            type: 'POST',
            data: {'rating': value,"did":id},
            success: function (d){

            }
        })

    });
     $("p").off( 'click' );
});


