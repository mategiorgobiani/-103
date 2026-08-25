// 1) let, const და var შორის განსხვავება
//let ცვლადი, რომლის მნიშვნელობის შეცვლაც შეგვიძლია.
//const ცვლადი, რომლის მნიშვნელობის შეცვლა აღარ შეგვიძლია.
//var ძველი მეთოდია ცვლადის შესაქმნელად და დღეს აღარ ვიყენებთ,
//რადგან მას აქვს scope-სთან დაკავშირებული პრობლემები და შეიძლება კოდში შეცდომები გამოიწვიოს.

// 2)
let num = 10;

console.log(num + 5);
console.log(num - 5);
console.log(num * 5);
console.log(num / 5);
console.log(num % 3);
console.log(num ** 2);

// 3)
let correctName = "მათე";
let name = prompt("შეიყვანე სახელი");

console.log(name === correctName ? "name is correct" : "name is not correct");

// 4)
let correctName2 = "nika";
let name2 = prompt("შეიყვანე სახელი:");

if (name2 === correctName2) {
    console.log("name is correct");
} else {
    console.log("name is not correct");
}