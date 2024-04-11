#!/usr/bin/node
function factr (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }
  const factorial = num * factr(num - 1);
  return factorial;
}
console.log(factr(parseInt(process.argv[2])));
