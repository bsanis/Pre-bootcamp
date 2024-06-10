function hide(element){
    element.remove();
}


function changetxt(element){
        if(element.innerText == "Login") {
            element.innerText = "Logout";
        } 
        else {
            element.innerText = "Login";
        }
    }

function newlike(element){
    alert("ninja was liked",element)
}

function over(element) {
    alert("mouseover");    
}
    
function out(element) {
    alert("mouseout");    
}

