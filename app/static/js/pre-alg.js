/*
 * Section 1 functions
 */

function send_section111() { //when request wkst form
	var accept = 0;
	var seed = "";
	var min = parseInt(document.getElementById("minnum").value);
	var max = parseInt(document.getElementById("maxnum").value);
	var nump = document.getElementById("numprob").value;
	
	//exit cases
	if(min >= max) {
		alert("The minimum value is smaller than the maximum value.");
		accept = 1;
	}
	else if(min < 100 || isNaN(parseFloat(min))) {
		alert("The minimum value should be at least 100.");
		accept = 1;	
	}
	else if(max > 900 || isNaN(parseFloat(max))) {
		alert("The maximum value should not more than 900.");
		accept = 1;	
	}
	else if(nump < 1 || nump > 10) {
		alert("Please check the Number of Problems");
		accept = 1;	
	}

	if(accept == 0) {
		var element = document.getElementsByClassName("col-worksheet");

		for (var i = 0; i < element.length; i++) {
			element[i].style.display = "block";
		} 

		var name = document.getElementById("studnetName").value;
		document.getElementById("txt-studnetName").innerHTML = name;
		var date = document.getElementById("dueDate").value;
		document.getElementById("txt-dueDate").innerHTML = date;

		//Desc
		document.getElementById("txt-title").innerHTML = document.getElementById("pdftitle").value;
		document.getElementById("txt-desc").innerHTML = document.getElementById("pdfdesc").value;

		//seed = preseed + "-" + nump + "&&";
		for(var i = 0; i < nump; i++) {
			var question = section1(1, min, max);
			question = question.replace("[", "$");
			question = question.replace("]", "$");
		//	seed += question;
	
			var divs = document.createElement("p");
			divs.innerHTML = question;
			console.log(divs);
			document.getElementById("wks-problems").appendChild(divs);
			//if(i != nump-1) {seed += ",";}
		}
	//	console.log("=seed: ", seed);
	} //Handling option closed
}

function sec1rand(min, max) {
	return Math.floor((Math.random() * (max - min + 1)) + min);
}

function section1(min, max) { //difficulty, minimum, maximum 
	var digit = sec1rand(1, 3), //define the value 
	num = sec1rand(min, max), 
	s_num = num.toString(),
	prob = "\\overline{b}", 
	arr = [],
	problem = "";

	//into char
	num = 614;
	s_num = num.toString();
	for(var i = 0; i < s_num.length; i += 1) {
		arr.push(+s_num.charAt(i));
	}

	//replace & combine
	if(digit == 1) { 
		problem = "[" + prob.replace("b", arr[0]) + arr[1] + arr[2] + "]"; }
	else if(digit == 2) { 
		problem = "[" + arr[0] + prob.replace("b", arr[1]) + arr[2] + "]"; } 
	else { 
		problem = "[" + arr[0] + arr[1] + prob.replace("b", arr[2]) + "]"; }
	
	return problem
}