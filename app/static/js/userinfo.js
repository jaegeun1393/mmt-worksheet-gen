/*
	Display User information
*/

function separate() {
	let value = document.getElementById("data").innerHTML;
	console.log(value);
	let myArr = value.split(',');
	myArr[1] = myArr[1]. slice(2, -1);
	myArr[4] = myArr[4]. slice(2, -2);
	let final = "Welcome back " + myArr[1] + " " + myArr[4] + "!"
	document.getElementById("username").innerHTML =  final;
}