function randomNumber() {
    return Math.random() * 10;
}

console.log(randomNumber());

let num = 5.99;
console.log(Math.floor(num));

console.log(Math.ceil(4.1));

function roundNumber(num) {
    return Math.round(num);
}

console.log(roundNumber(2.4));
console.log(roundNumber(2.5));

let balance = 150;
console.log(Math.sign(balance));

let side = 5;
let volume = Math.pow(side, 3);
console.log(volume);

console.log(Math.max(12, 45, 7, 89, 23));

console.log(Math.min(18, 25, 14));

let a = 3;
let b = 4;
let hypotenuse = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
console.log(hypotenuse);

function checkInteger(num) {
    return Number.isInteger(num);
}

console.log(checkInteger(5));
console.log(checkInteger(5.5));