#!/usr/bin/node

const dict = require('./101-data.js').dict;

const resultDict = {};

Object.keys(dict).forEach(occurrences => {
  if (!resultDict[dict[occurrences]]) {
    resultDict[dict[occurrences]] = [occurrences];
  } else {
    resultDict[dict[occurrences]].push(occurrences);
  }
});

console.log(resultDict);
