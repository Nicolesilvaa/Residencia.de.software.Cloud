//Js formulário

function campoVazio(){

	limpar();

	var n = document.getElementById("Semail");
	var s = document.getElementById("assunto");

	
	if(n.value == "" )
		document.getElementById("aEmail").innerHTML = "Prencha os campos obrigatórios";
	
	else if(s.value == "")
		document.getElementById("aAssunto").innerHTML = "Prencha os campos obrigatórios";
	
	else
		alert("Mensagem enviada")
}

function limpar(){
	
	document.getElementById("aEmail").innerHTML = "";
	document.getElementById("aAssunto").innerHTML = "";

	
}

