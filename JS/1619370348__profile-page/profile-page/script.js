console.log("page loaded...");

var username = document.querySelector("#username");
var request = document.querySelector("#requests");

function edit() {
    username.innertext = "anne-s";
}

function remove(id) {
    var user = document.querySelector(id);
    user.remove();
    request.innertext--;
}

