#!/usr/bin/node
// Script that prints addition of 2 integers.
const process = require('process');
const argz = process.argv;
const myVar1 = Number(argz[2]);
const myVar2 = Number(argz[3]);
function add (a, b) {
  console.log(a + b);
}
add(myVar1, myVar2);
