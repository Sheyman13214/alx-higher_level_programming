#!/usr/bin/node
const argument = process.argv[2];
if (argument === undefined || isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(argument));
}
