//Data types
/* Multiline comment in javascript
1. String 
2. Integers 
3. booleans 
4. Arrays(list of items)
5. 
*/
let name = "Wayne";
let height = 50;

//On click events
//Element selector in javascript
function submit(){
    var input = document.getElementById("inputfield").value;
    var input= parseInt(input);// Data Type conversion
    console.log(typeof(input))
}

let adult = true;  // boolean data type
let fruits = ['kiwi', 'pineapple','apple', 30, false] //Array or a list
let person = {
    firstname: 'Ada',
    lastname: 'lovelace',
    age : 18,
    address : {
        country : 'Sudan',
        city:'khartoum',
        street : 'Bani bani',
},
children :[ 'Kelly','Mary']
}

function saveItem(){
    var input= document.getElementById("inputField").value
    localStorage.setItem("inputField",inputField);
    showWelcomeMessage(input)
}
function showWelcomeMessage(input){
    var messageElement = document.getElementById("showMessage")
    messageElement.textContent= "We have saved your input as "+input;
}
var storedItem = localStorage.getItem("inputField");
if (storedItem){
    showWelcomeMessage(inputField)
}