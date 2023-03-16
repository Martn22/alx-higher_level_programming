#!/usr/bin/node
// Script that computes and prints a factorial
const process = require('process');
const argz = process.argv;
const myVar1 = Number(argz[2]);
function factorial (n) {
  if (!n) {
    return 1;
  } else {
    const myFact = n * (factorial(n - 1));
    return myFact;
  }
}
console.log(factorial(myVar1));
