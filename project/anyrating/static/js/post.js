var titleEntry = document.getElementById("title");
var imageEntry = document.getElementById("image");
var ratingEntry = document.getElementById("rating");
var commentEntry = document.getElementById("comment");
var categoryEntry = document.getElementById("category");


var mySubmit = document.getElementById("btn_submit");
mySubmit.addEventListener("click", function() {
	if (!titleEntry.checkValidity() || !imageEntry.checkValidity() ||
		!ratingEntry.checkValidity() || !commentEntry.checkValidity() ||
		!categoryEntry.checkValidity()) {
		return;
	}

	alert("Make a post successfully!\nYou can check the post in the homepage.");
});