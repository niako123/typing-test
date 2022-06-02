const {readFileSync, promises: fsPromises} = require('fs');
const word = document.querySelector("#word");
const text = document.querySelector("#text");
const timer = document.querySelector("#time");

// Word list
try {
    const contents = readFileSync('words.txt', 'utf-8');
    const words = contents.split(/\r?\n/);
    console.log(words);
} catch (err) {
    console.log(err);
}
