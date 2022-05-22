document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#unlimited').addEventListener('click', function() {
        document.querySelector('#forms').innerHTML = "OOOps";
    });

    document.querySelector('#limited').addEventListener('click', function() {
        document.querySelector('#forms').innerHTML = "Yeahoo";
    });
});

function onclick() {
    var clicked = document.getElementById(unlimited);
}