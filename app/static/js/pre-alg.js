/***********
 * Section 1 functions
 ***********/

//Generate the MASTERSEED

function send_section111() { //when request wkst form

	
	var elements = document.getElementsByClassName("editor");
	var tex = elements.getElementById("tex");
	console.log(tex);
	
}

function change(seed) {
	return seed
}

//Change the display setting to the block
function showPDF(seed) {
	var element = document.getElementsByClassName("col-worksheet");

	for (var i = 0; i < element.length; i++) {
		element[i].style.display = "block";
	}

	var element2 = document.getElementsByClassName("upload");

	for (var i = 0; i < element2.length; i++) {
		element2[i].style.display = "block";
	}

	var name = document.getElementById("studnetName").value;
	document.getElementById("txt-studnetName").innerHTML = name;
	var date = document.getElementById("dueDate").value;
	document.getElementById("txt-dueDate").innerHTML = date;

	//Desc
	document.getElementById("txt-title").innerHTML = document.getElementById("pdftitle").value;
	document.getElementById("txt-desc").innerHTML = document.getElementById("pdfdesc").value;
}

//Generate random problems
function sec1rand(min, max) {return Math.floor((Math.random() * (max - min + 1)) + min);}
function section1(min, max) { //difficulty, minimum, maximum
	var digit = sec1rand(1, 3), //define the value
	num = sec1rand(min, max),
	s_num = num.toString(),
	prob = "\\overline{b}",
	arr = [],
	problem = "";

	//into char
	s_num = num.toString();
	for(var i = 0; i < s_num.length; i += 1) {
		arr.push(+s_num.charAt(i));
	}

	//replace & combine
	if(digit == 1) {
		problem = "\\(" + prob.replace("b", arr[0]) + arr[1] + arr[2] + "\\)"; }
	else if(digit == 2) {
		problem = "\\(" + arr[0] + prob.replace("b", arr[1]) + arr[2] + "\\)"; }
	else {
		problem = "\\(" + arr[0] + arr[1] + prob.replace("b", arr[2]) + "\\)"; }

	return problem
}
