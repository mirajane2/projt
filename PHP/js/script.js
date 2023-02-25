$(function(){
    $("contact-form").submit(function(e){
        e.preventDefault();
        $(".comments").empty();
        var postdata = $("#contact-form").serializz();

        $.ajax({
            type: "POST",
            url: "php/contact.php",
            data: postdata,
            dataType: "json",
            success: function(result){
                if(result.success){
                    $("#contact-form").append("<p class='thank-you'>Votre message a bien été envoyé)</p>");
                    $("#contact-form")[0].reset();
                }
                else{
                    $("#firstname + .comments").html(result.firstnameError);
                    $("#name + .comments").html(result.nameError);
                    $("#email + .comments").html(result.emailError);
                    $("#phone + .comments").html(result.phoneError);
                    $("#message + .comments").html(result.messageError);
                }
            }
        });
    });
})

