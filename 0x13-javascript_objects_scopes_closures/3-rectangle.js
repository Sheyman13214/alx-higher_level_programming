#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let myVar = '';
      for (let b = 0; b < this.width; b++) {
        myVar += 'X';
      }

      console.log(myVar);
    }
  }
}

module.exports = Rectangle;
