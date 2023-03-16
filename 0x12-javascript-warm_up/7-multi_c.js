#!/usr/bin/node
// Script that prints x times "C is fun".
const process = require('process');
const argz = process.argv;
const myVar = Number(argz[2]);
let i;
if (isNaN(myVar)) {
  console.log('Missing number of occurences');
} else {
  for (i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
