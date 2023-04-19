function passdata() 
{
	var data = document.getElementById("data").value;
	eel.rankfinder(data)
}

eel.expose(jsc_printer);
function jsc_printer(string)
{
	alert(string);
	console.log(string)
}