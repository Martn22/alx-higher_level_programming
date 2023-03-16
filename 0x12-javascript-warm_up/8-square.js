#!/usr/bin/node
// Script that prints a square.
const process = require('process');
const argz = process.argv;
const myVar = parseInt(argz[2]);
let i, j;
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (i = 0; i < myVar; i++) {
    let row = '';
    for (j = 0; j < myVar; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
