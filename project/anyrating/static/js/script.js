var mylink1 = document.getElementById("link2profile");
var mylink2 = document.getElementById("link2post");

if (mylink1 != null) {
	mylink1.addEventListener("click", function() {
		alert("Login to view other's profile.");
	});
}

if (mylink2 != null) {
	mylink2.addEventListener("click", function() {
		alert("Login to make a post.");
	});
}
