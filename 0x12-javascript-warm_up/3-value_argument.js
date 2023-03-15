#!/usr/bin/node
const process = require('process');
const argz = process.argv;
if (argz[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argz[2]);
}
