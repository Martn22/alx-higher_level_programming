#!/usr/bin/node
const process = require('process');
const argz = process.argv;
const myVar = Number(argz[2]);
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
