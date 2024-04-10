#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  let a = list.length - 1;
  while (a >= 0) {
    reversedList.push(list[a]);
    a--;
  }

  return (reversedList);
};
