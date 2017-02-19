$(document).ready(function() {

    console.log($("#clothname").text());
    function clothlist(){
	$.getJSON("/getcloth/" + $("#clothname").text(), function(data){
	    //console.log("pls");
	    console.log(data);
	    $("#clothholder").append("Clothing Piece Name: " + data[0] + "<br>" +
				     '<img src="/../../static/images/uploads/' + data[0]+
				     '"  style="width:16rem">'+ "<br>" +
				     "Clothing Category: " +  data[2] + "<br>" +
				     "Clothing Subcategory: " + data[3]
				    );
	});
    };
    clothlist();

});
