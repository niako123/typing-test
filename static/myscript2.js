const userInput = document.querySelector("#user");
const text = document.querySelector('#textbox');
const seconds = document.querySelector('#sec');
const minutes = document.querySelector('#min');
let min = 0, sec = 0;
let upward = 0;
let typed_entries = 0;
let length = 0;
let hasStarted = false;
let randomText = "";
get_text();

// Get the content of the meta tag
function get_difficulty() {
    difficulty = document.getElementsByTagName('META')[3].content;
}

// Get the text
async function get_text() {
    try {
        content = await fetch('https://api.quotable.io/random')
        let data = await content.json();
        randomText = data.content;
        post_text(data.content);
    } catch (error) {
        console.log(error);
    }
}

// Post the text on the page
function post_text(text) {
    let words = text.split(" ");
    for (var i in words) {
        words[i] = words[i] + " ";
        length = i;
    }
    words[length] = words[length].substr(0, words[length].length - 1);
    for (var i in words) {
        document.querySelector('#textbox').innerHTML = document.querySelector('#textbox').innerHTML + '<span id="word' + i + '">' + words[i] + "</span> ";
    }
}

// Update time
function update_time() {
    if (parseInt(seconds.innerHTML) >= 59) {
        min++;
        sec = 0;
        minutes.innerHTML = min;
        seconds.innerHTML = "0" + sec;
    }
    else {
        sec++;
        if (sec < 10) {
            seconds.innerHTML = "0" + sec;
        }
        else {
            seconds.innerHTML = sec;
        }
    }
}

// Check if the word is right
function check() {
    try {
        let word = document.querySelector("#word" + upward).innerHTML;
        let input = userInput.value;
        change_color(word, input);
        if (input.localeCompare(word) == 0) {
            upward_word();
        }
    } catch (error) {
        console.log("end");
    }
    
}

// Change color
function change_color(word, input) {
    for (let i = 0; i < input.length; i++) {
        if (input[i] != word[i]) {
            document.querySelector("#word" + upward).style.color = "red";
            return;
        }
    }

    document.querySelector("#word" + upward).style.color = "blue";
}

// Change next word checked
function upward_word() {
    typed_entries += parseInt(document.querySelector("#word" + upward).innerHTML.length);
    document.querySelector("#word" + upward).style.color = "green";
    upward++;
    userInput.value = "";
}

// Timer on
function timer_set() {
    let timesRun = 0;
    var interval = setInterval(function() {
        timesRun++;
        if(upward == length) {
            clearInterval(interval);
            userInput.oninput = function onEvent(event) {
                event.stopPropagation();
                alert('Text ended');
            }
        }
        userInput.oninput = function onEvent(event) {
            speed(timesRun);
            check();
        }
        update_time();
    }, 1000);
    hasStarted = false;
}

// Count speed
function speed(time) {
    document.querySelector("#speed").innerHTML = Math.round((typed_entries/5)/(time/60));
}

// Program running
userInput.onkeypress = function () {
    if (!hasStarted) {
        timer_set();
        hasStarted = true;
    }
}