function runSearch( term) {
    $('#results').hide();
    $('tbody').empty();

    var formterm = $('#gene_search').serialize();

    $.ajax({
	url:'./frunsearch.cgi',
	dataType: 'json',
	data: formterm,
	success: function(data, textStatus, jqXHR) {
	    processJSON(data);
	},
	error: function(jqXHR, textStatus, errorThrown){
	    alert("Failed to perform search! textStatus: (" + textStatus + ") and errorThrown: (" + errorThrown")");
	}
    });
}

function processJSON( data) {
    $('#match_count').text (data.match_count );

    var next_row_num = 1;

    $.each( data.matches, function(i, item) {
	var this_row_id = 'result_row' + next_row_num++;

	$('<tr/>', {"id" : this_row_id } ).appendTo('tbody');

	$('<td/>', { "text" : item.loc } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.gene } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.gt } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.dn } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.rs } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.sig } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.clinvartype } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.sepred } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.sevartype } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.anpred } ).appendTo('#' + this_row_id);

	$('<td/>', { "text" : item.anvartype } ).appendTo('#' + this_row_id);

    });

    $('#results').show();

}


    


// run our javascript once the page is ready
$(document).ready( function() {
    $('#search_term').autocomplete({
	minLength:2,
	source:"./frunsearch.cgi"
    });
	
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;// prevents 'normal' form submission
    });
});
