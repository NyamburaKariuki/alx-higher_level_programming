#!/usr/bin/node
const data = require('./101-data.js');

const occurrencesDict = {};

// Iterate through the data and populate the occurrencesDict
for (const userId in data.dict) {
    const occurrences = data.dict[userId];
    if (!occurrencesDict[occurrences]) {
        occurrencesDict[occurrences] = [userId];
    } else {
        occurrencesDict[occurrences].push(userId);
    }
}

// Print the new dictionary
console.log(occurrencesDict);
