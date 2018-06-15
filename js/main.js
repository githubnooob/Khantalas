$(document).ready(function(){
    $('.nepali-calendar').nepaliDatePicker();

    $('#nepaliDateD').nepaliDatePicker({
			disableBefore: '12/08/2060',
			disableAfter: '12/20/2090'
		});

     $('.save').click(()=>{
	    $(".myData").text(JSON.stringify(youtubeData()));
	
	});
    let y = youtubeData();	



function youtubeData()
{


	let url= "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=NP&maxResults=10&key=AIzaSyB9ARJHdtJs4YxUdb2XnfpzkqLxGDQkDwU"; 


	let YoutubeApiCall = {}; 
	fetch(url) // Call the fetch function passing the url of the API as a parameter
	.then((resp) => resp.json())
	.then(function(data) {

		console.log("Data Fetched Properly"); 
		let items= data.items;
		let count = 0; 
		for ( item of items)
		{
			let title = item.snippet.title; 
			let channelTitle= item.snippet.channelTitle;
			let description = item.snippet.description;
			let thumbnailUrls = item.snippet.thumbnails.default;
			let pubDate = item.snippet.publishedAt; 
			let youtubeVideo = item.id;
			YoutubeApiCall[`${count}`] = {
									"title" : title,
									"channelTitle" : channelTitle,
									"thumbnail" : thumbnailUrls,
									"pubDate" : pubDate,
									"youtubeVideo" : youtubeVideo
									};  
			count++; 

		}
		return YoutubeApiCall; 
	})

	.catch(function() {
		console.log(" Some Error Occured "); 
	});

return YoutubeApiCall ; 
}





});

