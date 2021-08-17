/***********
 * Section 1 functions
 ***********/

//Generate the MASTERSEED

function send_section111() { //when request wkst form
	
	var all = document.querySelectorAll(".ace_editor");
	var editor = ace.edit(all[0].env.editor);
	editor.session.setValue("\\documentclass[12pt,oneside]{article}\\begin{document} \\setlength{\\belowdisplayskip}{5pt} \\setlength{\\belowdisplayshortskip}{0pt} \\setlength{\\abovedisplayskip}{-10pt} \\setlength{\\abovedisplayshortskip}{0pt} \\begin{flushright} Name: Jaegeun Oh\\\\ Insert Date\\\\ \\end{flushright} \\begin{center} Updated Worksheet\\\\ \\end{center} \\end{document}");
	
}

function mainPDFdesign() {
	const Tex = `\\documentclass[11pt,letterpaper]{article}
		\\usepackage[lmargin=1in,rmargin=1in,tmargin=1in,bmargin=1in]{geometry}

		\\usepackage{amsmath, amssymb, enumerate, graphicx, lastpage, multicol, multirow, qrcode, stackengine}

		\\usepackage[T1]{fontenc}
		\\usepackage{charter}

		\\newcommand{\\class}{Section Title}
		\\newcommand{\\term}{Worksheet Title}
		\\newcommand{\\instructor}{Firstname Lastname}
		\\newcommand{\\head}[2]{%
			\\thispagestyle{empty}
			\\vspace*{-0.5in}
	
			\\noindent\\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} l}
			\\textbf{#1} & \\textbf{Name:} & \\makebox[8cm]{\\hrulefill} \\\\
			\\textbf{#2} & & \\\\
			\\textbf{\\class:\\; \\term} & & \\\\
			\\textbf{Instructor: \\instructor}
			\\end{tabular*} \\\\
			\\rule[2ex]{\\textwidth}{2pt} %
		}


		\\newcommand{\\prob}{\\noindent\\textbf{Problem. }}
		\\newcounter{problem}
		\\newcommand{\\problem}{
			\\stepcounter{problem}%
			\\noindent \\textbf{Problem \\theproblem. }%
		}
		
		\\newcommand{\\pointproblem}[1]{
			\\stepcounter{problem}%
			\\noindent \\textbf{Problem \\theproblem.} (#1 points)\\,%
		}

		\\newcommand{\\pspace}{\\par\\vspace{\\baselineskip}}
		\\newcommand{\\ds}{\\displaystyle}

		\\usepackage{fancyhdr}

		\\fancypagestyle{pages}{
			\\fancyhead[L]{}
			\\fancyhead[C]{}
			\\fancyhead[R]{}
		\\renewcommand{\\headrulewidth}{0pt}
			\\fancyfoot[L]{}
			\\fancyfoot[C]{}
			\\fancyfoot[R]{}
		\\renewcommand{\\footrulewidth}{0.0pt}
		}
		\\headheight=0pt
		\\footskip=14pt

		\\pagestyle{pages}



	\\begin{document}
	\\head{MMTprep Worksheet}{Date: MM/DD/YYYY}

	\\pointproblem{5} This is the example sentence. \\vspace{1.5cm}

    
	{\\raggedleft\\vfill\\itshape\\Longstack[l]{%
		\\quad
		\\qrcode{http://127.0.0.1:5000/}
	}\\par
}

\\end{document}			
	`
	return Tex
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
