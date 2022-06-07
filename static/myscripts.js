import {words} from './words.js'
const text = document.querySelector("#textbox");
const userInput = document.querySelector("#user");
const changingSec = document.querySelector('#sec');
const changingMin = document.querySelector('#min');
const minutes = parseInt(document.querySelector("#minutes").innerHTML);
const seconds = parseInt(document.querySelector("#seconds").innerHTML);
let min = 0, sec = 0;
let counter = 0;
let upward = 0;
var hasStarted = false;
let typed_entries = 0;


// Started words
add_words_print(7);

// Choose random words
function random_word() {
    return words[Math.floor(Math.random() * (466549 - 0))];
}

// Update time
function update_time() {
    if (parseInt(changingSec.innerHTML) >= 59) {
        min++;
        sec = 0;
        changingMin.innerHTML = min;
        changingSec.innerHTML = "0" + sec;
    }
    else {
        sec++;
        if (sec < 10) {
            changingSec.innerHTML = "0" + sec;
        }
        else {
            changingSec.innerHTML = sec;
        }
    }
}

// Print the words
function add_words_print(times) {
    let number = 0;
    do {
        text.innerHTML = text.innerHTML + '<span id="word' + counter + '">' + random_word() + "</span> ";
        counter++;
        number++;
    } while (number != times)
}

// Check if the word is right
function check() {
    let word = document.querySelector("#word" + upward).innerHTML;
    let input = userInput.value;
    changeColor(word, input);
    if (input.localeCompare(word) == 0) {
        upward_word();
    }
}

// Change the word color
function changeColor(word, input) {
    for (let i = 0; i < input.length; i++) {
        if (input[i] != word[i]) {
            document.querySelector("#word" + upward).style.color = "red";
            return;
        }
    }

    document.querySelector("#word" + upward).style.color = "green";
}

// Change the upward word
function upward_word() {
    typed_entries += parseInt(document.querySelector("#word" + upward).innerHTML.length);
    document.querySelector("#word" + upward).remove();
    upward++;
    userInput.value = "";
    add_words_print(1);
}

// Calculate the time needed
function time_need() {
    return minutes * 60 + seconds;
}

// Set the timer
function timer_set() {
    var needed = time_need();
    var timesRun = 1;
    userInput.oninput = function onEvent() {
        speed(timesRun);
        check();
    }
    var interval = setInterval(function() {
        timesRun++;
        speed(timesRun);
        userInput.oninput = function onEvent() {
            check();
        }
        if((timesRun - 1) === needed){
            clearInterval(interval);
            userInput.oninput = function onEvent(event) {
                event.stopPropagation();
                alert('Timeout');
            }
            setTimeout(function () {
                $(document).ready(function($){
                    $.ajax({
                        data: JSON.stringify({
                            min : min,
                            sec : sec,
                            speed : Math.round((typed_entries/5)/(timesRun/60)),
                            configuration : 'time'
                        }),
                        type : 'POST',
                        url : '/result',
                        dataType : 'json',
                        contentType : 'application/json; charset=utf-8',
                        success : function(response) {
                            if (response.redirect) {
                                window.location = response.redirect;
                            }
                        }
                    })
                });
            }, 2000)
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
    if(!hasStarted) {
        timer_set();
        hasStarted = true;
    }
}

