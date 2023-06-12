async function redact() {
	const formValues = {
		postfix: document.getElementById("postfix").value || "redacted",
		regex: document.getElementById("regex").value,
		replacementChar: document.getElementById("replacementChar").value,
	}
	
	document.getElementById("redact-button").disabled = true;
	await eel.redact_py(formValues)(enableRedactButton);
	
}

function enableRedactButton() {
	document.getElementById("redact-button").disabled = false;
}

async function getFolder() {
	await eel.btn_fileUpload()(enableRedactButton);;
}
  
window.onload= () => {
	document.getElementById("redact-button").disabled = true;
	windowSize();
};


window.addEventListener("resize", windowSize());

function windowSize() {
	window.resizeTo("600", "450");
}
