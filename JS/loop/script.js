for(var i=1; i<=100; i++) {
    if(i % 15 == 0) {
        console.log("FizzBuzz");
    } else if(i % 5 == 0) {
        console.log("Buzz");
    } else if(i % 3 == 0) {
        console.log("Fizz");
    } else {
        console.log(i); //normal display
    }
}
//print odds

for (i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
      console.log(i);
    }
  }

//Multiple of 3
for(var x=100; x >=0 ; x-- ){
    if(x % 3 === 0){
        console.log(x, " is divisible by 3");
    }
}


//print the sequence
y=4
while (y != (-3.5)){
    y=y-1.5;
    console.log(y);
}

//Sigma

sum=0;
for(i=0; i=100 ; i++){
    sum=sum+i;
}
console.log(sum);

//Factoriel

product = 1;

for ( i = 1; i <= 12; i++) {
  product *= i;
}
console.log("Product of 1 to 12:", product);