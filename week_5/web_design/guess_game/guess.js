const randomNumber = Math.floor(Math.random() * 100) + 1;
let attempt = 0;

function checkGuess(){
    const guess = parseint(document.getElementById("guessfield").value)
    attempt++;
    if (isNaN(guess)||guess<1||guess>100){
        setMessage("Please eneter a number between 1 and 100")
        return;
    } if (guess === randomNumber) {
        setmessage("Congratulations! Guessed correectly")
        document.getElementById("guessfield").disabled = true;
    } else if (guess < randomNumber) {
        setmessage("Too low, try again")
    } else if (guess < randomNumber) {
        setmessage("Too high, try again")
    }
}
function setMessage(message){
    document.getElementById("message").textContent=message
}


