$(document).ready(function(){
    $('.nepali-calendar').nepaliDatePicker();

    $('#nepaliDateD').nepaliDatePicker({
			disableBefore: '12/08/2060',
			disableAfter: '12/20/2090'
		});

    let dropDowns = $('.dropdown-item');
   	let categoryButton = $('.categoryButton');
   	let task_button = $('.taskStateButton');
 	dropDowns.each( function(index)
 	{
 		
 		$(this).click(function(){
 			console.log("Clicked");
 			if($(this).parent().hasClass('categoryDropDown'))
 			{
 				 categoryButton.text( $(this).text() );
 			}
 			else
 			{
 				 task_button.text( $(this).text() );
 			}
 			//if( $(this).parent()=="categoryDropDown" )
 		})
 	})

    // $('.dropdown-item').on('click',()=>{
    // 	console.log("clicked");
    // 	let value = $(this.html);
    // 	console.log(value); 
    // 	$('.category').html = value;
    // });

 });


