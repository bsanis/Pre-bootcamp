/*
Always Hungry
Write a function that is given an array and each time the value is "food" it should console log "yummy". 
If "food" was not present in the array console log "I'm hungry" once.
*/

function alwaysHungry(arr) {
    var food_finder = 0;
    for(var i=0 ; i<=arr.length ; i++){
        if (arr[i] == "food"){
                console.log("yummy");
                food_finder++;
        }
        if(food_finder == 0){
            console.log("I'm hungry");
        }

    }
    
}
   
alwaysHungry([3.14, "food", "pie", true, "food"]);
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"

/*
Better than average:
Given an array of numbers return a count of how many of the numbers are larger than the average.
*/

function highPass(arr, larger_nb) {
    var Arr_filt = [];
    for(var i=0; i<arr.length; i++) {
        if(arr[i] > larger_nb) {
            filtArr.push(arr[i]);
        }
    }
    return Arr_filt;
}

/*
Array Reverse:
Write a function that will reverse the values an array and return them.
*/

function better_Average(arr) {
    var sum = 0;

    for(var i=0; i<arr.length; i++) {
        sum += arr[i];
    }

    var avg = sum / arr.length;
    var count = 0

    for(var i=0; i<arr.length; i++) {
        if(arr[i] > avg) {
            count++;
        }
    }
    return count;
}
var result = better_Average([6, 8, 3, 10, -2, 5, 9]);


/*
Fibonacci Array:
Fibonacci numbers have been studied for years and appear often in nature. 
Write a function that will return an array of Fibonacci numbers up to a given length n. 
Fibonacci numbers are calculated by adding the last two values in the sequence together. 
So if the 4th value is 2 and the 5th value is 3 then the next value in the sequence is 5.
*/

function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    while(fibArr.length < n) {
        var prev = fibArr[fibArr.length-1];
        var prevprev = fibArr[fibArr.length-2];
        fibArr.push(prev + prevprev);
    }
    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
