
(function() {
    /* Modal */
    var modalLine = document.getElementById('myLineModal');
    var modalBar = document.getElementById('myBarModal');
    var modalDonut = document.getElementById('myDonutModal');
    var modalScatter = document.getElementById('myScatterModal');

    /* Launch Button */
    // Get the button that opens the modal
    var btnLine = document.getElementById("myLineBtn");
    var btnBar = document.getElementById("myBarBtn");
    var btnDonut = document.getElementById("myDonutBtn");
    var btnScatter = document.getElementById("myScatterBtn");

    // When the user clicks on the button, open the modal
    btnLine.onclick = function() { modalLine.style.display = "block"; }
    btnBar.onclick = function() { modalBar.style.display = "block"; }
    btnDonut.onclick = function() { modalDonut.style.display = "block"; }
    btnScatter.onclick = function() { modalScatter.style.display = "block"; }
    
    // Get the <span> element that closes the modal
    var spanLine = document.getElementById("closeLine");
    var spanBar = document.getElementById("closeBar");
    var spanDonut = document.getElementById("closeDonut");
    var spanScatter = document.getElementById("closeScatter");
    
    // When the user clicks on <span> (x), close the modal
    spanLine.onclick = function() { modalLine.style.display = "none"; }
    spanBar.onclick = function() { modalBar.style.display = "none"; }
    spanDonut.onclick = function() { modalDonut.style.display = "none"; }
    spanScatter.onclick = function() { modalScatter.style.display = "none"; }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modalLine) {
            modalLine.style.display = "none";
        } else if (event.target == modalBar) {
            modalBar.style.display = "none";
        } else if (event.target == modalDonut) {
            modalDonut.style.display = "none";
        } else if (event.target == modalScatter) {
            modalScatter.style.display = "none";
        }
    }
    })();