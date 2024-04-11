#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
if (!isNaN(num)) {
  console.log('my number:', `${num}`);
} else {
  console.log('Not a number');
}
