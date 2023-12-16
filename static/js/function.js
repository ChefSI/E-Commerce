const monthNames = ["Jan","Feb","Mar","April","May","June","July","Aug","Sept","Oct","Nov","Dec"];

$("#reviewForm").submit(function(h){
    h.preventDefault();

    let dt = new Date();
    let time = dt.getDay()+ " " +monthNames[dt.getUTCMonth()]+ ", "+dt.getFullYear()
    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(response){
            console.log("Review Saved");

            if(response.bool == true){
                $("#review-res").html("Review Successfully Added.")
                $(".hide-review-form").hide()
                $(".add-review").hide()

                let _html = ' <div class="d-flex mb-3">'
                    _html +='<div class="flex-shrink-0">'
                    _html +='<img class="rounded-circle" src="{% static "img/customer-1.png" %}" alt="" width="50"/>'
                    _html +='</div>'
                    _html +='<div class="ms-3 flex-shrink-1">'
                    _html +='<h6 class="mb-0 text-uppercase">'+ response.context.user +'</h6>'
                    _html +='<p class="small text-muted mb-0 text-uppercase">'+time+'</p>'
                    for(let i =1; i<=response.context.rating; i++){
                        _html +='<i class="fas fa-star text-warning"></i>'
                    } 
                    _html +='<p class="text-sm mb-0 text-muted">'+ response.context.review +'</p>'
                    _html +='</div>'
                    _html +='</div>'
                
            $(".rev-ls").prepend(_html)
                }
        }
        })
})