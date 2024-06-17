function pizzaoven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    sandwich.crustType = crustType;
    sandwich.sauceType = sauceType;
    sandwich.cheeses = cheeses;
    sandwich.toppings = toppings;
    return pizza;
}
    
var p1 = pizzaoven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"]);
console.log(s1);

var p2 = pizzaoven("hand tossed","marinara",["mozzarella", "feta"],["mushrooms", "olives", "onions"])

var p3 = pizzaoven("italian","pesto", "feta","mushrooms")

var p4 = pizzaoven("detroit pasta","tomato","mozzarella", "olives")