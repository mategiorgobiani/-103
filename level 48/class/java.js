
let num1 = -8.5;
let num2 = Math.random() * 49 + 1; 

let min = Math.min(num1, num2);
let max = Math.max(num1, num2);

let maxInt = Math.parseInt(max); 


let sign;
if (maxInt > 0) {
    sign = "დადებითია";
} else if (maxInt < 0) {
    sign = "უარყოფითია";
} else {
    sign = "ნულია";
}


let roundedMin = Math.ceil(min);

console.log("პირველი რიცხვი: " + num1);
console.log("მეორე რიცხვი: " + num2);
console.log("მინიმალური: " + min);
console.log("მაქსიმალური: " + max);
console.log("მაქსიმალურის მთელი ნაწილი: " + maxInt);
console.log("ნიშანი: " + sign);
console.log("მინიმალური დამრგვალებული: " + roundedMin);