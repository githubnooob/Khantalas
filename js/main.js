$(document).ready(function(){
    $('.nepali-calendar').nepaliDatePicker();

    $('#nepaliDateD').nepaliDatePicker({
			disableBefore: '12/08/2060',
			disableAfter: '12/20/2090'
		});

});

