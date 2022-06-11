original = document.querySelector('#original').innerHTML;
last = parseInt(document.getElementById('story').children[0].id.substr(3)); 
username = document.getElementsByTagName('META')[3].content;
user = document.querySelector('#user');
general = document.querySelector('#general');
total = 0
counter = 0

function userButton(){
    for(let i = 1; i <= last; i++) {
        let run = document.querySelector('#run' + i);
        if(run != null){
            if(document.getElementById('run'+ i).children[1].innerHTML.localeCompare(username) != 0) {
                document.querySelector('#run' + i).remove();
            }
            else{
                counter++;
                total += parseInt(document.querySelector('#run' + i).children[4].innerHTML);
            }
        }
    }
    document.querySelector('#speed').innerHTML = "Average speed: " + total/counter;
}

function generalButton() {
    document.querySelector('#original').innerHTML = original;
    document.querySelector('#speed').innerHTML = " ";
}