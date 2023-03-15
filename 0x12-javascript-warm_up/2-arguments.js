#!/usr/bin/node
const process = require('process');
const argz = process.argv;
if (argz.length < 3) {
  console.log('No argument');
} else if (argz.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
