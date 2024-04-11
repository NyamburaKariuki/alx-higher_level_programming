#!/usr/bin/node
let arg = process.argv[2];
let num;
if (process.argv.length > 2) {
  num = parseInt(arg);
  if (!isNaN(num)) {
    num = String(num);
    console.log('my number:', `${num}`);
} else { 
  console.log('Not a number');
}
}
