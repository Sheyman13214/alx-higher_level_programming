#!/usr/bin/node
/**
 * Square class that inherits from previous square
 */
const PreSquare = require('./5-square');

class Square extends PreSquare {
  charPrint (ch) {
    if (ch === undefined) {
      ch = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let myVar = '';
      for (let b = 0; b < this.width; b++) {
        myVar += ch;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
