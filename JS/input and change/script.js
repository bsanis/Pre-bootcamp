
var namespan = document.querySelector("#name");
var foodtoOrder = "Pizza";

function setname(element){
    console.log(element.value);
    namespan.innerText = element.value;
}

function pickfood(element){
    console.log("The food is :"+" "+element.value);
    foodtoOrder= element.value;
}

function order(){
    alert("ordering a" + " " + foodtoOrder);

}