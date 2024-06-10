var count=3;
var likelement = document.querySelector("#count");

function add1(){
    count++;
    likelement.innerText = count + " "+"like(s)";
    console.log(count);
}