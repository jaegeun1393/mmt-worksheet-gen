function myFunction() {
	document.getElementById("myDropdown").classList.toggle("show");
	//change the location of the button "moveable"

	var y = document.getElementById("second-opt").style.top;
	//console.log("=y: ", y);
	if(y == "300px") {
		document.getElementById("second-opt").style.top = "0px";
	} else {
	document.getElementById("second-opt").style.top = "300px";
	}
}

function resetLocation() {
	document.getElementById("myDropdown2").classList.toggle("show"); //display options
	document.getElementById("second-opt").style.top = "0px"; //reset location
	var dropdowns = document.getElementsByClassName("dropdown-content2");
	var i;
	for (i = 0; i < dropdowns.length; i++) {
		var openDropdown = dropdowns[i];
		if (openDropdown.classList.contains('show')) {
			openDropdown.classList.remove('show');
		}
	}
}

function btnadd() {
	console.log("= Open");

	var dropdown = document.getElementById("AddDropdown");
	console.log("=id", dropdown);
	dropdown.classList.toggle("show");
}

function loginUser() {
	var emnail = document.getElementsByTagName("email").value;
	var password = document.getElementsByTagName("password").value;
	console.log("=Email", emnail);
	console.log("=password", password);
}
/*

This animation won't work in any version of IE.

*/
  

// Close the dropdown if the user clicks outside of it
/*window.onclick = function(event) {
	if (!event.target.matches('.dropbtn')) {
		document.getElementById("second-opt").style.top = "0px";
		var dropdowns = document.getElementsByClassName("dropdown-content");
	  	var i;
	  	for (i = 0; i < dropdowns.length; i++) {
			var openDropdown = dropdowns[i];
			if (openDropdown.classList.contains('show')) {
		  		openDropdown.classList.remove('show');
			}
	  	}
	}
}*/