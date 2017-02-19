$(document).ready(function() {

    function closet(){
	$.getJSON("/getcloset", function(data){
	    console.log(data);
	    $.each(data, function(i, cloth){
		if (cloth[2] == "Top"){
		    $("#top-closet").append('<div class="six columns" > Clothing Piece Name: ' + cloth[0] + "<br>" +
					     '<img src="/../../static/images/uploads/' + cloth[0]+
					     '"  style="width:16rem">'+ "<br>" +
					     "Clothing Category: " +  cloth[2] + "<br>" +
					     "Clothing Subcategory: " + cloth[3] + "<br> </div>"
					   )};
		if (cloth[2] == "Bottom"){
		    $("#bot-closet").append('<div class="six columns"> Clothing Piece Name: ' + cloth[0] + "<br>" +
					    '<img src="/../../static/images/uploads/' + cloth[0]+
					    '"  style="width:16rem">'+ "<br>" +
					    "Clothing Category: " +  cloth[2] + "<br>" +
					    "Clothing Subcategory: " + cloth[3] + "<br> </div>"
					   )}; 

		if (cloth[2] == "Other"){
		    $("#other-closet").append('<div class="six columns"> Clothing Piece Name: ' + cloth[0] + "<br>" +
					    '<img src="/../../static/images/uploads/' + cloth[0]+
					    '"  style="width:16rem">'+ "<br>" +
					    "Clothing Category: " +  cloth[2] + "<br>" +
					    "Clothing Subcategory: " + cloth[3] + "<br> </div>"
					   )}; 
	    });
	});
    };
    
    closet();

});
