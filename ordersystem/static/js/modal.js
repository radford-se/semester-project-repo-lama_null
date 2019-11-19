function modalClick(modalArea,button){
    var modal = document.getElementById(modalArea);
    var btn = document.getElementById(button);
    var span = document.getElementsByClassName("close")[0];

    btn.onclick = function() {
        modal.style.display = "table";
    }

    close.onclick = function() {
        modal.style.display = "none";
    }
    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}


