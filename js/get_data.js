$(document).ready(function () {
	$.getJSON("py/data.json", function(json) {
		console.log(json);
		document.getElementById("jsoninfo").innerHTML = JSON.stringify(json,null,4);
	});
});
