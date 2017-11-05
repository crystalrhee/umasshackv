$(function() {
	$("input").focus();
});

// $.get('file_to_read.txt', function(data) {
//    if ($("#tempRead").val())
// }, 'text');

function readFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
								"#tempRead" = allText.val();
                alert(allText);
            }
        }
    }
    rawFile.send(null);

		// if ($("#tempRead").val() == allText.val())
		// {
		// 	$("#tempRead").val() = all;
		// }
}

$(function timeOut() {
  setTimeout(readFile("file:///Users/msliv/Documents/umasshackv/umasshack/Arduino/temp_display/temp_data.txt") { timeOut() },1000);
});
