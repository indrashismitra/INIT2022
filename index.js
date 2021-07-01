async function go(){
    console.log("test")
    const response = await fetch(`https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Vodka`)
        .then(response => response.json());
        json = response
        one(json.drinks)
}

async function one(drinks){
    console.log("1")
    const response = await fetch(`http://www.randomnumberapi.com/api/v1.0/random`)
    .then(response => response.json());
    json = response
    console.log(json)
    document.getElementById("word") = drinks[json].strDrinks;
}