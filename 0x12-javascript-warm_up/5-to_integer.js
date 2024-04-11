#!/usr/bin/node
const process = require('process');
let num;
let msg = 'Not a number';
if (process.argv.length > 2) {
  num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
    num = String(num);
    msg = `My number: ${num}`;
  }
}
console.log(msg);
