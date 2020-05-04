// these functions execute our search via an AJAX call
function gene_search( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#search_term').serialize();
    
    $.ajax({
        url: './gene_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}
function dn_search( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#search_term').serialize();
    
    $.ajax({
        url: './dn_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function rs_search( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#rs_term').serialize();
    
    $.ajax({
        url: './rs_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function sig_search( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#search_term').serialize();
    
    $.ajax({
        url: './sig_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function anpred_search( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#search_term').serialize();
    
    $.ajax({
        url: './anpred_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

function sepred_search( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#search_term').serialize();
    
    $.ajax({
        url: './sepred_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count );
    
    // this will be used to keep track of row identifiers
    var next_row_num = 1;
    
    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
    
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');
        
        // add the loc column
        $('<td/>', { "text" : item.loc } ).appendTo('#' + this_row_id);
        
        // add the gene column
        $('<td/>', { "text" : item.gene } ).appendTo('#' + this_row_id);

        // add the gt column
        $('<td/>', { "text" : item.gt } ).appendTo('#' + this_row_id);

        // add the dn column
        $('<td/>', { "text" : item.dn } ).appendTo('#' + this_row_id);

        // add the rs column
        $('<td/>', { "text" : item.rs } ).appendTo('#' + this_row_id);

        // add the sig column
        $('<td/>', { "text" : item.sig } ).appendTo('#' + this_row_id);

        // add the clinvartype column
        $('<td/>', { "text" : item.clinvartype } ).appendTo('#' + this_row_id);

        // add the sepred column
        $('<td/>', { "text" : item.sepred } ).appendTo('#' + this_row_id);

        // add the sevartype column
        $('<td/>', { "text" : item.sevartype } ).appendTo('#' + this_row_id);

        // add the anpred column
        $('<td/>', { "text" : item.anpred } ).appendTo('#' + this_row_id);

        // add the anvartype column
        $('<td/>', { "text" : item.anvartype } ).appendTo('#' + this_row_id);

    });

    $.each($('td'), function () {
	if($(this).html() == 'HIGH' || $(this).html() == 'Automatic_disease_causing' || $(this).html() == 'Pathogenic' || $(this).html() == 'Pathogenic/Likely_pathogenic'|| $(this).html() == 'Likely_pathogenic') {
	    $(this).css('background-color', 'FireBrick');
	}
	    
	if($(this).html() == 'MODERATE' || $(this).html() == 'Disease_causing' || $(this).html() == 'Conflicting_interpretations_of_pathogenicity' || $(this).html() == 'Pathogenic,_risk_factor') {
	    $(this).css('background-color', 'LightCoral');
	}

	if($(this).html() == 'drug_response' || $(this).html() == 'LOW' ||$(this).html() == 'Uncertain_significance') {
	    $(this).css('background-color', 'MistyRose');
	}
	    
	if($(this).html() == 'CHT' || $(this).html() == 'HM') {
	    $(this).css('background-color', 'LightGrey');
	}

	if($(this).html() == 'Automatic_polymorphism' || $(this).html() == 'Polymorphism' || $(this).html() == 'Benign' || $(this).html() == 'Likely_benign' || $(this).html() == 'Benign/Likely_benign') {
	    $(this).css('background-color', 'LightGreen');
	}

	if($(this).html() == 'null') {
	    $(this).html('.');
	}
    });
    
    // now show the result section that was previously hidden
    $('#results').show();
}
    


// run our javascript once the page is ready
$(document).ready( function() {
    $('#search').hide();
    $('#rs_search').hide();
    $('#choose').click( function() {
	var search_type = $('input:radio[name=choice]:checked').val()
	if (search_type == 'gene'){
	    $('#search').show();
	    $('#rs_search').hide();
	    $('#search_term').autocomplete({
		minLength:3,
		source:"./gene_auto.cgi"
	    });
	    // define what should happen when a user clicks submit
	    $('#submit').click( function() {
		gene_search();
		return false;// prevents 'normal' form submission
	    });
	} if (search_type == 'dn'){
	    $('#search').show();
	    $('#rs_search').hide();
	    //add autocomplete
	    $('#search_term').autocomplete({
		minLength:4,
		source:"./dn_auto.cgi"
	    });
	    // define what should happen when a user clicks submit
	    $('#submit').click( function() {
		dn_search();
		return false;// prevents 'normal' form submission
	    });
	} if (search_type == 'rs'){
	    $('#rs_search').show();
	    $('#search').hide();
	    // define what should happen when a user clicks submit no atuocomplete for rs
	    $('#rs_submit').click( function() {
		rs_search();
		return false;// prevents 'normal' form submission
	    });
	} if (search_type == 'sig'){
	    $('#search').show();
	    $('#rs_search').hide();
	    //add autocomplete
	    $('#search_term').autocomplete({
		minLength:1,
		source:"./sig_auto.cgi"
	    });
	    // define what should happen when a user clicks submit
	    $('#submit').click( function() {
		sig_search();
		return false;// prevents 'normal' form submission
	    });
	} if (search_type == 'anpred'){
	    $('#search').show();
	    $('#rs_search').hide();
	    //add autocomplete
	    $('#search_term').autocomplete({
		minLength:0,
		source:"./anpred_auto.cgi"
	    });
	    $('#search_term').autocomplete("search", "");
	    // define what should happen when a user clicks submit
	    $('#submit').click( function() {
		anpred_search();
		return false;// prevents 'normal' form submission
	    });
	    
	} if (search_type == 'sepred'){
	    $('#search').show();
	    $('#rs_search').hide();
	    //add autocomplete
	    $('#search_term').autocomplete({
		minLength:0,
		source:"./sepred_auto.cgi"
	    });
	    $('#search_term').autocomplete("search", "");
	    // define what should happen when a user clicks submit
	    $('#submit').click( function() {
		sepred_search();
		return false;// prevents 'normal' form submission
	    });

	}
    });
});

	
	
