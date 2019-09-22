function validateForm() {
  var x = document.forms["form"]["name"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  else if(x =="[0-9]") {
	  alert("it should not contain number");
	return false;
  }
}
