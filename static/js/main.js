$(document).ready(function(){
    $('.nepali-calendar').nepaliDatePicker();

    $('#nepaliDateD').nepaliDatePicker({
			disableBefore: '12/08/2060',
			disableAfter: '12/20/2090'
		});


    let labelForFileName = $('.custom-file-label')
    let inputFile = $(".custom-file-input");
    let actual_fileName = $(".actual_file");
    inputFile.change(function(e){
            let fileName = e.target.files[0].name;
            labelForFileName.text(fileName);
            actual_fileName.attr("value",fileName)  ;
            console.log(fileName);

		})
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
 				 $(".category_DropDownValue").attr("value", $(this).text() ); 
 			}
 			if($(this).parent().hasClass('taskDropDown')) 			
 			{
 				 task_button.text( $(this).text() );
 				 $(".taskState_DropDownValue").attr("value", $(this).text() ); 

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


